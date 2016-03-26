from collections import namedtuple

AppCredentials = namedtuple('AppCredentials', 'key secret')
ClientCredentials = namedtuple('ClientCredentials', 'token secret')
TwitterRequest = namedtuple('TwitterRequest', 'method url params')
