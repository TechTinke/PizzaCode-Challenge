from flask import jsonify, request
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.controllers.restaurant_controller import get_restaurants, get_restaurant, delete_restaurant
from server.controllers.pizza_controller import get_pizzas
from server.controllers.restaurant_pizza_controller import create_restaurant_pizza

def register_routes(app):
    @app.route('/restaurants', methods=['GET'])
    def restaurants_index():
        return get_restaurants()

    @app.route('/restaurants/<int:id>', methods=['GET'])
    def restaurant_show(id):
        return get_restaurant(id)

    @app.route('/restaurants/<int:id>', methods=['DELETE'])
    def restaurant_delete(id):
        return delete_restaurant(id)

    @app.route('/pizzas', methods=['GET'])
    def pizzas_index():
        return get_pizzas()

    @app.route('/restaurant_pizzas', methods=['POST'])
    def restaurant_pizzas_create():
        return create_restaurant_pizza()

    def to_dict(self, include_pizzas=False):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
        if include_pizzas:
            data["pizzas"] = [rp.pizza.to_dict() for rp in self.restaurant_pizzas]
        return data

    Restaurant.to_dict = to_dict

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

    Pizza.to_dict = to_dict

    def to_dict(self, include_restaurant_and_pizza=False):
        data = {
            "id": self.id,
            "price": self.price,
            "pizza_id": self.pizza_id,
            "restaurant_id": self.restaurant_id
        }
        if include_restaurant_and_pizza:
            data["pizza"] = self.pizza.to_dict()
            data["restaurant"] = self.restaurant.to_dict()
        return data

    RestaurantPizza.to_dict = to_dict