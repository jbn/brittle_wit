from collections import namedtuple

AppCredentials = namedtuple('AppCredentials', 'key secret')
ClientCredentials = namedtuple('ClientCredentials', 'user_id token secret')
TwitterRequest = namedtuple('TwitterRequest', 'method url family params')
