# test.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import os


class DataConverterAPITestCase(APITestCase):

    def setUp(self):
        # Prepare paths to test files
        self.csv_file_path = os.path.join(os.path.dirname(__file__), 'test_data.csv')
        self.invalid_file_path = os.path.join(os.path.dirname(__file__), 'test_data.txt')

        # URLs
        self.url = '/api/converter/'

    def test_convert_csv_file(self):
        # Create a simple CSV file for testing
        with open(self.csv_file_path, 'w') as f:
            f.write('col1,col2,col3\n1,2,3\n4,5,6')

            # Open and read the file
        with open(self.csv_file_path, 'rb') as csv_file:
            # Upload the file in a request
            uploaded_file = SimpleUploadedFile('test_data.csv', csv_file.read(), content_type='text/csv')
            response = self.client.post(self.url, {'file': uploaded_file}, format='multipart')

            # Check if the response code is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], True)

    def test_no_file_uploaded(self):
        # Test request without a file
        response = self.client.post(self.url, format='multipart')

        # Check if the response code is 400
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'No uploaded file')

    def test_invalid_file_extension(self):
        # Create an invalid file for testing
        with open(self.invalid_file_path, 'w') as f:
            f.write('This is an invalid file format')

            # Open and read the file
        with open(self.invalid_file_path, 'rb') as invalid_file:
            # Upload the file in a request
            uploaded_file = SimpleUploadedFile('test_data.txt', invalid_file.read(), content_type='text/plain')
            response = self.client.post(self.url, {'file': uploaded_file}, format='multipart')

            # Check if the response code is 422
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    def tearDown(self):
        # Clean up created files
        if os.path.exists(self.csv_file_path):
            os.remove(self.csv_file_path)
        if os.path.exists(self.invalid_file_path):
            os.remove(self.invalid_file_path)