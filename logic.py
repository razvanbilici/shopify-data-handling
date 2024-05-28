from config import URL, API_VERSION, TOKEN
import requests
import sys

# So it doesn't crash the program when printing json to the console =)
sys.stdout.reconfigure(encoding='utf-8')

# Fetch the number of orders which have the status=any
# Returns the fetched orders or a single order if its name is specified via the function's arg
def fetch_orders(order_name: str=None) -> list:

    try:
        request_header: dict = {
            "X-Shopify-Access-Token": TOKEN,
            "Content-Type": "application/json"
        }

        orders_endpoint: str = f"{URL}/admin/api/{API_VERSION}/orders.json?status=any"

        response = requests.get(orders_endpoint, headers=request_header)

        # Success status code
        if response.status_code == 200:
            
            orders: dict = response.json()["orders"]

            if order_name is not None:
                for order in orders:
                    if order["name"] == order_name:
                        return order
                    
            return orders
        else:   
            print(f"Failed to fetch data - Status error: \n{response.json()}")
            return {}
    
    except Exception as e:
        print(f"Encountered error: \n{e.__class__.__name__}")
        return {}

# ----

# List the orders' names and the total amount
def list_orders() -> dict:
    
    orders: dict = fetch_orders()

    if len(orders) == 0:
        return {"order_names" : [], 
                "count" : 0}
    
    order_names: list[str] = [order["name"] for order in orders]
  
    return {"order_names" : order_names,
            "count" : len(order_names)}

# ----

def shipbob_request():
    
    order_1028: dict = fetch_orders("#1028")

    # Mock data
    shipbob_url: str = "mock"
    shipbob_channel_id: int = -1

    shipbob_header = {
    "Content-Type": "application/json",
    "shipbob_channel_id": str(shipbob_channel_id)
    }  

    # Required: recipient, products
    shipbob_payload: dict = {
    "recipient": {
        "name": order_1028["billing_address"]["name"],
        "address": {
        "address1": order_1028["billing_address"]["address1"],
        "address2": order_1028["billing_address"]["address2"],
        "company_name": order_1028["billing_address"]["company"],
        "city": order_1028["billing_address"]["city"],
        "state": order_1028["billing_address"]["province"],
        "country": order_1028["billing_address"]["country"],
        "zip_code": order_1028["billing_address"]["zip"],
        },
        "email": None,
        "phone_number": order_1028["billing_address"]["phone"],
        },

    "products": [
        {
            "reference_id": item["id"],
            "product_name": item["name"],
            "quantity": item["quantity"]
        } for item in order_1028["line_items"]
    ]
    }

    # response = requests.post(shipbob_url, headers=shipbob_header, data=shipbob_payload)

    return f"Mock Url: {shipbob_url} \n{shipbob_header} \nPOST \n{shipbob_payload}"


# Saved order and billing info keys in .txt files
# if __name__ == "__main__":
    
#     order: dict = fetch_orders("#1001")
    
#     with open("order_structure.txt", "a") as file:
#         for key in order:
#             file.write(f"{key}\n")

#     with open("billing_structure.txt", "a") as file:
#             for key in order["billing_address"]:
#                 file.write(f"{key}\n")

#     with open("product_structure.txt", "a") as file:
#             for key in order["line_items"][0]:
#                 file.write(f"{key}\n")

# print(shipbob_request())
