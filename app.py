from flask import Flask, url_for

import doctors

app = Flask(__name__)
doc_data = doctors.DoctorData()

@app.route('/doctors')
def api_doctors():
    return str(doc_data.get_doctors())

if __name__ == '__main__':
    
    print doc_data.get_doctors()
    app.run()
