FROM ubuntu:latest

# Установка необходимых пакетов
RUN apt-get update && apt-get install -y \
    cmake \
    python3 \
    python3-pip \
    git

# Установка Flask
RUN pip3 install Flask

# Копирование файлов проекта в образ
COPY . /app
COPY README.md /

# Создание исполняемого файла print_hello
RUN mkdir -p /bin && \
    echo '#!/bin/bash\necho "Hello world"' > /bin/print_hello && \
    chmod +x /bin/print_hello

# Установка git
RUN apt-get install -y git

# Команды для сборки проекта на cmake
RUN mkdir -p /app/build && \
    cd /app/build && \
    cmake .. && \
    make

# Создание пользователя devops2024user и установка прав
RUN useradd -ms /bin/bash devops2024user
RUN chown -R devops2024user /app

# Пользователь для выполнения команд внутри контейнера
USER devops2024user

# Команда для запуска процесса
CMD ["python3", "-u", "/app/app.py", "--host", "0.0.0.0", "--port", "8898"]

