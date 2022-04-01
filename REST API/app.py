from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import decimal
import flask.json

app = Flask(__name__)

# Initial Setup
#Creating a JSON serializer
class EncoderJSON(flask.json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(EncoderJSON, self).default(obj)


app.json_encoder = EncoderJSON
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:newpassword@localhost/northwind' #Connecting and loading the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#The automap base class on SQLALchemy creates a database class from the tables that are present in the MYSQL database
base = automap_base()
base.prepare(db.engine, reflect=True)

#Creating database classes for products, customers and orders table
Products = base.classes.products
Customers = base.classes.customers
Orders = base.classes.orders



##### Insert, update and select on customers
@app.route('/')
def homepage():
    return "You have landed on the homepage of this web application. You can retrieve information from the Northwind database from this application."


@app.route('/customers', methods=['GET']) #Get all the customers information
def customers_everyone():
    results = db.session.query(Customers).all()
    cust = []
    for result in results:
        result = result.__dict__
        del result['_sa_instance_state']
        cust.append(result)
    return flask.jsonify(cust)


@app.route('/customers/<id>', methods=['GET']) #Get customer by id
def customer_individual(id):
    results = db.session.query(Customers).get(id)
    if results == None:
        return "Customer with the ID not found"
    results = results.__dict__
    del results['_sa_instance_state']
    return flask.jsonify(results)



@app.route('/customers/add', methods=['POST']) #Add a new customer
def add_customer():
    new_cust = Customers(CustomerID = request.json['CustomerID'],
                         CompanyName = request.json['CompanyName'],
                         ContactName = request.json['ContactName'],
                         ContactTitle = request.json['ContactTitle'],
                         Address = request.json['Address'],
                         City = request.json['City'],
                         Region = request.json['Region'],
                         PostalCode = request.json['PostalCode'],
                         Country = request.json['Country'],
                         Phone = request.json['Phone'],
                         Fax = request.json['Fax'],)
    db.session.add(new_cust)
    db.session.commit()
    return "New Customer Added Successfuly!"


@app.route('/customers/update/<id>', methods=['PUT']) #Update the details of a customer
def update_customer(id):
    cust = db.session.query(Customers).get(id)
    if cust == None:
        return "Customer Not Found!"
    cust.CustomerID = request.json['CustomerID']
    cust.CompanyName = request.json['CompanyName']
    cust.ContactName = request.json['ContactName']
    cust.ContactTitle = request.json['ContactTitle']
    cust.Address = request.json['Address']
    cust.City = request.json['City']
    cust.Region = request.json['Region']
    cust.PostalCode = request.json['PostalCode']
    cust.Country = request.json['Country']
    cust.Phone = request.json['Phone']
    cust.Fax = request.json['Fax']

    db.session.commit()
    return "Customer Details Updated Successfuly!"


##### Insert, update and select on products
@app.route('/products', methods=['GET']) #Select all products
def all_products():
    results = db.session.query(Products).all()
    prod = []
    for result in results:
        result = result.__dict__
        del result['_sa_instance_state']
        prod.append(result)
    return flask.jsonify(prod)


@app.route('/products/<id>', methods=['GET']) #Select products based on id
def product_individual(id):
    results = db.session.query(Products).get(id)
    if results == None:
        return "Product with the ID not found"
    results = results.__dict__
    del results['_sa_instance_state']
    return flask.jsonify(results)



@app.route('/products/add', methods=['POST']) #Add new products
def add_product():
    new_cust = Products(ProductID = request.json['ProductID'],
                         ProductName = request.json['ProductName'],
                         SupplierID = request.json['SupplierID'],
                         CategoryID = request.json['CategoryID'],
                         QuantityPerUnit = request.json['QuantityPerUnit'],
                         UnitPrice = request.json['UnitPrice'],
                         UnitsInStock = request.json['UnitsInStock'],
                         UnitsOnOrder = request.json['UnitsOnOrder'],
                         ReorderLevel = request.json['ReorderLevel'],
                         Discontinued = request.json['Discontinued'],)
    db.session.add(new_cust)
    db.session.commit()
    return "New Product Added Successfuly!"


@app.route('/products/update/<id>', methods=['PUT']) #Update a product
def update_product(id):
    cust = db.session.query(Products).get(id)
    if cust == None:
        return "Product Not Found!"
    cust.ProductID = request.json['ProductID']
    cust.ProductName = request.json['ProductName']
    cust.SupplierID = request.json['SupplierID']
    cust.CategoryID = request.json['CategoryID']
    cust.QuantityPerUnit = request.json['QuantityPerUnit']
    cust.UnitPrice = request.json['UnitPrice']
    cust.UnitsInStock = request.json['UnitsInStock']
    cust.UnitsOnOrder = request.json['UnitsOnOrder']
    cust.ReorderLevel = request.json['ReorderLevel']
    cust.Discontinued = request.json['Discontinued']

    db.session.commit()
    return "Product Details Updated Successfuly!"


#### Insert, update and select on orders
@app.route('/orders', methods=['GET']) #Select all orders
def all_orders():
    results = db.session.query(Orders).all()
    ord = []
    for result in results:
        result = result.__dict__
        del result['_sa_instance_state']
        ord.append(result)
    return flask.jsonify(ord)


@app.route('/orders/<id>', methods=['GET']) #Select orders based on id
def order_individual(id):
    results = db.session.query(Orders).get(id)
    if results == None:
        return "Order with the ID not found"
    results = results.__dict__
    del results['_sa_instance_state']
    return flask.jsonify(results)



@app.route('/orders/add', methods=['POST']) #Add new Orders
def add_order():
    new_order = Orders(OrderID = request.json['OrderID'],
                         CustomerID = request.json['CustomerID'],
                         EmployeeID = request.json['EmployeeID'],
                         OrderDate = request.json['OrderDate'],
                         RequiredDate = request.json['RequiredDate'],
                         ShippedDate = request.json['ShippedDate'],
                         Freight = request.json['Freight'],
                         ShipName = request.json['ShipName'],
                         ShipAddress = request.json['ShipAddress'],
                         ShipCity = request.json['ShipCity'],
                         ShipRegion = request.json['hipRegion'],
                         ShipPostalCode = request.json['ShipPostalCode'],
                         ShipCountry = request.json['hipCountry'])
    db.session.add(new_order)
    db.session.commit()
    return "New Order Added Successfuly!"


@app.route('/orders/update/<id>', methods=['PUT']) #Update an Order
def update_order(id):
    order = db.session.query(Orders).get(id)
    if order == None:
        return "Product Not Found!"
    order.OrderID = request.json['OrderID']
    order.CustomerID = request.json['CustomerID']
    order.EmployeeID  = request.json['EmployeeID ']
    order.OrderDate = request.json['OrderDate']
    order.RequiredDate = request.json['RequiredDate']
    order.ShippedDate = request.json['ShippedDate']
    order.Freight = request.json['Freight']
    order.ShipName = request.json['ShipName']
    order.ShipAddress = request.json['ShipAddress']
    order.ShipCity = request.json['ShipCity']
    order.ShipRegion = request.json['ShipRegion']
    order.ShipPostalCode = request.json['ShipPostalCode']
    order.ShipCountry = request.json['ShipCountry']

    db.session.commit()
    return "Order Details Updated Successfuly!"



###### Order history of the given customer
@app.route('/orderhistory/<id>', methods=['GET'])
def get_order_history(id):
    results = db.session.query(Orders).filter(Orders.CustomerID == id).all()
    if results == None:
        return "Cannot find the order history of the customer!"
    ord_his = []
    for result in results:
        result = result.__dict__
        del result['_sa_instance_state']
        ord_his.append(result)
    return flask.jsonify(ord_his)


if __name__ == "__main__":
    app.run(debug=True, port=5000)














