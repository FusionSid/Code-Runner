import requests

url = ""

data = {
    "code" : 'take me to ur heart\n    together forever and never to part\n    i just wanna tell u how im feeling "hello world"\n    saygoodbye\nsay goodbye\n'
}

r = requests.post(f"{url}/run", json=data)
print(r.json())