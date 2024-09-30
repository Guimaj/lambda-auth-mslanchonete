import jwt
import os
from jwt import InvalidTokenError, ExpiredSignatureError

def get_secret(secret_name):
    return os.environ.get(secret_name)

def lambda_handler(event, context):

    secret = get_secret("jwtsecret")

    response = {
            "isAuthorized": False
        }
  
    try:
        # Recuperando o token JWT do evento
        headers = event.get("headers")
        token = headers.get("authorization", headers.get("Authorization"))

        if not token:
            print('denied: missing auth token')
            return response

    
        decoded_token = jwt.decode(token[7:], secret, algorithms=["HS256"])
        response = {
            "isAuthorized": True
        }
        print('allowed')
        return response
    except BaseException:
        print('denied')
        return response