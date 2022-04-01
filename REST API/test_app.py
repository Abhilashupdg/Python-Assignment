try:
    from app import app
    import unittest
    import requests

except Exception as e:
    raise e 


class FlaskTest(unittest.TestCase):

    URL = 'http://127.0.0.1:5000/customers/add'
    URL_update = 'http://127.0.0.1:5000/customers/update/FGSH'

    data = {
    "CustomerID": "DBSH",
    "CompanyName": "ABC",
    "ContactName": "David",
    "ContactTitle": "NewContacts",
    "Address": "AddressC",
    "City": "Washington",
    "Region": "California",
    "PostalCode": 566422,
    "Fax": "030-2567989",
    "Phone": "030-6541320",
    "Country": "USA"
}
    data_new = {
    "CustomerID": "FGSH",
    "CompanyName": "GSH",
    "ContactName": "Davide Astori",
    "ContactTitle": "NewContactsA",
    "Address": "AddressD",
    "City": "Milan",
    "Region": "North Italy",
    "PostalCode": 56645622,
    "Fax": "030-256798809",
    "Phone": "030-654132520",
    "Country": "Italy"
}


    #testing to see if the get api can be reached
    def test_customers(self):
        tester = app.test_client(self)
        response = tester.get('/customers')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    #testing to see if the type returned is of json format
    def test_individual(self):
        tester = app.test_client(self)
        response = tester.get('/products')
        self.assertEqual(response.content_type, 'application/json')
    
    #testing for post requests
    def test_post_cust(self):
        response = requests.post(self.URL, json=self.data)
        self.assertEqual(response.status_code, 200)
    
    #testing for put requests
    def test_update_cust(self):
        response = requests.put(self.URL_update, json=self.data_new)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    tester = FlaskTest()
    unittest.main()

    tester.test_post_cust()
    tester.test_update_cust()