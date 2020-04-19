import http.client
import json
from urllib.parse import urlparse
import requests


def request(
    method: str,
    url: str,
    token: str
    ):
    """
    Constructs and send a request
    :param method: method for the request: 'POST' and 'GET'
    :param url: URL for the request, include params
    :param data: (optional) Dictionary to send in the body
    :param token: (optional) Authorization token for protected endpoints
    :param error_message: (optional) Custom error message

    :return: Dictionary with the response data
    """
    res = None

    # parse url
    parsed_url = urlparse(url)
    base_url = parsed_url.netloc
    path = '{}'.format(parsed_url.path)

    if parsed_url.query:
        path = '{}?{}'.format(path, parsed_url.query)

    # connection
    conn = http.client.HTTPSConnection(base_url)
    headers = {
        'content-type': 'application/json',
    }

    # add token if exists
    if token:
        headers['Authorization'] = 'JWT {}'.format(token)

    # required request data
    kwargs = {}  # type: Dict[str, Any]

    # put body
    """if data:
        kwargs['body'] = json.dumps(data)"""

    # make request
    error_message = 'Nada'
    try:
        # request
        conn.request(method, path, headers=headers, **kwargs)

        # manage response
        res = conn.getresponse()

        response_data = json.loads(res.read().decode())
        print(response_data)
    except Exception:
        if error_message is None:
            error_message = f'Url may be wrong. url: {url}'
            if res:
                error_message += f' HTTP status: {res.code}'

        raise ValueError(error_message)
    
    
    return response_data



request('GET', "https://dogs.magnet.cl", "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNDEsInVzZXJuYW1lIjoiamFyYjI5QGdtYWlsLmNvbSIsImV4cCI6MTU4NzI5OTY0NSwiZW1haWwiOiJqYXJiMjlAZ21haWwuY29tIn0.MaqaTDxUTab3y5IlLHNRjn2jnjU8cKy1Fb63RrA5yPA")