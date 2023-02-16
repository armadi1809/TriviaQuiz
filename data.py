import requests  


url = 'https://opentdb.com/api.php?amount=10&type=boolean'




def get_data():     
    response = requests.get(url) 
    return response.json()['results'] 