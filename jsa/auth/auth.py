from kiota_abstractions.authentication.access_token_provider import (
    AccessTokenProvider,
)
from kiota_abstractions.authentication.allowed_hosts_validator import AllowedHostsValidator
import os

class JSAAccessTokenProvider(AccessTokenProvider):
    def __init__(self):
        self.allowed_hosts_validator = AllowedHostsValidator(["sso.redhat.com", "api.openshift.com"])

    async def get_authorization_token(self, uri: str) -> str:
        return os.environ['OFFLINE_TOKEN']

    def get_allowed_hosts_validator(self) -> AllowedHostsValidator:
        return self.allowed_hosts_validator

