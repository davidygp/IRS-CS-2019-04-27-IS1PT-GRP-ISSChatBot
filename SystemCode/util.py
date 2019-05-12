from flask import Flask, request, make_response, jsonify

# **********************
# UTIL FUNCTIONS : START
# **********************

def getjson(url):
    resp=requests.get(url)
    return resp.json()

# **********************
# UTIL FUNCTIONS : END
# **********************
