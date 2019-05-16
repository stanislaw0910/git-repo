def app(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    body = [bytes('\n'.join(env['QUERY_STRING'].split('&')),
                  encoding="utf8")]

    return body
