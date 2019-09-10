from git import Repo

def checkout_branch( gitInfo, requestData , logger ):

    project_id = req_Data["project"]["id"]
    projects_main_dir = gitInfo["projects_directory"]

    project_path = projects_main_dir + project_id
    branch =  requestData["ref"].split("/")[-1]

    logger.info("read_queue.GitRepo.checkout_branch")
    try :
        repo = git.Repo ( project_path )
    except Exception as error :
        logger.error("Error on project path : %s" %error)
    #fetch latest changes in remote repository
    try :
        changes = repo.remote().fetch()
    except Exception as error :
        logger.error("ERROR on fetching : %s" %error )
        return -1
    #checkout to given branch
    try :
        checkout_msg = repo.git.checkout ( branch )
    except Exception as error :
        logger.error("ERROR on checkout to '{0}' branch : {1}".format( branch ,  error ) )
        return -1
    #pull changes
    try :
        pull_msg = repo.remotes.origin.pull()
        logger.info("checkout to '%s' branch and changes are pulled successfully..." %branch )
    except Exception as error :
        logger.error("ERROR on pulling changes from '{0}' branch : {1}".format( branch , error ) )
        return -1
    return True