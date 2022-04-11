import os
import random
import string
import asyncio
from subprocess import run, DEVNULL
from typing import Literal, get_args


LANGUAGES = Literal["python", "rickroll-lang", "node"]


async def cleanup(random_code):
    await asyncio.sleep(5)
    
    image = run(["docker", "images", "-q", random_code], capture_output=True).stdout.decode()
    container = run(["docker", "ps", "-a", "-q", "--filter", f"ancestor={image}"], capture_output=True).stdout.decode()
    
    os.system(f"docker container kill {container} >/dev/null 2>&1") # just makes it try to not print the output to terminal
    os.system(f"docker container rm -f {container} >/dev/null 2>&1")
    os.system(f"docker image rm -f {image} >/dev/null 2>&1")


async def run_code(code, language: LANGUAGES, *args, **kwargs):
    
    if language not in list(get_args(LANGUAGES)):
        return f"Not a valid lanuage\nList: {', '.join(list(get_args(LANGUAGES)))}"
    
    random_code_list = string.ascii_lowercase + string.digits
    random_code = "".join([random.choice(random_code_list) for i in range(12)])

    code = repr(code).strip("'") # idk why this works but it does

    run(["docker", "build", "-t", random_code, f"./{language}/", "--build-arg", f"CODE={code}"], stdout=DEVNULL, stderr=DEVNULL)
    output = run(["timeout", "-s", "KILL", "3", "docker", "run", "--rm", "--read-only", random_code], capture_output=True).stdout.decode()

    if len(output) > 4000:
        output = output[:4000]

    if kwargs["await_task"]: # if you are in an async event loop that wont be killed before this is done eg: discord bot, fastapi
        loop = asyncio.get_event_loop()
        loop.create_task(cleanup(random_code))
    else:
        await cleanup(random_code)

    return output


async def main():
    # Example of how to use with file
    with open("example.rickroll") as file:
        code = file.read()

    output = await run_code(code, "rickroll-lang")
    
    print(f"Output:\n", output)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
