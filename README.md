# Django Library Manager

Django Library Manager is a web-based application to manage library books, authors, and users with Django.



## Installation
1. Clone the repo:
    ```bash
    git clone https://github.com/AmirAflak/Django-Library-Manager.git
    cd Django-Library-Manager
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/Mac
    .\env\Scripts\activate  # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

Access it on: **`http://127.0.0.1:8000/`**  
Admin panel: **`http://127.0.0.1:8000/admin/`**

## Contributing
Feel free to fork and submit pull requests.

## License
Licensed under the MIT License.
