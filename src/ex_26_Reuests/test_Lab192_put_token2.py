import requests



base_url = "https://restful-booker.herokuapp.com"
headers = { "Content-Type": "application/json",}

def get_token():
    base_path = "/auth"
    full_url = base_url + base_path
    json_payload_auth = {
        "username": "admin",
        "password": "password123"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload_auth)
    print(response_data)
    assert response_data.status_code ==200
    response_json = response_data.json()
    token=response_json["token"]
    print(token)
    assert type(token) == str
    assert len(token) > 0
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url+base_path

    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.post(url=full_url, headers=headers, json=json_payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["bookingid"]
    print(booking_id)
    return booking_id

def test_put():
    token = get_token()
    booking_id = get_booking_id()
    base_path = "/booking/"+str(booking_id)
    full_url = base_url + base_path
    cookie=  "token="+token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Karan",
        "lastname": "Prashar",
        "totalprice": 670000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.put(url=full_url, headers=headers, json=json_payload)
    response_data_json= response_data.json()
    assert response_data.status_code == 200
    assert response_data_json["firstname"] == "Karan"





