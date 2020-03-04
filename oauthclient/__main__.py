import base64
import json
import requests
import os

API_HOST = 'http://ec2-18-222-116-160.us-east-2.compute.amazonaws.com'
OAUTH_TOKEN_ENDPOINT = '/oauth/token/'
API_ENDPOINT = '/api/v2_1/properties/'

def main():
    client_id = input('Enter the client ID: ')
    client_secret = input('Enter the client secret: ')
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    params = {
        'username': username,
        'password': password,
        'grant_type': 'password',
    }
    token_response = requests.post(API_HOST + OAUTH_TOKEN_ENDPOINT,
                                   params=params, auth=(client_id, client_secret))
    token_json = token_response.json()
    access_token = token_json['access_token']
    scope = token_json['scope']
    print(f'Access token: {access_token}')
    print(f'Scope: {scope}')

    params = {
        'org_id': '1',
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
