FROM ubuntu:latest

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    cmake \
    python3 \
    python3-pip \
    git \
    python3-flask

# Копирование файлов проекта в корень образа
COPY ./* /

# Установка git
RUN apt-get install -y git

# Команды для сборки проекта на cmake
RUN mkdir -p /build && \
    cd /build && \
    cmake .. && \
    make

# Создание исполняемого файла print_hello
RUN mkdir -p /bin && \
    echo '#!/bin/bash\necho "Hello world"' > /bin/print_hello && \
    chmod +x /bin/print_hello

# Создание пользователя devops2024user и установка прав
RUN useradd -ms /bin/bash devops2024user
RUN chown -R devops2024user /*

# Пользователь для выполнения команд внутри контейнера
USER devops2024user

# Команда для запуска процесса
CMD ["python3", "/app.py", "--port", "8898"]

