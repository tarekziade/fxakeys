# uses https://github.com/mozilla/PyFxA/tree/rfk/assertion-and-oauth-helpers
import os
from fxa.oauth import Client as OAuthClient
from fxa.core import Client


EMAIL = os.environ.get('FXA_USER', "tarek@mozilla.com")
PASSWORD = os.environ.get('FXA_PASSWORD')
CLIENT_ID = "021fd64aa9661fa1"
AUTH_SERVER = "https://stable.dev.lcip.org/auth"
OAUTH_SERVER = "https://oauth-stable.dev.lcip.org"
KB = b'a' * 32


def get_oauth_token(client_id=CLIENT_ID, oauth_server=OAUTH_SERVER,
                    auth_server=AUTH_SERVER, email=EMAIL, password=PASSWORD):

    if password is None:
        raise Exception('You must set FXA_PASSWORD')

    print('Getting an oauth token from FxA')
    oauth_client = OAuthClient(client_id, server_url=oauth_server)
    session = Client(server_url=auth_server).login(email, password=password)
    assertion = session.get_identity_assertion(oauth_server)

    return oauth_client.authorize_token(assertion, scope="profile")


def verify_oauth_token(token, scope='profile', oauth_server=OAUTH_SERVER,
                       client_id=CLIENT_ID):
    oauth_client = OAuthClient(client_id, server_url=oauth_server)
    return oauth_client.verify_token(token, scope=scope)
