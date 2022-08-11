# SIFTORA

## 💄 Project Description

This is the backend of the full-stack application, [Siftora](https://github.com/jyaymie/siftora-frontend).

It follows a RESTful architectural style and has full CRUD functionality with (currently) two tables, 'bins' and 'products', which hold a many-to-many relationship. Here is what you can do with the Siftora API:

| HTTP Verb | URL              | Description               |
| --------- | ---------------- | ------------------------- |
| GET       | api/bins         | Retrieve all Bins         |
| GET       | api/bins/:id     | Retrieve a Bin by :id     |
| GET       | api/products     | Retrieve all Products     |
| GET       | api/products/:id | Retrieve a Product by :id |
| POST      | api/bins         | Create a new Bin          |
| POST      | api/products     | Create a new Product      |
| PUT       | api/bins/:id     | Update a Bin by :id       |
| PUT       | api/products/:id | Update a Product by :id   |
| DELETE    | api/bins/:id     | Delete a Bin by :id       |
| DELETE    | api/products/:id | Delete a Product by :id   |

## 👩‍💻 Technologies

This API was built using Python and Django REST Framework (DRF), as well as PostgreSQL (for the database) and Heroku (for deployment).

## 🛠 Installation

1. Fork and clone this repository, and change into the new `siftora-backend` directory.
2. Run `python3 -m venv env` to create a virtual environment.
3. Install the required dependencies with `pip install -r requirements.txt`, and apply tables to the database with the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
4. Use `python3 manage.py runserver` to start up your Django server, and ta-da! You can now access the API service. Go to http://localhost:8000/api/bins to view the bins. Happy sifting!

## 🤝 Contribution

There is always room for improvement! If you have any suggestions, please submit an issue or create a pull request.

##

✨ Thank you for checking out Siftora! ✨
