import plaid
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

configuration = plaid.Configuration(
        host=plaid.Environment.Sandbox,
        api_key={
            'clientId': "647a883b8635b6001be94638",
            'secret': "981ecbc50691492bf477cb3564e82c",
        })
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

###

exchange_request = ItemPublicTokenExchangeRequest(
    public_token=pt_response['public_token']
)
exchange_response = client.item_public_token_exchange(exchange_request)
access_token = exchange_response['access_token']

###

request = TransactionsSyncRequest(
    access_token=access_token,
)
response = client.transactions_sync(request)
transactions = response['added']

while (response['has_more']):
    request = TransactionsSyncRequest(
        access_token=access_token,
        cursor=response['next_cursor']
    )
    response = client.transactions_sync(request)
    transactions += response['added']