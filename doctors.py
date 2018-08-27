'''
Class object to hold the data
'''
from random import randint

class DoctorData(object):
	"""Holds all data and provides fucntions for the REST requests"""
	def __init__(self):
		'''
		Adding sample doctors
		'''
		self.doctors = dict()
		self.add_doctor('John', 'Doe')
		self.add_doctor('Jane', 'Doe')

	def add_doctor(self, first_name, last_name):
		randid = str(randint(0, 9999))
		print randid
		self.doctors[randid] = Doctor(first_name, last_name)

	def get_doctors(self):
		print self.doctors
		return [(doc.last_name, doc.first_name) for doc in self.doctors.values()]


class Doctor(object):
	"""Data structure to hold doctor data"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.dates = dict()

class DateSlot(object):
	"""docstring for DateSlot"""
	def __init__(self, date):
		self.appointments = Appointment()
		self.busy = dict()

class Appointment(object):
	"""docstring for Appointment"""
	def __init__(self, patient_first_name, patient_last_name, date, time, kind):
		self.patient_last_name = patient_first_name
		self.patient_last_name = patient_last_name
		self.date = date
		self.time = time
		self.kind = kind
