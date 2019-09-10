import os

def read_file( gitInfo , requestData , logger ):

    try:
        project_id = requestData["project"]["id"]
        projects_main_dir = gitInfo["projects_directory"]

        project_path = projects_main_dir + project_id

        content = ""

        for root, dirs, files in os.walk( project_path ):
            for file in files:
                with open(os.path.join(root, file), "r") as data:
                    content = content + " " + data.read()

        logger.info("gitOperations.readEveryFile.py - success")
        return content
    except Exception as error:
        logger.error("gitOperations.readEveryFile.py {}".format(error) )
        return
                
