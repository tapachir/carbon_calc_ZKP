FROM zokrates/zokrates:0.7.13

USER root
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y \
    software-properties-common \
    npm
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash -
RUN apt-get -y install nodejs
RUN npm install
RUN npm -global --quiet install truffle
RUN apt-get install python3-requests

COPY . .
RUN chmod u+x run_authority.sh
RUN npm install

EXPOSE 8001
