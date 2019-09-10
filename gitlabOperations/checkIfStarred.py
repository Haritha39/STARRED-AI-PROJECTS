import gitlab,json,pprint
import requests
import pprint
# url = "http://192.168.4.219:30080"
# token = "APbpYKDXMkCUusHnCsXJ" 
# gl = gitlab.Gitlab( url,private_token = token,per_page=100 )

# proj_list = gl.projects.list(starred = True)
# # print( proj_list )

# for each in proj_list:
#     print(each,"\n\n")

def checkStar( proj_id ,logger ):

    try:
        url = "http://192.168.4.219:30080/api/v4/projects/"+str( proj_id )
        headers = {'PRIVATE-TOKEN': 'APbpYKDXMkCUusHnCsXJ'}
        result = requests.get( url , headers = headers )
        print(result)
        res = json.loads(result.text)
        # pprint.pprint(res)
        print( res["star_count"])

        starCount = res["star_count"]
        logger.info(" successfully checked starred or not ")

        return starCount
    
    except Exception as error :
        logger.error("gitlab Operations.checkIfStarred.py {}".format(error) )
        return

# checkStar(7)