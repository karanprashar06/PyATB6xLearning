import pytest
import allure
import requests

@pytest.mark.positive
@allure.title("TC#1 - Verify the get request.valid")
@allure.description("Verify that the GET request works and give a 200 status code.")
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url=url)
    assert response_data.status_code ==200

@pytest.mark.negative
@allure.title("TC#2 - Verify the get request.invalid")
@allure.description("Verify that the GET request works and give a 400 status code.")
def test_get_request_invalid():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url=url)
    assert response_data.status_code == 404
    print("KARAN PRASHAR")