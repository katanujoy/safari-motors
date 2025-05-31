from faker import Faker
from faker_vehicle import VehicleProvider  
from sqlalchemy.orm import Session
from datetime import datetime
from config.db import Base, engine
from models.car import Car
from models.customer import Customer
from models.employee import Employee
from models.sale import Sale


def seed_data(num_cars=10, num_customers=10, num_employees=10, num_sales=10):
    fake = Faker()
    fake.add_provider(VehicleProvider) 
    session = Session(bind=engine)

    try:
        print("Clearing existing data...")
        session.query(Sale).delete()
        session.query(Employee).delete()
        session.query(Customer).delete()
        session.query(Car).delete()
        session.commit()
        print("Existing data cleared.")

        now = datetime.utcnow()

        # Create cars, with at least 1/3 marked as sold
        cars = []
        num_sold_cars = max(1, num_cars // 3)
        for i in range(num_cars):
            status = "sold" if i < num_sold_cars else "available"
            car = Car(
                make=fake.vehicle_make(),         
                model=fake.vehicle_model(),         
                year=fake.random_int(min=2005, max=2024),  
                price=fake.random_int(min=20000, max=150000),
                status=status,
                created_at=now
            )
            cars.append(car)
        session.add_all(cars)
        session.commit()
        print(f"Created {len(cars)} cars ({num_sold_cars} sold).")

        # Create customers
        customers = []
        for _ in range(num_customers):
            customer = Customer(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                created_at=now
            )
            customers.append(customer)
        session.add_all(customers)
        session.commit()
        print(f"Created {len(customers)} customers.")

        # Create employees
        positions = ["Manager", "Salesperson", "Technician", "Receptionist"]
        employees = []
        for _ in range(num_employees):
            employee = Employee(
                name=fake.name(),
                position=fake.random_element(elements=positions),
                email=fake.unique.email(),
                phone=fake.phone_number(),
                created_at=now
            )
            employees.append(employee)
        session.add_all(employees)
        session.commit()
        print(f"Created {len(employees)} employees.")

        # Create sales only for sold cars
        sold_cars = session.query(Car).filter(Car.status == "sold").all()  
        max_sales = min(num_sales, len(sold_cars), len(customers), len(employees))

        if max_sales == 0:
            print("No sold cars available to create sales.")
        else:
            sales = []
            for i in range(max_sales):
                sale = Sale(
                    car_id=sold_cars[i].id,
                    customer_id=customers[i].id,
                    employee_id=employees[i].id,
                    price=sold_cars[i].price,
                    date=now,
                    created_at=now
                )
                sales.append(sale)
            session.add_all(sales)
            session.commit()
            print(f"Created {len(sales)} sales.")

        print("Database seeded with fake data successfully!")

    except Exception as e:
        print(f"Error during seeding: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    print("Creating tables if they don't exist...")
    Base.metadata.create_all(bind=engine)
    print("Tables ready.")
    seed_data()
