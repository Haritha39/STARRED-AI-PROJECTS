import pymysql
from helperClasses.constantClass import databaseConstants

class databaseHelper(databaseConstants):

    def __init__( self , db_config ,logger ):
        self.logger = logger
        self.config = db_config
        self.logger.info(" This is a constructor ")
        self.connectDatabase()

    def connectDatabase(self):        
        try:
            dbConnection = pymysql.connect( host = self.config["host"],port = self.config["port"], \
                                            user = self.config["root"],\
                                            password = self.config["passwd"], db = self.config["database"] )
            dbConnection.autocommit(True)
            self.logger.info("Successfully Connected to Mysql Database")
            self.cursor = dbConnection.cursor()   
                     
        except Exception as error :
            self.logger.error("mysql.py - Error in connecting to mysql :: {}".format(error) )
        return

    def createCommitTable( self ):

        tableName = databaseConstants.table_commit
        tableDesc = databaseConstants.table_commit_pid + " int," \
                    + databaseConstants.table_commit_time + " datetime," \
                    + databaseConstants.table_commit_cid + " TEXT," \
                    +databaseConstants.table_commit_lang + " TEXT," \
                    + databaseConstants.table_commit_ai + " TEXT"
                    
        try:
            self.cursor.execute( "CREATE TABLE IF NOT EXISTS "+ tableName + "("+ tableDesc + ")" )
            
            self.logger.info( " Table is created : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in createCommitTable method :: {}".format(error) )

    def selectCommitTable( self , values ):
        
        tableName = databaseConstants.table_commit
        condition = databaseConstants.table_commit_cid
        try:
            if( values is not None ):
                result = self.cursor.execute("SELECT * FROM " + tableName + " WHERE " + condition +"=%s" , (values) )     
            else:
                result = self.cursor.execute( "SELECT *  FROM " + tableName )     
            self.logger.info( " Data  is retireived from : {}".format(tableName) )
            return result
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in selectCommitTable method :: {}".format(error) )
            return False

    def insertIntoCommitTable( self , values ):
        tableName = databaseConstants.table_commit
        tableDesc = "("+databaseConstants.table_commit_pid + "," \
                       +databaseConstants.table_commit_time + "," \
                       +databaseConstants.table_commit_cid + "," \
                       +databaseConstants.table_commit_lang + "," \
                       +databaseConstants.table_commit_ai + ")" 
        formatString = "(%s,%s,%s,%s,%s)"

        try:   
            insert = self.cursor.execute("INSERT INTO "+ tableName + tableDesc + " VALUES " + formatString , values )     
            self.logger.info( " Data  is inserted into : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in insertIntoCommitTable method :: {}".format(error) )

    def updateCommitTable( self , setValues ):

        tableName = databaseConstants.table_commit
        setColumns = databaseConstants.table_commit_lang + "=%s," + databaseConstants.table_commit_status + "=%s," + databaseConstants.table_commit_ai + "=%s"
        condition = databaseConstants.table_commit_cid

        try:
            update = self.cursor.execute("UPDATE "+ tableName +" SET " + setColumns + " WHERE "+ condition + "=%s",setValues )
            self.logger.info( " Data  is updated in : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in updateCommitTable method :: {}".format(error) )

        

    def createProjectStarsTable( self ):

        tableName = databaseConstants.table_star
        tableDesc = databaseConstants.table_star_pid + " int," \
                    +databaseConstants.table_star_starred + " char(16) ," \
                    +databaseConstants.table_star_starred_count + " int"
                    
        
        try:
            self.cursor.execute( "CREATE TABLE IF NOT EXISTS "+ tableName + "("+ tableDesc + ")" )
            
            self.logger.info( " Table is created : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in createProjectStarsTable method :: {}".format(error) )


    def selectProjectStarsTable( self , values ):
        
        tableName = databaseConstants.table_star
        condition = databaseConstants.table_star_pid
        getColumns = databaseConstants.table_star_pid + ","+databaseConstants.table_star_starred_count

        try:
            if( values is not None ):
                result = self.cursor.execute("SELECT "+ getColumns+" FROM " + tableName + " WHERE " + condition +"=%s" , (values) )     
            else:
                result = self.cursor.execute( "SELECT *  FROM " + tableName )     
            self.logger.info( " Data  is retireived from : {}".format(tableName) )
            return result
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in selectProjectStarsTable method :: {}".format(error) )
            return False
    
    def insertIntoProjectStarsTable( self , values ):
        tableName = databaseConstants.table_star
        tableDesc = "("+databaseConstants.table_star_pid + "," \
                       +databaseConstants.table_star_starred + "," \
                       +databaseConstants.table_star_starred_count + ")" 
        formatString = "(%s,%s,%s)"

        try:   
            insert = self.cursor.execute("INSERT INTO "+ tableName + tableDesc + " VALUES " + formatString , values )     
            self.logger.info( " Data  is inserted into : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in insertIntoProjectStarsTable method :: {}".format(error) )

    def updateProjectStarsTable( self , setValues ):

        tableName = databaseConstants.table_star
        setColumns = databaseConstants.table_star_starred + "=%s," + databaseConstants.table_star_starred_count + "=%s"
        condition = databaseConstants.table_star_pid

        try:
            update = self.cursor.execute("UPDATE "+ tableName +" SET " + setColumns + " WHERE "+ condition + "=%s",setValues )
            self.logger.info( " Data  is updated in : {}".format(tableName) )
        except Exception as error:
            self.logger.error("databaseHelperClass.py - Error in updateProjectStarsTable method :: {}".format(error) )

        