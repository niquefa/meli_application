# Python exploration implementing a rest API

**Here goes the problem description.**

## Running locally

* This app uses [docker](https://docs.docker.com/engine/install/) 
* For local testing, the next environmental varible should exists: ```export ENVIRONMENT="TEST"```
* This project uses a virtual env, you should set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/) to
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To get the local enviroment running: ```docker-compose up -d``` and  ```docker-compose run dbmate```
* To run unit testing: `./test.sh`
* To locally start the service: `: ./run.sh`

## Load test
Load test file in jmeter. Inside the folder ```loadtest```

## Black Prettier

This code has been beautify using black: https://github.com/psf/black. 
The command `black . -l 120`.

## Work to do:

* Add load balancing.
* Add task replication rules.
* Make load test.
* Make infrasctucture analysis and advices. 