import requests

data = {
    "code" : 'take me to ur heart\n    together forever and never to part\n    i just wanna tell u how im feeling "hello world"\n    saygoodbye\nsay goodbye\n'
}

r = requests.post("http://127.0.0.1:8000/run", json=data)
print(r.json())