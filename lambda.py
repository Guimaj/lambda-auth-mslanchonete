import boto3
import jwt
from jwt import InvalidTokenError, ExpiredSignatureError
from botocore.exceptions import ClientError

def get_secret(secret_name):
    client = boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return secret
    except ClientError as e:
        raise Exception(f"Erro ao recuperar secret: {e}")

def lambda_handler(event, context):

    secret = get_secret("jwt-secret")
  
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