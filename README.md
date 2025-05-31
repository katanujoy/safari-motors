# Safari Motors CLI

Safari Motors is a command-line car dealership management system built with Python. It allows users to manage cars, customers, employees, and sales for a virtual car yard tailored to the Kenyan market.


## Features

- Add and manage cars, customers, employees, and sales
- Search and filter cars by make, price, or status
- View and track sales history
- Built with `Click` for a user-friendly command-line interface


## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/katanujoy/safari-motors.git
   cd safari-motors
2. **Install Pipenv (if not already installed):**

pip install pipenv
3. **Install dependencies:**

pipenv install
4. **Activate the virtual environment**

pipenv shell
5. **Run database migrations:**

alembic upgrade head
6. **Seed the database with sample data (optional):**
python seed.py

7. **Start the CLI application:**

python cli.py

## Technologies Used
Python 3.11+

Pipenv – for managing the virtual environment

SQLAlchemy – object-relational mapper (ORM)

Alembic – database migrations

Click – command-line interface creation

## Project Structure

safari-motors/
├── Pipfile
├── Pipfile.lock
├── README.md
├── cli.py
├── config/
│   └── db.py
├── models/
│   ├── __init__.py
│   ├── car.py
│   ├── customer.py
│   ├── employee.py
│   └── sale.py
├── migrations/
│   └── (Alembic migration files)
└── seed.py

## Commands
python cli.py car list           # View all cars
python cli.py car add            # Add a new car
python cli.py customer add       # Register a new customer
python cli.py sale add           # Record a new sale
python cli.py sale list          # View all sales

## BY:
Joy Katanu
GitHub: @katanujoy
Email: katanujoyy99@gmail.com

## License
This project is open-source and available under the MIT License.