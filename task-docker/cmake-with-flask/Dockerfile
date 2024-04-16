
FROM ubuntu:latest


RUN apt-get update && apt-get install -y git

COPY README.md /

COPY print_hello /bin/
RUN chmod +x /bin/print_hello

RUN apt-get install -y cmake

RUN useradd -ms /bin/bash devops2024user

COPY . /app
WORKDIR /app

RUN mkdir build && cd build && cmake .. && make

USER devops2024user

CMD ["python3", "app.py", "--port=8898"]

