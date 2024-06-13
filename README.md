# ravelry-api-oauth
Python example of OAuth 2.0 with Ravelry API

## Overview
This repository provides an example for authenticating with Ravelry via OAuth 2.0 using the [OAuth2Session](https://requests-oauthlib.readthedocs.io/en/latest/index.html) library by utilizing FastAPI and a HTTPS server running with uvicorn.

## Run Locally
1. Create your own Ravelry API at `https://www.ravelry.com/pro/developer`
    - Get the client id, client secret, and redirect url
2. Create your own pem files using `mkcert`
    - `mkcert localhost 127.0.0.1 ::1`
    - rename the files to `cert.pem` and `key.pem`
3. Create and start the venv: `python3 -m venv venv && source venv/bin/activate`
4. Get the dependencies: `pip3 install -r requirements.txt`    
5. Run the HTTPS server with `python3 server.py`
6. Navigate to `https://localhost:8432/login`, authenticate, and see your page redirect to the root page

## References
- Ravelry API: https://www.ravelry.com/api
- OAuth2Session: https://requests-oauthlib.readthedocs.io/en/latest/index.html
- FastAPI: https://fastapi.tiangolo.com/
- Uvicorn: https://www.uvicorn.org/
