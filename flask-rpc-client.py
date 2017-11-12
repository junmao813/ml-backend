from flask_jsonrpc.proxy import ServiceProxy
server = ServiceProxy('http://localhost:5123/api')
server.App.index()
print("res:", res)

# {'jsonrpc': '2.0', 'id': '91bce374-462f-11e2-af55-f0bf97588c3b', 'result': 'Welcome to Flask JSON-RPC'}
