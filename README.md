## Overview

This Flask application contains the receipt processor API. This application has been built using **Python 3.8.12**.

## Setup Instructions

Pull down the source code from this Git repository:

```sh
$ git clone 
$ cd receipt-processor
```

### Run as a Docker container emulating production environment

If you have Docker and Docker Compose setup on your machine, on a terminal inside the project directory run:

```sh
$(receipt-processor) docker-compose up -d 
```

### Running the Flask Application on local machine for development

Create a new virtual environment:

```sh
$(receipt-processor) python3 -m venv venv
```

Activate the virtual environment:

```sh
$(receipt-processor) source venv/bin/activate
```

Install the python packages specified in requirements.txt:

```sh
(venv) $(receipt-processor) pip install -r requirements.txt
```

Run development server to serve the Flask application:

```sh
(venv) $(receipt-processor) python -m flask run -p 8000
```

### Examples

Once the application is running with either of the methods suggested above, you can send requests to the app.


Try the following to send a POST request to process a JSON receipt. This will return an id in response:
```sh
$ curl  -X POST \
  'http://127.0.0.1:8000/receipts/process' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}'
{"id": "8662998a-7ecd-c0c3-122d-b27be5dd08cf"}
```

Send a GET request to get the points for the above receipt `id`. This will return an id in response:
```sh
$ curl  -X GET \
  'http://127.0.0.1:8000/receipts/8662998a-7ecd-c0c3-122d-b27be5dd08cf/points' \
  --header 'Accept: */*'
{"points": 28}
```



## Testing

To run all the tests:

```sh
(venv) $(receipt-processor) python -m pytest -v
```

To check the code coverage of the tests:

```sh
(venv) $(receipt-processor) coverage run -m pytest
```

