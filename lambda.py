import jwt
import os
from jwt import InvalidTokenError, ExpiredSignatureError

def get_secret(secret_name):
    return os.environ.get(secret_name)

def lambda_handler(event, context):

    secret = get_secret("jwtsecret")
  
    # Recuperando o token JWT do evento (por exemplo, do corpo da requisição ou dos headers)
    token = event.get('jwt')

    if not token:
        return {
            'statusCode': 401
        }

    try:
        decoded_token = jwt.decode(token, secret, algorithms=["HS256"])

        # Se a verificação for bem-sucedida, o token é válido
        return {
            'statusCode': 200
        }

    except ExpiredSignatureError:
        # O token expirou
        return {
            'statusCode': 401
        }

    except InvalidTokenError as e:
        # Token inválido
        return {
            'statusCode': 401
        }
