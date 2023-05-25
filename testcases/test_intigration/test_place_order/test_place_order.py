"""Add driver orders to the trip if the trip is in started state"""

import base64
import json
import pytest
from pytest_bdd import scenario, when, parsers, then, given
import requests

# We are managing session so our login key
# get stored in out cache
session = requests.Session()

# Scenario 1
@scenario(
    "place_order.feature",
    "PlaceOrder -> User Places the order",
)
def test_place_order():
    """
        Add to cart case
    """
    pass


@pytest.fixture(scope="function")
def context():
    """
        Fixture to manage data sharing
    """
    return {}


@given('A customer open the website')
def check_website_is_working(context):
    """
        To cehck website is woking 
        Asserts
            :assert: check api status
    """
    res = session.get(url="http://localhost")
    assert res.status_code == 200


@given('he register his account')
def user_register_the_account(context):
    """
        And then user register his account
    """
    payload = {
        "username": "testing1",
        "password": "testpassword1",
        "email": "texttesting@xyz.com"
    }
    res = session.post(
        url="http://localhost/register",
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    context["user_id"] = res.json().get("id")


@given('he login to website')
def user_login_to_account(context):
    """
        user login to website
    """
    session.auth = ("testing1", "testpassword1")
    res = session.get(url="http://localhost/login")
    print(res.status_code)


@given(parsers.parse('user add the product to cart with quantity:{quantity}'))
def user_add_product_to_cart(context, quantity):
    """
        user going to retrive his addresses
        Asserts
            :assert: check api status
    """
    res = session.post(
        url="http://localhost/cart",
        data=json.dumps({"id": 1, "quantity": quantity}),
        headers={'Content-Type': 'application/json'}
    )


@when(parsers.parse('he verify its cart with quantity:{quantity}'))
def user_check_his_cart(context, quantity):
    """
        user add's product to his cart
    """
    res = session.get(url="http://localhost/cart")
    assert res.status_code == 200
    assert int(res.json()[0].get('quantity', 0))


@then('he adds his address')
def user_added_his_address(context):
    """
        user adds the product
    """
    res = session.post(
        url="http://localhost/addresses",
        data=json.dumps({
            "street": "test",
            "number": "test",
            "country": "test",
            "city": "test",
            "postcode": "test"
        }),
        headers={'Content-Type': 'application/json'}
    )


@then('he adds the payment card')
def user_added_his_card(context):
    """
        user adds his payment card
    """
    res = session.post(
        url="http://localhost/cards",
        data=json.dumps({
            "longNum":"2222222222222222",
            "expires": "12/25",
            "cvv": "123"
        }),
        headers={'Content-Type': 'application/json'}
    )
    print(res.json())
    context['card_id'] = res.json()['id']

    
@then('he check the card detail')
def user_get_his_card(context):
    """
        user verify its card
        Asserts:
            :assert: check api status
            :assert: check response
    """
    res = session.get(
        url=f"http://localhost/cards/{context['card_id']}",
    )
    assert res.status_code == 200
    assert res.json()
    

@when('he is done, he places the order')
def user_place_the_order(context):
    """
        user place the order
    """
    res = session.post(
        url="http://localhost/orders",
        data=json.dumps({}),
        headers={'Content-Type': 'application/json'}
    )
    print(res.json())

@then('he verify the order details')
def user_vrify_hit_order(context):
    """
        user verify his orders
        Asserts:
            :assert: check api status
            :assert: check response
    """
    res = session.get(
        url="http://localhost/orders",
    )
    assert res.status_code == 201
    assert res.json()