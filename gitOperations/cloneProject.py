from git import Repo
import os , git  

def cloning( gitInfo, requestData ,logger ) :

    repo_name = requestData["project"]["path_with_namespace"]
    project_id = requestData["project"]["id"]
    # project_url = requestData["project"]["git_http_url"]
    project_url = "http://192.168.4.219:30080/Harsha/bootstrap.git"
    projects_main_dir = gitInfo["projects_directory"]

    #get all folders from project directory into dirs 

    try:
        # print(projects_main_dir)
        dirs = os.walk( "\'"+projects_main_dir+"\'" ) 
        # files = next(dirs)
        # print("next : " , next(dirs) )
    except StopIteration as error :
        logger.error("cloneProject.py error in os walk directory : {}".format(error))        
        pass # Some error handling here
    # print( dirs )
    #create directory with name project id in projects directory
    try :
        os.mkdir( projects_main_dir + str(project_id) ) 
    except Exception as error :
        logger.error("cloneProject.py error in creating directory : {}".format(error))
        pass
    #give authentication details with in the link
    user_position = project_url.find('/')
    user_position = user_position + 2
    clone_url = project_url[ 0 : user_position ] + gitInfo["username"] + ":"+ gitInfo["password"] + "@" \
                + project_url[user_position :]
    try :
        clone_msg = git.Repo.clone_from( clone_url , projects_main_dir+str(project_id) )
        logger.info("clone msg : {0}\n'{1}' project is cloned successfully... ".format( clone_msg , project_id ) )
    except Exception as error :
        logger.error("ERROR on cloing '{0}' project : {1}".format( project_id , error ) )
        return -1
    return True