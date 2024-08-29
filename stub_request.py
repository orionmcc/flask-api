import json

def StubRequest(method, url, data):
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

        def json(self):
            return self.json_data
        
        
    temp_resp_data = {
        'itemCount': 3,
        'itemMatches':[
            {
                'itemDescription': "3 inch widget",
                'matches': [
                    "match_1",
                    "match_2",
                    "match_3",
                ]
            },
            {
                'itemDescription': "4 inch sprocket",
                'matches': [
                    "match_1",
                    "match_2",
                ]
            },
            {
                'itemDescription': "pip joint",
                'matches': [
                    "match_1",
                    "match_2",
                    "match_3",
                    "match_4",
                    "match_5",
                ]
            }
        ]
    }
    return MockResponse(json.dumps(temp_resp_data), 200)