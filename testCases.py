# test_teacher_management_flask.py
import unittest
import requests

class TestTeacherManagementAPI(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'

    def test_add_teacher(self):
        url = f'{self.base_url}/add_teacher'
        data = {'name': 'John Doe', 'subject': 'Math'}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_teacher(self):
        teacher_id = 'teacher_id'  # Replace with an existing teacher ID
        url = f'{self.base_url}/update_teacher/{teacher_id}'
        data = {'name': 'Updated Name', 'subject': 'Updated Subject'}
        response = requests.put(url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_teacher(self):
        teacher_id = 'teacher_id'  # Replace with an existing teacher ID
        url = f'{self.base_url}/delete_teacher/{teacher_id}'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)

    def test_get_teachers(self):
        url = f'{self.base_url}/get_teachers'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
