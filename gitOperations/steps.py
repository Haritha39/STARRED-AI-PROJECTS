import gitOperations.cloneProject as cloneProject
import gitOperations.checkoutBranch as checkoutBranch
import gitOperations.readEveryFile as readEveryFile
from classificationModel import  preprocesser
from classificationModel import model
from gitlabOperations.checkIfStarred import checkStar

def aiCodeCommit( request_data , connectDB , logger , config ):

    try:
        # print("request_data : ", request_data )
        commitId = request_data["commits"][-1]["id"]
        project_id = request_data["project"]["id"]
        # commitCount = request_data["total_commits_count"]
        timestamp = request_data["commits"][-1]["timestamp"]
        z = timestamp.split("Z")
        t = z[1].split("T")
        timestamp = z[0] + " " + t[0]
        print( timestamp )

        res = connectDB.selectProjectStarsTable(project_id)
        # print( "res : " , res )
        starred = "False"
        if( res != 0):
            reslist ={}
            for each in res:
                reslist[each[0]] = each[1]
            # print("reslist : ", reslist )

            # Checking if project is starred or not
            starCount = checkStar( project_id ,logger )
            # print("starCount : " , starCount )
            if( starCount > 0 ):
                starred = "True"
                if( project_id in reslist.keys() ):
                    connectDB.updateProjectStarsTable( ("True" , starCount , project_id) )
                else:
                    connectDB.insertIntoProjectStarsTable( (project_id , "True" , starCount) )
            else:
                starred = "False"
                if( project_id in reslist.keys() ):
                    connectDB.updateProjectStarsTable( ("False" , starCount ,project_id) )
                else:
                    connectDB.insertIntoProjectStarsTable( (project_id , "False" , starCount) )            


        # Checking if project is an AI based project or not
        cloneProject.cloning( config["git"] , request_data , logger )
        checkoutBranch.checkout_branch( config["git"],request_data , logger )
        raw_data = readEveryFile.read_file( config["git"],request_data , logger )
        processedDataList = preprocesser.preprocessData( raw_data ,logger )
        finalData = model.checkCommit( processedDataList ,logger )
        # print("final data :  ", finalData )

        connectDB.createCommitTable()
        if( finalData is not None ):
            
            lang = ",".join( eachKey for eachKey in finalData.keys() )
            ai = "True"
            connectDB.insertIntoCommitTable((project_id,timestamp,commitId,lang,ai))
            insert = []
            connectDB.createAITable()
            for each in finalData.keys(): 
                vals = (project_id,timestamp ,each , finalData[each])             
                insert.append( vals ) 
            print( insert )
            connectDB.insertIntoAITable( insert )
        else:
            connectDB.insertIntoCommitTable((project_id,timestamp,commitId,"None","False"))
        

        outputFile = open('../output/output.csv' , 'a+')
        outputFile.write( str(project_id) + " ," + str(commitId) + " ," + ai + " ," + starred )
        outputFile.close()
        # print( str(project_id) + " ," + str(commitId) + " ," + ai + " ," + starred )

        if( ai == "True" and starred == "True" ):
            logger.info(" This is STARRED AI PROJECT ")
        else:
            logger.info( " This is Not Starred AI project " )

    except Exception as error:
        logger.error("gitOperations.steps.py - {}".format(error))