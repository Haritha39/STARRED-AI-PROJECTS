from flask import Flask,request
import pymysql , json 
import logging , logging.config
from helperClasses.dbconnect import retConnect
from gitOperations.steps import aiCodeCommit
import time


app = Flask( __name__ )

# Loading Configuration files
with open('./config.json') as cfg:
    config = json.load(cfg)

logging.config.fileConfig('./logging.conf')
logger = logging.getLogger("root")

logger.info("\n\n")

# Connecting to Mysql

db_config = config["mysql"]

connectDB = retConnect( db_config , logger )


@app.route("/ai" , methods = ["GET" , "POST"])
def connection():
    request_data = request.get_json()
    try:
        # print( request_data ,type(request_data))
        res = aiCodeCommit( request_data , connectDB , logger , config )
    except Exception as e:
        logger.error("init.py-commit_db.py-store()",e)
    logger.info("\n")
    return "Hello webhook from ai api"


try:    

    app.run( debug = False , host = config["flask"]["host"] , port = config["flask"]["port"] )
   
except Exception as error:
    logger.error("Error - init.py not connecting to flask {}".format(error) )



