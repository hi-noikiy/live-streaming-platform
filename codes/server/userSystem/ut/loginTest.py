from django.test import TestCase
import unittest
import requests
import json


class LoginTest(TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/login/login"

    def test_json_decode_error(self):
        data = {'username': 'aaa', 'password': '123', 'is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        requests.post(self.base_url, headers=headers, data=data)
        self.assertRaises(json.decoder.JSONDecodeError)

    def test_login_successful(self):
        data = {'username': 'aaa', 'password': '123', 'is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, headers=headers, data = json.dumps(data) )
        result = response.json()
        self.assertEqual(result['ret'], 1)

    def test_password_incorrect(self):
        data = {'username': 'aaa', 'password': '321', 'is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, headers=headers, data = json.dumps(data) )
        result = response.json()
        self.assertEqual(result['ret'], 2)

    def test_user_not_exist(self):
        data = {'username': 'zzz', 'password': '123', 'is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, headers=headers, data = json.dumps(data) )
        result = response.json()
        self.assertEqual(result['ret'], 0)

    def test_user_exist_anchor_not_exist(self):
        data = {'username': 'ddd', 'password': '123', 'is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, headers=headers, data = json.dumps(data) )
        result = response.json()
        self.assertEqual(result['ret'], 0)

    def test_anchor_exist_user_not_exist(self):
        data = {'username': 'aaa', 'password': '123', 'is_anchor': 0}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, headers=headers, data = json.dumps(data) )
        result = response.json()
        self.assertEqual(result['ret'], 0)

    def test_data_error_no_user(self):
        data = {'password': '123', 'is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        response=requests.post(self.base_url, headers=headers, data=json.dumps(data))
        result = response.json()
        self.assertEqual(result['ret'], 0)

    def test_data_error_no_pwd(self):
        data = {'username': 'aaa','is_anchor': 1}
        headers = {'Content-Type': 'application/json'}
        response=requests.post(self.base_url, headers=headers, data=json.dumps(data))
        result = response.json()
        self.assertEqual(result['ret'], 2)

    def test_data_error_no_isAnchor(self):
        data = {'username': 'aaa','password': '123'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.base_url, headers=headers, data=json.dumps(data))
        result = response.json()
        self.assertEqual(result['ret'], 0)

if __name__ == '__main__':
    unittest.main()