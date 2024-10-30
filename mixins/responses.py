from typing import Any
from rest_framework.response import Response

class RhombusResponse:
    """
    Define Response format for all response cases
    """

    @staticmethod
    def default_response(
        result: Any,
        message: str,
        success: bool,
        status: int,
        headers: dict = None,
        **kwargs,
    ):
        response = {
            "message": message,
            "success": success 
        }

        if result is not None:
            response['result'] = result
        
        for key, value in kwargs.items():
            response[key] = value

        if headers is None:
            headers = {}    
            
        return Response(response, status=status, headers=headers)
        
    @staticmethod
    def success_200(
        result: Any = None,
        message: str = "Retrieved Succcessfully",
        success: bool = True,
        status: int = 200,
        **kwargs,
    ):
        return RhombusResponse.default_response(result, message, success, status, **kwargs)
        
    @staticmethod
    def error_400(
        result: Any = None,
        message: str = "Something went wrong.",
        success: bool = False,
        status: int = 400,
        **kwargs,
    ):
        return RhombusResponse.default_response(result, message, success, status, **kwargs)
        
    @staticmethod
    def error_404(
        result: Any = None,
        message: str = "Object not found",
        success: bool = False,
        status: int = 404,
        **kwargs,
    ):
        return RhombusResponse.default_response(result, message, success, status, **kwargs)
        
    @staticmethod
    def error_422(
        result: Any = None,
        message: str = "Invalid Code",
        success: bool = False,
        status: int = 422,
        **kwargs,
    ):
        return RhombusResponse.default_response(result, message, success, status, **kwargs)
        
