import unittest
from flask import Flask, render_template
from main import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'EMAIL SENDING AUTOMATION', response.data)

    def test_sel2_page_get(self):
        response = self.app.get('/sel2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email Form', response.data)

    def test_sel2_page_post(self):
        response = self.app.post('/sel2', data=dict(
            email='test@example.com',
            subject='Test Subject',
            content='Test Content'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email Sending is now Complete!', response.data)

    def test_selection_page_get(self):
        response = self.app.get('/selection')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email Sending Automation', response.data)

    def test_automation_get_page(self):
        response = self.app.get('/forautom')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email Sending Automation', response.data)

    # Add more test cases for other routes and functionalities

if __name__ == '__main__':
    unittest.main()