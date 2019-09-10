from git import Repo

def cloning( gitInfo, requestData ,logger ) :

    repo_name = requestData["project"]["path_with_namespace"]
    project_id = requestData["project"]["id"]
    project_url = requestData["project"]["git_http_url"]
    projects_main_dir = gitInfo["projects_directory"]

    #get all folders from project directory into dirs 
    dirs = os.walk( projects_main_dir ).next()[1]
    
    #create directory with name project id in projects directory
    try :
        os.mkdir( projects_main_dir + project_id ) 
    except Exception as error :
        pass
    #give authentication details with in the link
    user_position = project_url.find('/')
    user_position = user_position + 2
    clone_url = project_url[ 0 : user_position ] + gitInfo["username"] + ":"+ gitInfo["password"] + "@" \
                + project_url[user_position :]
    try :
        clone_msg = git.Repo.clone_from( clone_url , projects_main_dir+project_id )
        logger.info("clone msg : {0}\n'{1}' project is cloned successfully... ".format( clone_msg , project_id ) )
    except Exception as error :
        logger.error("ERROR on cloing '{0}' project : {1}".format( project_id , error ) )
        return -1
    return True