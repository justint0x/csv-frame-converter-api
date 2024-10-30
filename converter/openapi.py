from drf_yasg import openapi

InputFileParams = [
    openapi.Parameter(
        "file",
        in_=openapi.IN_FORM,
        type=openapi.TYPE_FILE,
        required=True,
        consumes=["application/x-www-form-urlencoded", "multipart/form-data"],
    ),
]