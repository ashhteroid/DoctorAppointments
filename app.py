from flask import Flask
from flask import url_for
from flask import json
from flask import request
from flask import abort
import doctors


app = Flask(__name__)
doc_data = doctors.DoctorData()

@app.route('/doctors', methods = ['GET'])
def api_doctors():
    """ API to get a list of all doctors """
    return json.dumps(doc_data.get_doctors())

@app.route('/appointments', methods = ['GET', 'POST', 'DELETE'])
def api_appointments():
    """ API to GET, POST and DELETE appointments. """
    try:
        if (request.method == 'POST' and request.headers['Content-Type'] == 'application/json'):
            return json.dumps(doc_data.add_appointment(request.json))
        elif request.method == 'GET':
            app.logger.info(request.json)
            return json.dumps(doc_data.get_appointments(request.json["doc_id"],request.json["date"]))
        elif request.method == 'DELETE':
            return json.dumps(doc_data.del_appointment(request.json["doc_id"], request.json["date"], request.json["apt_id"]))
    except (ValueError, KeyError) as exception:
        app.logger.error(exception)
        abort(400, description=exception)

if __name__ == '__main__':

    print doc_data.get_doctors()
    app.run(debug=True)
