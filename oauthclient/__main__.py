import base64
import json
import requests
import os

API_HOST = 'http://localhost:8090'
OAUTH_TOKEN_ENDPOINT = '/oauth/token/'
API_ENDPOINT = '/testkyle/groups/'
# Development instance ID. Change to match your environment
CLIENT_ID = '2R6TunDgVi6wmKzRtcGzOYNTRKmyYr8eNXPMu17Q'
# Development instance secret. Change to match your environment
CLIENT_SECRET = 'aiCzrBL9BX7JQXDluKmX6TAUpU6uiHBITCXGmywfHVWjJ9bGHORXIE611SKuK7bMhOQbfJhKnzg61fMQKCiICVTAE29aWjtSKmEgJp2VJCamAdKfIpmpdTwbn4UfOZ6k'

def main():
    #client_id = input('Enter the client ID: ')
    #client_secret = input('Enter the client secret: ')
    r = requests.get(API_HOST)
    csrf_token = r.cookies['csrftoken']
    params = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'csrfmiddlewaretoken': csrf_token,
        'grant_type': 'client_credentials',
    }
    token_response = requests.post(API_HOST + OAUTH_TOKEN_ENDPOINT,
                                   params=params)
    token_json = token_response.json()
    access_token = token_json['access_token']
    print(f'Access token: {access_token}')
    params = {
        'csrfmiddlewaretoken': csrf_token,
        'org_id': '2',
    }
    headers = {
        'content-type':'application/json',
        'Authorization': f'Bearer {access_token}',
    }
    r = requests.get(API_HOST + API_ENDPOINT,
                     headers=headers,
                     data=json.dumps(params))
    print(r.status_code)
    print(r.json())

if __name__ == '__main__':
    main()
