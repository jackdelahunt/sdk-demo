from kiota_abstractions.authentication.access_token_provider import (
    AccessTokenProvider,
)
from kiota_abstractions.authentication.allowed_hosts_validator import AllowedHostsValidator
import os
import requests
from keycloak import KeycloakOpenID

DEFAULT_AUTH_URL  = "https://sso.redhat.com/auth/"
DEFAULT_CLIENT_ID = "cloud-services"
REALM_NAME = "redhat-external"

class JSAAccessTokenProvider(AccessTokenProvider):
    def __init__(self):
        self.offline_token = os.environ['OFFLINE_TOKEN']
        self.allowed_hosts_validator = AllowedHostsValidator(["sso.redhat.com", "api.openshift.com"])

    async def get_authorization_token(self, uri: str) -> str:
        return self.new_token()

    def get_allowed_hosts_validator(self) -> AllowedHostsValidator:
        return self.allowed_hosts_validator
    
    def new_token(self) -> str:
        # Configure keycloak_openid client 
        keycloak_openid = KeycloakOpenID(server_url=DEFAULT_AUTH_URL,
            client_id=DEFAULT_CLIENT_ID,
            realm_name=REALM_NAME)
        
        # Refresh token
        token = keycloak_openid.refresh_token(self.offline_token)
        # print(f"REFRESH TOKEN :: {token}")
        return token["access_token"]