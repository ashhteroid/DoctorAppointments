# Doctor Appointment System

The task is to build a web back-end that supports
the following functionality via HTTP requests:
* Get a list of all doctors
* Get a list of all appointments for a particular doctor and particular day
* Add a new appointment to a doctor's calendar
* Delete an existing appointment from a doctor's calendar

Doctors should have a unique ID, a first name, and a last name. Appointments should have a unique ID,
patient first name, patient last name, date & time, and kind (New Patient or Follow-up). The
backend should respond to HTTP requests (ie GET, POST, DELETE).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
1. Clone the project
2. python app.py (To start flask app)
3. python run.py (Helper script to test the app)

### Prerequisites

flask needs to be installed

```
pip install flask
```

## Running Unit tests

python -m unittest discover -v

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used

## Authors

* **Ashwin R** - *Initial work* - [PurpleBooth](https://github.com/timeperceptron)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Sample Curl Commands for Testing

curl -X GET http://127.0.0.1:5000/doctors

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/appointments -d '{"doc_id":1132, "date": "09/25/1992", "time": "10:30", "kind":"New Patient", "patient_last_name": "Fieri", "patient_first_name":"Guy"}'

curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/appointments -d '{"doc_id":1132, "date": "09/25/1992", "time": "11:30", "kind":"New Patient", "patient_last_name": "Ramsay", "patient_first_name":"Gordon"}'

curl -H "Content-type: application/json" -X GET http://127.0.0.1:5000/appointments -d '{"doc_id":1132, "date": "09/25/1992"}'

curl -H "Content-type: application/json" -X "DELETE" http://127.0.0.1:5000/appointments -d '{"doc_id":1132, "date": "09/25/1992", "apt_id":"4083"}'