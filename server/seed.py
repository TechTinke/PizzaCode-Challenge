import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import db
from server.app import app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    try:
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add restaurants
        restaurant1 = Restaurant(name="Dominion Pizza", address="123 Main St")
        restaurant2 = Restaurant(name="Pizza Hut", address="456 Oak Ave")
        db.session.add_all([restaurant1, restaurant2])

        # Add pizzas
        pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
        pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        db.session.add_all([pizza1, pizza2])

        # Add restaurant_pizzas
        rp1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
        rp2 = RestaurantPizza(price=12, restaurant=restaurant1, pizza=pizza2)
        rp3 = RestaurantPizza(price=11, restaurant=restaurant2, pizza=pizza1)
        db.session.add_all([rp1, rp2, rp3])

        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        db.session.rollback()
        print(f"Error seeding database: {str(e)}")