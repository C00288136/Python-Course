import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token/"

class FlightSearch:
    def __init__(self):
        self._api_key = "F0meeAEm6rhbusofLGQ3Ay4W98H5ADmP"
        self._api_secret = "6cL8TZdQGLgjkWyV"
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=data)

        if response.status_code != 200:
            print(f"Failed to obtain token: {response.status_code}")
            print(f"Response: {response.json()}")
            return None

        response_json = response.json()
        print(f"Your token is {response_json['access_token']}")
        print(f"Your token expires in {response_json['expires_in']} seconds")
        return response_json['access_token']

# Example usage
if __name__ == "__main__":
    flight_search = FlightSearch()
