import requests

from flask import Flask, request, Response
from db import SQLiteDB
from stub_request import StubRequest

app = Flask(__name__)
db = SQLiteDB()
# The assumption is that this is from within the VPC
# To unify business logic, i would probabably do all result formatting in the app server monolith
# That is unless all of the initialization of the new model happened in this API server, 
# which I would be cautious about due to the two implementations diverging over time. 
INTERNAL_API_URL = 'http://0.0.0.0:3000/internal-api/email-model'

@app.route('/ping', methods=['GET'])
def heart_beat():
    return Response('pong', status=200)


@app.route('/api/email', methods=['GET'])
def proxy():
    print('Get api/email')
    
    # Check for the API key in the request headers
    api_key = request.headers.get('Authorization')
    
    db_key = db.query(query_str=f" SELECT * FROM 'valid_tokens' WHERE token = '{api_key}' ").fetchone()

    if db_key == None:
        return Response('Unauthorized', status=401)


    # Forward the request to the internal API
    try:
        # Forward the request with headers, if any
        resp =  StubRequest (
            method='GET', 
            url=INTERNAL_API_URL,
            data=request.get_data())

        # Return the response from the internal API
        return Response(resp.content, status=resp.status_code)
        
    except requests.RequestException as e:
        return Response(f'Error: {str(e)}', status=500)
    
    
if __name__ == '__main__':
    db.init_app(db_name="api_keys.db")
    app.run(host='0.0.0.0', port=5000)