import os , git 

def read_file( gitInfo , requestData , logger ):

    # Checking out each directory and sub directories and reading every file content
    try:
        project_id = requestData["project"]["id"]
        projects_main_dir = gitInfo["projects_directory"]

        project_path = projects_main_dir + str(project_id)

        content = ""

        for root, dirs, files in os.walk( project_path ):
            for file in files:
                # print( file )
                filepath = os.path.join(root, file)
                try:
                    data = open(filepath , "r")
                    data = data.read()
                    content = content + " " + data
                    # print( content)
                except Exception:
                    # print(" passed files : ", filepath )
                    pass

        logger.info("gitOperations.readEveryFile.py - success")
        return content
    except Exception as error:
        logger.error("gitOperations.readEveryFile.py {}".format(error) )
        return
                
