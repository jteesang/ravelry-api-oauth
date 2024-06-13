import base64
import requests

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from requests_oauthlib import OAuth2Session

app = FastAPI()

client_id ="" # Create app at https://www.ravelry.com/pro/developer
client_secret ="" # Create app at https://www.ravelry.com/pro/developer
auth_url = "https://www.ravelry.com/oauth2/auth"
token_url = "https://www.ravelry.com/oauth2/token"
redirect_url = "https://localhost:8432/callback" # Add your redirect uri from https://www.ravelry.com/pro/developer

@app.get('/')
def main():
    return {"message":"fastapi https example"}

@app.get('/login')
def login():
    global client_id, auth_url, redirect_url
    ravelry = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)
    authorization_url, state = ravelry.authorization_url(auth_url)
    return RedirectResponse(authorization_url)

@app.get('/callback')
def callback(req: Request):
    global client_id
    global client_secret
    cred = f"{client_id}:{client_secret}"
    cred_b64 = base64.b64encode(cred.encode()).decode()
    data= {
        "code":req.query_params.get('code'),
        "redirect_uri": "https://localhost:8432/callback",
        "grant_type": "authorization_code"
    }
    headers = {
        "Authorization": f"Basic {cred_b64}"
    }
    response = requests.post(token_url,data=data, headers=headers)

    if "access_token" in response.json():
        print(f"server resp: {response.json()}")
        access_token = response.json()["access_token"]
        redirect_url = "https://localhost:8432"
    return RedirectResponse(redirect_url)