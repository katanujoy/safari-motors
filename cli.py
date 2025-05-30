import click
from datetime import datetime
from config.db import get_session
from models.car import Car, CarStatus
from models.customer import Customer
from models.employee import Employee
from models.sale import Sale
from sqlalchemy.orm import Session
from config.db import engine

@click.group()
def cli():
    """Safari Motors CLI - Manage your car dealership."""
    pass

### --- CAR COMMANDS ---

@cli.group()
def car():
    """Manage cars."""
    pass

@car.command('list')
@click.option('--make', default=None, help='Filter cars by make')
@click.option('--status', default=None, type=click.Choice(['available', 'sold']), help='Filter by status')
def list_cars(make, status):
    """List all cars, optionally filtered."""
    session = get_session()
    query = session.query(Car)
    if make:
        query = query.filter(Car.make.ilike(f"%{make}%"))
    if status:
        query = query.filter(Car.status == CarStatus[status])
    cars = query.all()
    if not cars:
        click.echo("No cars found with the given filters.")
        session.close()
        return
    for car in cars:
        click.echo(f"{car.id}: {car.make} {car.model} ({car.year}) - ${car.price} [{car.status.value}]")
    session.close()

@car.command('add')
@click.option('--make', prompt=True)
@click.option('--model', prompt=True)
@click.option('--year', prompt=True, type=int)
@click.option('--price', prompt=True, type=float)
def add_car(make, model, year, price):
    """Add a new car to inventory."""
    session = get_session()
    car = Car(make=make, model=model, year=year, price=price, status=CarStatus.available)
    session.add(car)
    session.commit()
    click.echo(f"Car {car.make} {car.model} added with ID {car.id}.")
    session.close()

@car.command('update')
@click.argument('car_id', type=int)
@click.option('--make', help='New make')
@click.option('--model', help='New model')
@click.option('--year', type=int, help='New year')
@click.option('--price', type=float, help='New price')
@click.option('--status', type=click.Choice(['available', 'sold']), help='New status')
def update_car(car_id, make, model, year, price, status):
    """Update an existing car."""
    session = get_session()
    car = session.query(Car).get(car_id)
    if not car:
        click.echo(f"Car with ID {car_id} not found.")
        session.close()
        return
    if make:
        car.make = make
    if model:
        car.model = model
    if year:
        car.year = year
    if price:
        car.price = price
    if status:
        car.status = CarStatus[status]
    session.commit()
    click.echo(f"Car {car.id} updated.")
    session.close()

@car.command('delete')
@click.argument('car_id', type=int)
def delete_car(car_id):
    """Delete a car."""
    session = get_session()
    car = session.query(Car).get(car_id)
    if not car:
        click.echo(f"Car with ID {car_id} not found.")
        session.close()
        return
    session.delete(car)
    session.commit()
    click.echo(f"Car {car_id} deleted.")
    session.close()

### --- CUSTOMER COMMANDS ---

@cli.group()
def customer():
    """Manage customers."""
    pass

@customer.command('list')
def list_customers():
    session = get_session()
    customers = session.query(Customer).all()
    if not customers:
        click.echo("No customers found.")
        session.close()
        return
    for cust in customers:
        click.echo(f"{cust.id}: {cust.name} | Email: {cust.email} | Phone: {cust.phone}")
    session.close()

@customer.command('add')
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
@click.option('--phone', prompt=True)
def add_customer(name, email, phone):
    session = get_session()
    customer = Customer(name=name, email=email, phone=phone)
    session.add(customer)
    session.commit()
    click.echo(f"Customer {customer.name} added with ID {customer.id}.")
    session.close()

@customer.command('update')
@click.argument('customer_id', type=int)
@click.option('--name', help='New name')
@click.option('--email', help='New email')
@click.option('--phone', help='New phone')
def update_customer(customer_id, name, email, phone):
    session = get_session()
    customer = session.query(Customer).get(customer_id)
    if not customer:
        click.echo(f"Customer with ID {customer_id} not found.")
        session.close()
        return
    if name:
        customer.name = name
    if email:
        customer.email = email
    if phone:
        customer.phone = phone
    session.commit()
    click.echo(f"Customer {customer.id} updated.")
    session.close()

