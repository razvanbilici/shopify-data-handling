from flask import Flask, render_template
from logic import list_orders, fetch_orders, shipbob_request

app: Flask = Flask(__name__)

# ----

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# ----

# Should display orders with status=any    
@app.route("/order-list/", methods=['GET'])
def order_list():

    order_names: list[str] = list_orders()["order_names"]  
    order_count: int = list_orders()["count"] 

    return render_template("order-list.html", orders=order_names, count=order_count)

# ----

# Should diplay the names of the products contained in order #1028
@app.route("/order-1028/", methods=['GET'])
def order_1028():   

    _1028: dict = fetch_orders("#1028")
    products: list[str] = [product["name"] for product in _1028["line_items"]]

    return render_template("order-1028.html", products=products)     

# ----

# Mock POST request
# Needs proper header data, see logic.py
@app.route("/shipbob-mock/", methods=['GET'])
def mock_post():
    return shipbob_request()

if __name__ == "__main__":
    app.run(debug=True)