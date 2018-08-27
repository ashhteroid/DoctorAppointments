import unittest
import doctors

data = doctors.DoctorData()
doc1_id = data.doctors.keys()[0]

class DoctorDataTest(unittest.TestCase):
    """Unit test for DoctorData"""
     
    def test_get_doctors(self):
        """Unit test for get_doctors"""
        self.assertTrue(data.get_doctors())
     
    def test_add_appointment(self):
        """Unit test for add_appointment"""
        with self.assertRaises(KeyError):
            data.add_appointment({"doc_id":-100})

        with self.assertRaises(KeyError):
            data.add_appointment({})

    def test_get_appointments(self):
        """Unit test for get_appointments"""
        with self.assertRaises(KeyError):
            data.get_appointments(-100, "")

        with self.assertRaises(KeyError):
            data.get_appointments(doc1_id ,"")

    def test_del_appointment(self):
        """Unit test for el_appointment"""
        with self.assertRaises(KeyError):
            data.del_appointment(-100, "", "")

        with self.assertRaises(KeyError):
            data.del_appointment(doc1_id ,"","")


if __name__ == '__main__':
    unittest.main()