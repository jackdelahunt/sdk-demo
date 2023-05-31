import pytest
from jsa.client.service_account_client import ServiceAccountClient
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

def test_basic():
    assert 10 == 9 + 1

@pytest.mark.asyncio
async def test_service_account_list():
    auth_provider = AnonymousAuthenticationProvider()
    # Create request adapter using the HTTPX-based implementation
    request_adapter = HttpxRequestAdapter(auth_provider)
    # Create the API client
    client = ServiceAccountClient(request_adapter)

    service_accounts = await client.apis.service_accounts.v1.get()
    print(service_accounts)

    assert True
