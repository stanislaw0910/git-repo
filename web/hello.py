def app(env, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body =''
    a = env[Query_String]
    a = a.split('&')
    for i in range(len(a)):
        body = a[i].encode('utf-8') +'\n'
    return body