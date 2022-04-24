import requests

def get_quote(client):

    response = requests.get(

        'https://' + client.endpoint + '/v1/markets/quotes',

        params = {
            'symbols': client.ticker
            },

        headers = {
            'Authorization': 'Bearer ' + client.api_key,
            'Accept': 'application/json'
         }
    )

    json_response = response.json()

    return json_response