# LibraryProject

A minimal Django app to manage a library catalog — books, authors and simple search/filtering. Intended as a learning project for Django fundamentals: models, admin, views, templates and basic tests.

## Features
- Book and Author models
- Admin site registration
- List and detail views for books
- Basic search and filtering
- Unit tests for models and views

## Requirements
- Python 3.8+
- Django 3.2+ (or your preferred supported version)
- (Optional) virtualenv or venv

## Quickstart

1. Clone or create the project
    ```bash
    git clone <repo-url>
    cd LibraryProject
    ```

2. Create and activate virtual environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # macOS / Linux
    .venv\Scripts\activate      # Windows
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations
    ```bash
    python manage.py migrate
    ```

5. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```

6. Run development server
    ```bash
    python manage.py runserver
    ```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/

## Testing
Run the test suite:
```bash
python manage.py test
```

## Project structure (excerpt)
```
LibraryProject/
├─ LibraryProject/        # project settings
├─ library_app/           # main app (models, views, templates)
├─ manage.py
└─ README.md
```

## Contributing
- Keep changes small and focused
- Write tests for new behavior
- Follow PEP 8

## License
Add a license file (e.g. MIT) if you plan to share the project.