import pytest
import allure
import requests



@pytest.mark.crud
@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("VErify thr create Booking!")
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"

    }

    response_data = requests.post(url=url, headers=headers, json=payload)
    print(response_data.text)
    assert response_data.status_code == 200