@customer.command('delete')
@click.argument('customer_id', type=int)
def delete_customer(customer_id):
    session = get_session()
    customer = session.query(Customer).get(customer_id)
    if not customer:
        click.echo(f"Customer with ID {customer_id} not found.")
        session.close()
        return
    session.delete(customer)
    session.commit()
    click.echo(f"Customer {customer_id} deleted.")
    session.close()

### --- EMPLOYEE COMMANDS ---

@cli.group()
def employee():
    """Manage employees."""
    pass

@employee.command('list')
def list_employees():
    session = get_session()
    employees = session.query(Employee).all()
    if not employees:
        click.echo("No employees found.")
        session.close()
        return
    for emp in employees:
        click.echo(f"{emp.id}: {emp.name} | Position: {emp.position}")
    session.close()

@employee.command('add')
@click.option('--name', prompt=True)
@click.option('--position', prompt=True)
def add_employee(name, position):
    session = get_session()
    employee = Employee(name=name, position=position)
    session.add(employee)
    session.commit()
    click.echo(f"Employee {employee.name} added with ID {employee.id}.")
    session.close()

@employee.command('update')
@click.argument('employee_id', type=int)
@click.option('--name', help='New name')
@click.option('--position', help='New position')
def update_employee(employee_id, name, position):
    session = get_session()
    employee = session.query(Employee).get(employee_id)
    if not employee:
        click.echo(f"Employee with ID {employee_id} not found.")
        session.close()
        return
    if name:
        employee.name = name
    if position:
        employee.position = position
    session.commit()
    click.echo(f"Employee {employee.id} updated.")
    session.close()

@employee.command('delete')
@click.argument('employee_id', type=int)
def delete_employee(employee_id):
    session = get_session()
    employee = session.query(Employee).get(employee_id)
    if not employee:
        click.echo(f"Employee with ID {employee_id} not found.")
        session.close()
        return
    session.delete(employee)
    session.commit()
    click.echo(f"Employee {employee_id} deleted.")
    session.close()

### --- SALE COMMANDS ---

@cli.group()
def sale():
    """Manage sales."""
    pass

@sale.command('list')
def list_sales():
    session = get_session()
    sales = session.query(Sale).all()
    if not sales:
        click.echo("No sales found.")
        session.close()
        return
    for s in sales:
        click.echo(f"Sale {s.id}: Car {s.car.make} {s.car.model} sold to {s.customer.name} by {s.employee.name} on {s.date}")
    session.close()

@sale.command('add')
def add_sale():
    """Add a new sale record."""
    session = Session(bind=engine)
    try:
        # Ask for Car ID and validate it's a sold car
        while True:
            car_id = click.prompt("Enter Car ID (must be a sold car)", type=int)
            car = session.query(Car).filter(Car.id == car_id, Car.status == CarStatus.sold).first()
            if car:
                break
            click.echo("Car not found or is not sold. Please enter a valid sold car ID.")

        # Ask for Customer ID and validate
        while True:
            customer_id = click.prompt("Enter Customer ID", type=int)
            customer = session.query(Customer).filter(Customer.id == customer_id).first()
            if customer:
                break
            click.echo("Customer not found. Please enter a valid customer ID.")

        # Ask for Employee ID and validate
        while True:
            employee_id = click.prompt("Enter Employee ID", type=int)
            employee = session.query(Employee).filter(Employee.id == employee_id).first()
            if employee:
                break
            click.echo("Employee not found. Please enter a valid employee ID.")

        # Create the sale record
        now = datetime.utcnow()
        sale = Sale(
            car_id=car.id,
            customer_id=customer.id,
            employee_id=employee.id,
            price=car.price,
            date=now,
            created_at=now
        )
        session.add(sale)
        session.commit()
        click.echo(f"Sale recorded successfully! Sale ID: {sale.id}")

    except Exception as e:
        click.echo(f"Error adding sale: {e}")
        session.rollback()
    finally:
        session.close()

@sale.command('delete')
@click.argument('sale_id', type=int)
def delete_sale(sale_id):
    session = get_session()
    sale = session.query(Sale).get(sale_id)
    if not sale:
        click.echo(f"Sale with ID {sale_id} not found.")
        session.close()
        return
    # Mark car as available again if sale deleted
    sale.car.status = CarStatus.available
    session.delete(sale)
    session.commit()
    click.echo(f"Sale {sale_id} deleted and car status updated to available.")
    session.close()

if __name__ == '__main__':
    cli()