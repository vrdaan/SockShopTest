import base64
import json
import pytest
import requests


class TestLoginTestCase:
    """
        Test case to test login
    """

    @pytest.mark.parametrize("success_case", [True, False])
    def test_user_login(self, success_case):
        """
            Testcases to test API
            ENDPOINT: http://localhost/login

            Asserts:
                assert: First case we test for the success case:
                assert: Second case we test for the negative case:
        """
        session = requests.Session()

        # Register user first
        payload = {
            "username": "testing2",
            "password": "testpassword2",
            "email": "texttesting@xyz.com"
        }
        if success_case:
            res = session.post(
                url="http://localhost/register",
                data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )

        if success_case:
            # setting basic auth for login
            session.auth = (payload["username"], payload["password"])

        # login
        res = session.get(url="http://localhost/login")
        if success_case:
            assert res.status_code == 200
        else:
            assert res.status_code == 401
