# Data Converter API

A Django application that provides a REST API for converting CSV/Excel files into a processed data format using pandas.

## Features

- Convert CSV and Excel files to a standardized format.
- Supports `.csv`, `.xls`, and `.xlsx` file formats.
- Utilizes pandas for data manipulation.
- Provides clear and consistent API response messages.

## Requirements

- Python 3.12
- Django 5.5.1
- Django REST Framework
- Pandas
- Openpyxl (for `.xlsx` files)
- Xlrd (for `.xls` files)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/justint0x/csv-frame-converter-api.git
   cd csv-frame-converter-api
   ```

2. **Set up a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the API:**

   By default, the server runs at `http://127.0.0.1:8000/`. Use a tool like Postman or `curl` to interact with the API.

2. **API Endpoint:**

   - **URL:** `/api/converter/`
   - **Method:** `POST`
   - **Description:** Upload a CSV or Excel file to convert it.
   - **Parameters:**
     - `file` (required): The CSV or Excel file to be converted.

3. **Example using `curl`:**

   ```bash
   curl -X POST http://127.0.0.1:8000/api/converter/ \
        -F 'file=@path/to/your/file.csv'
   ```

4. **Response:**

   A successful response will contain the processed data or metadata indicating successful processing. Error responses will include error messages detailing what went wrong.

## Testing

Run tests using the Django test framework:

```bash
python manage.py test
```

This will execute the tests defined in your test suite, ensuring the API behaves as expected.

## Documentation

Swagger OpenAI documentation is implemented.

`http://localhost:8000/api/swagger/`

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
