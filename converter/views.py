from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema, no_body
from drf_yasg import openapi
import pandas as pd
import os

from converter.openapi import InputFileParams
from converter.services import infer_and_convert_data_types
from mixins.responses import RhombusResponse


class DataConverterAPIView(APIView):
    
    """
    CSV/EXCEL data converter
    """
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description='Convert csv/excel file by pandas',
        request_body=no_body,
        manual_parameters=InputFileParams,
        operation_id="rhombus-data-convert",
        responses={
            200: openapi.Response('Data is processed successfully'),
            400: 'Something went wrong',
            404: 'Object not found',
            422: 'Invalid Code'
        }
    )
    def post(self, request, *args, **kwargs):
        # Validate the uploaded file
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return RhombusResponse.error_400(message='No uploaded file')

        valid_extensions = ['.csv', '.xls', '.xlsx']
        if os.path.splitext(uploaded_file.name)[-1].lower() not in valid_extensions:
            return RhombusResponse.error_422()

        valid_content_types = [
            'text/csv',
            'application/vnd.ms-excel',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ]
        if uploaded_file.content_type not in valid_content_types:
            return RhombusResponse.error_422()

        try:
            # Read the uploaded file into a Pandas DataFrame
            if isinstance(uploaded_file, InMemoryUploadedFile) and uploaded_file.content_type != 'text/csv':
                # Use the proper engine for file types
                if uploaded_file.content_type in ['application/vnd.ms-excel']:
                    # Read Excel 97-2003 spreadsheet file
                    df = pd.read_excel(uploaded_file, engine='xlrd')
                else:
                    # Read modern Excel file
                    df = pd.read_excel(uploaded_file, engine='openpyxl')
            else:
                # Read CSV file
                df = pd.read_csv(uploaded_file)

            # Do something with df
            result = infer_and_convert_data_types(df)
            # For example, return its shape as part of the success response
            return RhombusResponse.success_200(data={"result": result})

        except Exception as e:
            # Handle exceptions during file reading
            return RhombusResponse.error_400(message='Failed to process the uploaded file', details=str(e))
