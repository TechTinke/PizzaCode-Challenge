PHASE 4 PIZZA CODE CHALLENGE

---

SETUP

1. Clone the repo: git clone git@github.com:TechTinke/PizzaCode-Challenge.git
2. Install dependencies
3. Set up environment: export FLASK_APP=server.app:app
4. Run migrations: flask db upgrade
5. Seed database: python server/seed.py
6. Start server: python server/app.py --port 5006

---

API ENDPOINTS

- GET /restaurants: List all restaurants.
- GET /restaurants/:id: Get restaurant by ID with associated pizzas.
- DELETE /restaurants/:id: Delete restaurant by ID.
- GET /pizzas: List all pizzas.
- POST /restaurant_pizzas: Create a RestaurantPizza association.
  - Body: `{"price": 5, "pizza_id": 1, "restaurant_id": 1}`

---

TESTING WITH POSTMAN

1. Install Postman
2. Import Challenge 1 Pizzas.postman_collection.json
   - In Postman, click Import > File > Select Challenge 1 Pizzas.postman_collection.json.
3. Update URLs to http://127.0.0.1:5006 if needed.
4. Run requests in the collection to test all endpoints.
5. Check test results in the Tests tab of each request.

---

PROJECT STRUCTURE

- server/app.py: Flask application.
- server/seed.py: Database seeding script.
- server/models/: SQLAlchemy models.
- server/controllers/: Route logic.
- server/routes.py: API routes and to_dict methods.
- Challenge 1 Pizzas.postman_collection.json: Postman collection for API testing.
