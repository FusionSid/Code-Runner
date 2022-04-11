import asyncio

from runner import run_code


async def main():
    # Example of how to use with file
    with open("example.rickroll") as file:
        code = file.read()

    output = await run_code(code, "rickroll-lang")
    
    print(f"Output:\n", output)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
