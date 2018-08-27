import requests

while True:
    print ( "Choose:\n"
            "1. Get doctors\n"
            "2. Add appointment\n"
            "3. Show appointments \n"
            "4. Delete appointment\n" )
    choice = raw_input()
    if choice == '1':
        r = requests.get('http://127.0.0.1:5000/doctors')
        print r.text + '\n'

    elif choice == '2':
        print "Input doc_id\n"
        doc_id = raw_input()
        url = 'http://127.0.0.1:5000/appointments'
        payload = ('{"doc_id":%s, \
                    "date": "09/25/1992", \
                    "time": "10:30", \
                    "kind":"New Patient", \
                    "patient_last_name": "Fieri", \
                    "patient_first_name":"Guy"}' %doc_id)
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=payload, headers=headers)
        print r.text + '\n'

    elif choice == '3':
        print "Input doc_id\n"
        doc_id = raw_input()
        url = 'http://127.0.0.1:5000/appointments'
        payload = ('{"doc_id":%s, \
                    "date": "09/25/1992"}' %doc_id)
        headers = {'content-type': 'application/json'}
        r = requests.get(url, data=payload, headers=headers)
        print r.text + '\n'

    elif choice == '4':
        print "Input doc_id\n"
        doc_id = raw_input()
        print "Input apt_id\n"
        apt_id = raw_input()
        url = 'http://127.0.0.1:5000/appointments'
        payload = ('{"doc_id":%s, \
                    "date": "09/25/1992", \
                    "apt_id":%s}' %(doc_id,apt_id))
        headers = {'content-type': 'application/json'}
        r = requests.delete(url, data=payload, headers=headers)
        print r.text + '\n'

