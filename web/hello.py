def app(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    body = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]

    return body