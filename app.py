from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')

def whatismyip():
    return {'client_ip': request.remote_addr, 'server_ip':request.headers.get('Host').split(':')[0]}