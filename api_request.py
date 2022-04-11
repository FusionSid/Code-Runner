# i havent actualy hosted this api anywhere yet but if I do heres how to make a request to it

import requests

api_link = "http://127.0.0.1:8000"

data = {
    "code" : 'take me to ur heart\n    i just wanna tell u how im feeling "I am cool"\nsay goodbye',
    "language" : "rickroll-lang"
}
response = requests.post(f"{api_link}/api/run", json=data).json()
print(response["output"])