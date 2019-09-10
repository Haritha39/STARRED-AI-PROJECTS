from helperClasses.databaseHelperClass import databaseHelper

def retConnect(db_config ,logger ):   

    try:
        connectDB = databaseHelper(db_config , logger )      
        return connectDB     
    except Exception as error :
        logger.error("mysql.py - Error in connecting to mysql :: {}".format(error) )
