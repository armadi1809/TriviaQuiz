import requests  


url = 'https://opentdb.com/api.php'
parameters = {'amount': 10, 'type': 'boolean'}
def get_data():     
    response = requests.get(url, params=parameters) 
    return response.json()['results'] 