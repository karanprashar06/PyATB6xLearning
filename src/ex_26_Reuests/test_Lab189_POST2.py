import pytest
import allure
import requests


@pytest.mark.crud
@allure.title("Test Post 2")
@allure.description("Test Post 2")
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "firstname": "karan",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response.text)
    assert response.status_code == 200

def test_read_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {
        "Content-Type": "application/json",
    }


    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    print(response.text)
    assert response.status_code == 200