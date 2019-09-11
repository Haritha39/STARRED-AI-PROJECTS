import gitOperations.cloneProject
import gitOperations.checkoutBranch
import gitOperations.readEveryFile 
from classificationModel import  preprocesser
from classificationModel import model
from gitlabOperations.checkIfStarred import checkStar

def aiCodeCommit( request_data , connectDB , logger , config ):

    try:
        # print( request_data )
        commitId = request_data["commits"][-1]["id"]
        project_id = request_data["project"]["id"]
        # commitCount = request_data["total_commits_count"]
        timestamp = request_data["commits"][-1]["timestamp"]

        res = connectDB.selectProjectStarsTable(project_id)
        reslist ={}
        for each in res:
            reslist[each[0]] = each[1]

        # Checking if project is starred or not
        starCount = checkStar( project_id ,logger )
        if( starCount > 0 ):
            starred = "True"
            if( project_id in reslist.keys() ):
                connectDB.updateProjectStarsTable( "True" , starCount )
            else:
                connectDB.insertIntoProjectStarsTable( project_id , "True" , starCount )
        else:
            starred = "False"
            if( project_id in reslist.keys() ):
                connectDB.updateProjectStarsTable( ("False" , starCount) )
            else:
                connectDB.insertIntoProjectStarsTable( (project_id , "False" , starCount) )            


        # Checking if project is an AI based project or not
        cloneProject.cloning( config["git"] , request_data , logger )
        checkoutBranch.checkout_branch( config["git"],request_data , logger )
        raw_data = readEveryFile.read_file( config["git"],request_data , logger )
        processedDataList = preprocesser.preprocessData( raw_data ,logger )
        finalData = model.checkCommit( processedDataList ,logger )


        if( finalData is not None ):
            
            lang = ",".join( eachKey for eachKey in finalData.keys() )
            ai = "True"
            connectDB.insertIntoCommitTable((project_id,timestamp,commitId,lang,ai))
        else:
            connectDB.insertIntoCommitTable((project_id,timestamp,commitId,"None","False"))
        
        print( commitId , ai , starred)

        if( ai == True and starred == True ):
            logger.info(" This is STARRED AI PROJECT ")
        else:
            logger.info( " This is Not Starred AI project " )

    except Exception as error:
        logger.error("gitOperations.steps.py - {}".format(error))