# Setup guide
## Software requirements
- Python v3.9.13
- Flask module
  - pip install flask
- Native OS: Windows 10 (not sure about potential portability issues, e.g. Linux Distros)

 ## Startup
- Add config.py file; It should include the store's URL (URL), API version (API_VERSION) and access token (TOKEN)
  - config.py sample:
      - URL: str = "https://your-shopify-url-here.com/"
      - API_VERSION: str = "2023-03"
      - TOKEN: str = "mock-token39432"
- run app.py:
   -  python app.py
- I've used Bootstrap for a bit of styling, but there's no need for local installation as it's been imported in the base html template via CDNs

## Tasks
- [x] Fetch the number of orders which have the status=any and list the number of orders
- [x] Fetch data for order #1028 and print the product names contained within the order (line_items contains products for the order).
- [ ] Using data from order #1028, create a mocked Shipbob API request using their documentation for “Create Order”
  - https://developer.shipbob.com/api-docs/#tag/Orders/paths/~11.0~1order/post
  - [X] Only fill the required data in the JSON.
 
