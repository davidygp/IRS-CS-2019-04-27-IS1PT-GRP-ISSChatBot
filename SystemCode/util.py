import requests

# **********************
# UTIL FUNCTIONS : START
# **********************

def getjson(url):
    resp=requests.get(url)
    return resp.json()

# **********************
# UTIL FUNCTIONS : END
# **********************
