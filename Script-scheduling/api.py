from flask import *
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home_page():
    data_set = [
        {
            "id": "1", 
            "street": "Pylimo g.", 
            "number": "15", 
            "status": "red"
        },
        {
            "id": "2", 
            "street": "Petro g.", 
            "number": "4", 
            "status": "redd"
        },
        {
            "id": "3", 
            "street": "Daukanto g.", 
            "number": "32", 
            "status": "redd"
        },
        {
            "id": "4", 
            "street": "Valio g.", 
            "number": "55", 
            "status": "redd"
        },
        {
            "id": "5", 
            "street": "Petrioniu g.", 
            "number": "67", 
            "status": "redd"
        }
    ]

    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == "__main__" :
    app.run(port=7777)

