
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
    "add_to_cart.feature",
    'AddToCart -> Add Product to cart',
)
def test_add_to_cart_case():
    """
        Add to cart case
    """
    pass

# Scenario 2
@scenario(
    "add_to_cart.feature",
    "UpdateCart -> Update Product Quantity",
)
def test_update_cart_quantity():
    """
        Update cart quantity
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
        "username": "testing",
        "password": "testpassword",
        "email": "texttesting@xyz.com"
    }
    res = session.post(
        url="http://localhost/register",
        data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )

    # setting userid for further use
    context["user_id"] = res.json().get("id")


@given('he login to website')
def user_login_to_account(context):
    """
        user login to website
    """
    session.auth = ("testing", "testpassword")
    session.get(url="http://localhost/login")


@given('get user addresses')
def user_get_his_addresses(context):
    """
        user going to retrive his addresses
        Asserts
            :assert: check api status
    """
    res = session.get(url="http://localhost/addresses")
    assert res.status_code == 200


@given(parsers.parse('user add the product to cart with quantity:{quantity}'))
def user_add_product_to_cart(context, quantity):
    """
        user add's product to his cart
    """
    res = session.post(
        url="http://localhost/cart",
        data=json.dumps({"id": 1, "quantity": quantity}),
        headers={'Content-Type': 'application/json'}
    )


@then(parsers.parse('verify its cart with quantity:{quantity}'))
def user_check_his_cart(context, quantity):
    """
        user verify its cart quantity
        Asserts:
            :assert: check api status
            :assert: check quantity
    """
    res = session.get(url="http://localhost/cart")
    assert res.status_code == 200
    assert int(res.json()[0].get('quantity', 0))



# Scenario 2 start

@given('get his cart detail')
def user_get_cart_detail(context):
    """
        user verify its cart quantity
        Asserts:
            :assert: check api status
            :assert: check quantity
    """
    res = session.get(url="http://localhost/cart")
    assert res.status_code == 200
    assert res.json()[0].get('quantity', 0)


@when(parsers.parse('he is updating the cart quantity:{quantity}'))
def user_update_cart_product(context, quantity):
    """
        user update his cart products
    """
    res = session.post(
        url="http://localhost/cart",
        data=json.dumps({"id": 1, "quantity": quantity}),
        headers={'Content-Type': 'application/json'}
    )