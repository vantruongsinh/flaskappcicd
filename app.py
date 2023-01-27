from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def whatismyip():
    try:
        return {'client_ip': request.remote_addr, 'server_ip':request.headers.get('Host').split(':')[0], 'proxy':request.headers.get('Forwarded')}
    except Exception as e:
        return {'Error':str(e)}