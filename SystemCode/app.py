from flask import Flask, request, make_response, jsonify
import util

app = Flask(__name__)

# *****************************
# Intent Handlers funcs : START
# *****************************

# ***************************
# Intent Handlers funcs : END
# ***************************


# *****************************
# WEBHOOK MAIN ENDPOINT : START
# *****************************
@app.route('/', methods=['POST'])
def webhook():
   req = request.get_json(silent=True, force=True)
   intent_name = req["queryResult"]["intent"]["displayName"]
   print(req)
 
   if intent_name == "GetWeatherIntent" :
       respose_text = getWeatherIntentHandler(req) 
   elif intent_name == "GetUVIndexIntent" :
       respose_text = getUVIndexHandler(req)
   else:
       respose_text = "No intent matched"
   # Branching ends here

   # Finally sending this response to Dialogflow.
   return make_response(jsonify({'fulfillmentText': respose_text}))

# ***************************
# WEBHOOK MAIN ENDPOINT : END
# ***************************

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
