from flask import Flask
from flask import url_for
from flask import json
from flask import request

import doctors

app = Flask(__name__)
doc_data = doctors.DoctorData()

@app.route('/doctors', methods = ['GET'])
def api_doctors():
    return json.dumps(doc_data.get_doctors())

@app.route('/appointments', methods = ['GET', 'POST', 'DELETE'])
def api_appointments():
    if (request.method == 'POST' and request.headers['Content-Type'] == 'application/json'):
        #app.logger.info(request.json)
        return json.dumps(doc_data.add_appointment(request.json))
    elif request.method == 'GET':
        app.logger.info(request.json)
        return json.dumps(doc_data.get_appointments(request.json["doc_id"],request.json["date"]))
    elif request.method == 'DELETE':
        return json.dumps(doc_data.del_appointment(request.json["doc_id"], request.json["date"], request.json["apt_id"]))

if __name__ == '__main__':

    print doc_data.get_doctors()
    app.run(debug=True)
