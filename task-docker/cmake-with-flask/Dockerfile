FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    cmake \
    python3 \
    python3-pip \
    git

RUN pip3 install Flask

COPY . /app
COPY README.md /

RUN mkdir -p /bin && \
    echo '#!/bin/bash\necho "Hello world"' > /bin/print_hello && \
    chmod +x /bin/print_hello

RUN apt-get install -y git

RUN mkdir -p /app/build && \
    cd /app/build && \
    cmake .. && \
    make

RUN useradd -ms /bin/bash devops2024user
RUN chown -R devops2024user /app

USER devops2024user

CMD ["python3", "-u", "/app/app.py", "--host", "0.0.0.0", "--port", "8898"]

