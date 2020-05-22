FROM gitpod/workspace-full
                    
USER gitpod

RUN pyenv uninstall 2.7.17
RUN pyenv uninstall 3.8.2
RUN pyenv install 3.7.7
RUN pyenv global 3.7.7
# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && #     sudo apt-get install -yq bastet && #     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/config-docker/
