# Python exploration implementing a rest API

**The problem description is private**

# Python version

This repository is made in Python 3.6.9 and pip version 21.1.2

# Reference document

In this document I explain several considerations: [go to document](https://docs.google.com/document/d/1ZZ_wVpf9ky831L_wC3IqByKQbIkgN4MtHrP81KQRGak/edit?usp=sharing)

## Running locally

* This app uses [docker](https://docs.docker.com/engine/install/) for local testing. 
* For local testing, the next environmental varible should exists: ```export ENVIRONMENT="TEST"```
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To get the local enviroment running: ```docker-compose up -d``` 
* To create the local database and db schema  ```docker-compose run dbmate```
* To run unit testing: `./test.sh`
* To locally start the service: `: ./run.sh`
* To test locally the health endpoint just make a GET request to ```http://127.0.0.1:3000/health``` 
* To test locally just make a POST request to ```http://127.0.0.1:3000/mutant``` with a payload similar to:

```Javascript
{
    "dna":["ATAA","GAAC","AGAA","AAAT"]
}
```
For more details on payload constrainst, check the document mentioned above.

* To test locally the stats endpoint just make a GET request to ```http://127.0.0.1:3000/stats```.

## Unit testing and test coverage
To check the test coverage, run `coverage run  -m unittest discover -v` and then run `coverage report`.

```
Name                          | Stmts | Miss | Cover
-----------------------------------------------------
analyzer/algorithms.py        |  29   | 5    |  83%
analyzer/analyzer_utils.py    |  18   | 3    |  83%
analyzer/config.py            |  28   | 3    |  89%
analyzer/constants.py         |   5   | 0    | 100%
analyzer/controller.py        |  29   | 7    |  76%
analyzer/data_generator.py    |  10   | 0    | 100%
analyzer/gateway.py           |  32   | 5    |  84%
test/test_algorithms.py       |  24   | 1    |  96%
test/test_analyzer_utils.py   |  15   | 1    |  93%
test/test_controller.py       |  41   | 1    |  98%
test/test_data_generator.py   |  13   | 1    |  92%
test/test_gateway.py          |  22   | 1    |  95%
```

## Load test
Load test file in jmeter. Inside the folder ```loadtest```. For load testing, in local, change user defined variables HOST and PORT for ```127.0.0.1``` and ```3000``` respectively.

For load testing the aws infrastructure, send me a message to get the host. 

## Black Prettier

This code has been beautify using black: https://github.com/psf/black. 
The command `black . -l 120`.
