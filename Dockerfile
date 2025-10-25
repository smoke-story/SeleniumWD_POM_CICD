FROM python:3.13.9-alpine3.22

ENV PYTHONUNBUFFERED=1

# update apk repo
# RUN echo "https://dl-4.alpinelinux.org/alpine/v3.23/main" >> /etc/apk/repositories && \
#     echo "https://dl-4.alpinelinux.org/alpine/v3.23/community" >> /etc/apk/repositories

RUN apk add --no-cache chromium chromium-chromedriver

# Get all the prereqs
# RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
# RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/tag/2.35-r1/glibc-2.35-r1.apk
# RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/tag/2.35-r1/glibc-bin-2.35-r1.apk

# Installing allure-commandline
RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.35.0.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.35.0/allure-commandline-2.35.0.tgz && \
    tar -zxvf allure-2.35.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.35.0/bin/allure /usr/bin/allure && \
    rm allure-2.35.0.tgz

WORKDIR /usr/workspace

COPY ./requirements.txt /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt