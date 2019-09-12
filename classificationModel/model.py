import json , os
from ast import literal_eval

def checkCommit( data ,logger ):

    cwd = os.getcwd() + "/classificationModel/"
    # print(cwd)
    os.chdir( cwd ) 

    # Segregating the project as ai or not ai
    try :
        dataset = open("./scientificKeywords.txt","r")
        dataset = dataset.read()
        # print(type(dataset))
        dataset = eval( dataset )
        # print( type( dataset ) )
        keys = dataset.keys()
        values = dataset.values()

        langCount = {}

        # print("\n\n", data ,"\n\n" )

        for each in data:
            for eachKey in keys:
                if( each in dataset[eachKey]):
                    if( each in langCount.keys() ):
                        # print( each , eachKey , dataset[eachKey] )
                        langCount[each] = langCount[each] + 1
                    else:
                        langCount[each] = 1
                
        logger.info(" model is completed successfully ")    
        return langCount

    except Exception as error:
        logger.error(" classificationModel - model.py {}".format(error) )

