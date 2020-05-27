FROM gitpod/workspace-full


ENV PATH=/usr/lib/dart/bin:$PATH

USER root

RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list && \
    apt-get update && \
    apt-get -y install  build-essential dart libkrb5-dev gcc make && \
    apt-get clean && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*;

USER gitpod

### Install Flutter
# dependencies
RUN set -ex; \
    sudo apt-get update; \
    sudo apt-get install -y libglu1-mesa; \
    sudo rm -rf /var/lib/apt/lists/*

RUN set -ex; \
    mkdir ~/development; \
    cd ~/development; \
    git clone https://github.com/flutter/flutter.git -b stable

ENV PATH="$PATH:/home/gitpod/development/flutter/bin"

RUN set -ex; \
    flutter channel beta; \
    flutter upgrade; \
    flutter config --enable-web; \
    flutter precache
