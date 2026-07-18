import requests
import os 
from dotenv import load_dotenv

load_dotenv()  

username = os.environ.get('PA_USERNAME')
token = os.environ.get('PA_TOKEN')


if not username or not token:
    print('Brak username lub token w zmiennych środowiskowych!')
else:
    response = requests.get(
        'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
            username=username
        ),
        headers={'Authorization': 'Token {token}'.format(token=token)}
    )
    if response.status_code == 200:
        print('CPU quota info:')
        print(response.content)
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
