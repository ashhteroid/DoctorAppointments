'''This module stores doctor data and provides methods for GET, POST and DELETE calls.   
'''
from random import randint

class DoctorData(object):
    """Class holds all data and provides functions for the HTTP requests.

    This class hold all the data in memory as doctor dict(). It provides methods for HTTP requests.
    A database can be added to store the data instead of holding it in memory. Two doctors
    are initialized in init for simplicity/scope.

    The data is stored as follows:
    Doctor Data = { Doctor_ID : DoctorInfo}
    DoctorInfo = { first name, last name,  dates}
    dates = { date: DateInfo}
    DateInfo = { Appointments, booked}
    Appointments = { Appointment ID : Appointment() }

    Attributes:
        doctors: A dictionary with key: doctor-id and Value: DoctorInfo() object.
        add_doctor: A function to add a new doctor.
        get_doctors: A function to retrieve list of all doctors.
        add_appointment: A function to add new appointment.
        get_appointment: A function to return all appointments of a doctor for a given date.
        del_appointment: A function to delete an appointment.
    """
    def __init__(self):
        '''
        Adding sample doctors
        '''
        self.doctors = dict() # Key: Doc_ID Value: DoctorInfo()
        self.add_doctor('John', 'Doe')
        self.add_doctor('Jane', 'Doe')

    def add_doctor(self, first_name, last_name):
        """Adds new doctor to to doctors dict() with a unique id. """
        doc_id = randint(1, 9999)
        self.doctors[doc_id] = DoctorInfo(first_name, last_name)

    def get_doctors(self):
        """Retrieves list of all doctors."""
        return [{doc[0]: {"first_name": doc[1].first_name, "last_name":doc[1].last_name}} for doc in self.doctors.items()]

    def add_appointment(self, json_data):
        """ Adds new appointment to the data 
            
            Args:
                json_data: A dict() of all relevant data needed for appointment. For example:
                           {"doc_id":1132, "date": "09/25/1992", "time": "10:30", "kind":"New Patient",
                            "patient_last_name": "Fieri", "patient_first_name":"Guy"}
        """
        doc_id = int(json_data['doc_id'])
        if doc_id not in self.doctors:
            raise KeyError("Invalid Doctor ID.")
        doctor = self.doctors[doc_id]
        date = json_data['date']
        time = json_data['time']
        apt_id = randint(1, 9999)
        apt_data = [json_data["patient_first_name"],
                    json_data["patient_last_name"],
                    json_data["date"],
                    json_data["time"],
                    json_data["kind"]]
        return doctor.add_appointment(date, time, apt_id, apt_data)

    def get_appointments(self, doc_id, date):
        """ Returns all appointments of a doctor for a given date."""
        if doc_id not in self.doctors:
            raise KeyError("Invalid Doc_ID")
        doctor = self.doctors[int(doc_id)]
        appointments = doctor.get_appointments(date)
        return [ {str(appointment[0]):str(appointment[1])} for appointment in appointments.items()]

    def del_appointment(self, doc_id, date, apt_id):
        """ Deletes an appointment specified by doctor id, appointment id and date"""
        if doc_id not in self.doctors:
            raise KeyError("Invalid Doc_ID")
        doctor = self.doctors[int(doc_id)]
        return doctor.del_appointment(date, apt_id)
         

class DoctorInfo(object):
    """Class holds all the data of a doctor.

    This class hold all the doctor data as DoctorInfo() objects.

    Attributes:
        first_name: Doctor first name.
        last_name: Doctor last name.
        dates: all the dates the doctor has appointments.
        get_appointment: A function to return all appointments for a given date.
        del_appointment: A function to delete an appointment.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.dates = dict() # Key: Date Value: DateInfo()

    def add_appointment(self, date, time, apt_id, apt_data):
        '''
        Retrieve Date Info for the particular date for the doctor and add appointment 
        '''
        if date not in self.dates:
            self.dates[date] = DateInfo()
        date_info = self.dates[date]
        return date_info.add_appointment(time, apt_id, apt_data)

    def get_appointments(self, date):
        """ Returns all appointment of the given date."""
        if date not in self.dates:
            raise KeyError("Not a valid date")
        return self.dates[date].appointments

    def del_appointment(self, date, apt_id):
        """ Deletes an appointment for the given date"""

        if date not in self.dates:
            raise KeyError("Given appointment date doesn't exist")
        date_info = self.dates[date]
        return date_info.del_appointment(apt_id)
        

class DateInfo(object):
    """Class holds all the data of a particular date. 
    
    Attributes:
        appointments: All the appointments. Key: Appointment_ID Value: Appointment()
        booked: A dict() that keeps track of booked slots. Assuming GUI provides a fixed 
                set of slots (Example: Every hour)
        dates: all the dates the doctor has appointments.
        add_appointment: A function to add a new appointment.
        del_appointment: A function to delete an appointment.
    """

    def __init__(self):
        self.appointments = dict() # Key: Appointment_ID Value: Appointment()
        self.booked = dict() # Key: Time Value: True

    def __str__(self):
        return str([str(appointment) for appointment in self.appointments.items()]) + str(self.booked.items())

    def add_appointment(self, time, apt_id, apt_data):
        """ Adds an appointment. """
        if time in self.booked:
            raise ValueError("The slot is already booked.")
        self.booked[time] = True
        self.appointments[int(apt_id)] = Appointment(*apt_data)
        return "Appointment booked."

    def del_appointment(self, apt_id):
        """ Deletes an appoint. """
        if apt_id not in self.appointments:
            raise KeyError("No such appointment to delete.")
        apt_time = self.appointments[int(apt_id)].time
        del self.appointments[int(apt_id)]
        del self.booked[apt_time]
        return "Appointment deleted."

class Appointment(object):
    """Class holds all the data of an appointment. """
    def __init__(self, patient_first_name, patient_last_name, date, time, kind):
        self.patient_first_name = patient_first_name
        self.patient_last_name = patient_last_name
        self.date = date
        self.time = time
        self.kind = kind
    
    def __str__(self):
        return str(self.__dict__)
