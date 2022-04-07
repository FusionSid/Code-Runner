import os
import shutil
import string
import random
import asyncio
from subprocess import run
from distutils.dir_util import copy_tree

from fastapi import APIRouter
from pydantic import BaseModel

async def cleanup(random_code):
    shutil.rmtree(f"./files/{random_code}")
    
    await asyncio.sleep(10)
    
    image = run(["docker", "images", "-q", random_code], capture_output=True).stdout.decode()
    os.system(f"docker image rm -f {image}")
    print("IMAGE:", image)

    container = run(["docker", "ps", "-a", "-q", "--filter", f"ancestor={image}"], capture_output=True).stdout.decode()
    print("CONTAINER:", container)

    os.system(f"docker container kill {container}")


async def run_code(code):
    random_code_list = string.ascii_lowercase + string.digits
    random_code = "".join([random.choice(random_code_list) for i in range(12)])

    os.mkdir(f"./files/{random_code}")

    with open(f"./files/{random_code}/main.rickroll", "w") as f:
        f.write(code)

    with open(f"./files/{random_code}/Dockerfile", "w") as f:
        f.write(
"""

FROM ricklang

COPY main.rickroll .

CMD ["python3", "RickRoll.py", "main.rickroll"]

"""
        )

    copy_tree(f"{os.getcwd()}/files/src-py/", f"{os.getcwd()}/files/{random_code}/src-py/")

    build = run(["docker", "build", "-t", random_code, f"./files/{random_code}"])
    output = run(["timeout", "-s", "KILL", "3", "docker", "run", "--rm", "--read-only", random_code], capture_output=True).stdout.decode()
    if len(output) > 4000:
        output = output[:4000]

    loop = asyncio.get_event_loop()
    loop.create_task(cleanup(random_code))
    return output


class Code(BaseModel):
    code : str


runner_endpoint = APIRouter()


@runner_endpoint.post("/run")
async def run_ricklang(code : Code):
    output = await run_code(code.code)
    return {"output":output}
