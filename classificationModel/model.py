import json

def checkCommit( data ):

    # Segregating the project as ai or not ai
    try :
        dataset = open("scientificKeywords.txt","r")
        dataset = dataset.read()
        dataset = json.loads( dataset )

        keys = dataset.keys()
        values = dataset.values()

        print( type( dataset ))

        langCount = {}

        for each in data:
            for eachKey in keys:
                if( each in dataset[eachKey]):
                    if( each in langCount.keys() ):
                        langCount[each] = langCount[each] + 1
                    else:
                        langCount[each] = 1
                
        logger.info(" model is completed successfully ")    
        return langCount

    except Exception as error:
        logger.error(" classificationModel - model.py {}".format(error) )

