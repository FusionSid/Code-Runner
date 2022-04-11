FROM python:3.8-alpine

ARG CODE

RUN echo -e ${CODE} > code.py

CMD ["timeout", "-s", "KILL", "5", "python3", "code.py"]