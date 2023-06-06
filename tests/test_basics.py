import pytest
from jsa.client.service_account_client import ServiceAccountClient
from jsa.auth.auth import JSAAccessTokenProvider


from kiota_abstractions.authentication.base_bearer_token_authentication_provider import (
    BaseBearerTokenAuthenticationProvider)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

def test_basic():
    assert 10 == 9 + 1

# @pytest.mark.asyncio
# async def test_offline_token():
#     accessTokenProvider = JSAAccessTokenProvider()
#     token = await accessTokenProvider.get_authorization_token("...")
#     assert len(token) > 0

@pytest.mark.asyncio
async def test_service_account_list():
    accessTokenProvider = JSAAccessTokenProvider()
    auth_provider = BaseBearerTokenAuthenticationProvider(accessTokenProvider)
    request_adapter = HttpxRequestAdapter(auth_provider)
    client = ServiceAccountClient(request_adapter)

    service_accounts = await client.apis.service_accounts.v1.get()
    assert True
