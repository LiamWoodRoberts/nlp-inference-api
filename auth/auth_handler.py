import os
import secrets
from base64 import b64decode

USERNAME = os.getenv("USERNAME", "testing")
PASSWORD = os.getenv("PASSWORD", "abc123")


def handler(event, context):
    print("Event:", event)
    token = get_token(event)
    username = get_current_user(token)
    policy = generate_policy(username, "Allow", event["methodArn"])
    return policy


def get_token(event):
    auth = event.get("authorizationToken")
    if auth is None:
        raise Exception("Unauthorized")
    else:
        _, token = auth.split()
        return token


def get_current_user(token):
    data = b64decode(token).decode("ascii")
    username, _, password = data.partition(":")
    correct_username = secrets.compare_digest(username, USERNAME)
    correct_password = secrets.compare_digest(password, PASSWORD)
    if not (correct_username and correct_password):
        raise Exception("Unauthorized")
    return username


def generate_policy(principal_id, effect, resource, scopes=None):
    policy = {
        "principalId": principal_id,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": "/".join(resource.split("/")[:-1]) + "/*",
                }
            ],
        },
    }
    if scopes:
        policy["context"] = {"scopes": scopes}
    return policy
