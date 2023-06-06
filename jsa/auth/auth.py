from kiota_abstractions.authentication.access_token_provider import (
    AccessTokenProvider,
)
from kiota_abstractions.authentication.allowed_hosts_validator import AllowedHostsValidator
import os
import requests

class JSAAccessTokenProvider(AccessTokenProvider):
    def __init__(self):
        self.offline_token = os.environ['OFFLINE_TOKEN']
        self.allowed_hosts_validator = AllowedHostsValidator(["sso.redhat.com", "api.openshift.com"])
        self.client_id = "cloud-services"
        self.url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

    async def get_authorization_token(self, uri: str) -> str:
        return self.new_token()

    def get_allowed_hosts_validator(self) -> AllowedHostsValidator:
        return self.allowed_hosts_validator
    
    def new_token(self) -> str:
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": self.offline_token
        }

        print(data)

        response = requests.post(self.url, data=data)

        print(f"RESPONSE :: \n {response}")

        code = response.status_code
        if code == 200:
            body = response.json()
            try:
                token = body["access_token"]
            except Exception as e:
                raise RuntimeError("Error issuing a new token, received answer with body " + str(body)) from e
        else:
            raise RuntimeError("Error issuing a new token, received answer code " + str(code))

        return token

