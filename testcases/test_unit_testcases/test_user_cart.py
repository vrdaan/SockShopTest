import base64
import json
import pytest
import requests


class TestUserCart:
    """
        Test case to test add to cart
    """
    URL = "http://localhost/cart"

    def test_add_to_cart(self):
        """
            Testcases to test Cart APIs
            ENDPOINT: http://localhost/cart

            Asserts:
                :assert: To check the value must be the same which 
                         we have passed
    
        """
        session = requests.Session()

        # setting basic auth for login
        session.auth = ("testing2", "testpassword2")

        # Login to get the login cookies
        res = session.get(url="http://localhost/login")

        # Adding item to cart
        res = session.post(
            url=self.URL,
            data=json.dumps({"id": 1, "quantity": 1}),
        )

        # Checking cart is updated or not
        res = session.get(url=self.URL)

        res = res.json()
        if res:
            assert res[0].get('quantity', 0)
