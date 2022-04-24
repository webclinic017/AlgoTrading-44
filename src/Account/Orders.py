import requests

def place_equity_order(client, order):
    """
    Sends Equity Order to Tradier Brokerage

    Input:
    1. Ticker Symbol
    2. Side: Buy or Sell
    3. Quantity: 100 shares
    4. Type: Market or Limit
    5. Duration: Day, Good till Cancelled, Pre, Post
    6. Price: Market or Limit Price
    """

    response = requests.post(
        
        'https://' + client.endpint + '/v1/accounts/' + order.accountid + '/orders',

        data = {
            'class': 'equity', 
            'symbol': order.ticker, 
            'side': order.side, 
            'quantity': order.quantity, 
            'type': order.type, 
            'duration': order.duration, 
            'price': order.price, 
            },

        headers={'Authorization': 'Bearer ' + client.api_key, 'Accept': 'application/json'})

    json_response = response.json()

    return json_response