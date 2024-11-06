from rest_framework.views import APIView
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema, no_body
from drf_yasg import openapi
import os

from converter.openapi import InputFileParams
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

        valid_content_types = ['text/csv', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
        if uploaded_file.content_type not in valid_content_types:
            return RhombusResponse.error_422()

        return RhombusResponse.success_200()