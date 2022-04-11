# Code-Runner

Runs code safely (i think) in a docker container

## Supported Languages:
    - python
    - rickroll-lang
    - node

This project is mainly just for me to test docker but it works so thats good
I will use the code from here in the rickroll-lang server bot

**I have added an example of how to use this with:**

    - a discord bot
    - a fastapi API
    - a normal file with the code

## Contributing:

If you have a docker file for a certain language make a fork of this repo

Then create a new folder with the language name in the `src` folder. 

Here is a template for that: 
```
FROM image

ARG CODE # this is the code provided

RUN echo -e ${CODE} > code.file_ext # write the code to a file

CMD ["timeout", "-s", "KILL", "5", code to run file ,"code.file_ext"]
```

btw this is like my first time using docker so if im doing something wrong let me know
