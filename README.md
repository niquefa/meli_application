# Python exploration implementing a rest API

**The problem description is private, I should ask for permission to share it, I probably will not get it**

# Python version

This repository is made in Python 3.6.9 and pip3 (version 21.1.2). Make sure you have those installed in your system.

# Reference document

In this document I explain several considerations: [go to document](https://docs.google.com/document/d/1ZZ_wVpf9ky831L_wC3IqByKQbIkgN4MtHrP81KQRGak/edit?usp=sharing) This links is broken, but here I did explain several improvement option in scalability and robustness.

## Running locally

* Note: This instructions are for linux systems. Windows or macOS will require some changes.
* This app uses [docker](https://docs.docker.com/engine/install/) for local testing. 
* For local testing, the next environmental varible should exists: ```export ENVIRONMENT="TEST"```
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
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
Name                          | Statemets | Missing | Cover
------------------------------------------------------------
analyzer/algorithms.py        |      29   |    5    |  83%
analyzer/analyzer_utils.py    |      18   |    3    |  83%
analyzer/config.py            |      28   |    3    |  89%
analyzer/constants.py         |       5   |    0    | 100%
analyzer/controller.py        |      29   |    7    |  76%
analyzer/data_generator.py    |      10   |    0    | 100%
analyzer/gateway.py           |      32   |    5    |  84%
test/test_algorithms.py       |      24   |    1    |  96%
test/test_analyzer_utils.py   |      15   |    1    |  93%
test/test_controller.py       |      41   |    1    |  98%
test/test_data_generator.py   |      13   |    1    |  92%
test/test_gateway.py          |      22   |    1    |  95%
```

## Load test
Load test file in jmeter. Inside the folder ```loadtest```. For load testing, in local, make sure, you have the user defined variables HOST and PORT in the values ```127.0.0.1``` and ```3000``` respectively.

For load testing the aws infrastructure, send me a message to get the host (or may be not, the billing could be high). 

## Black Prettier

This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.

## Codedeploy notes:

".github/workflows/build.yml" file and files in "codedeploy" folder are based on the ones in the next rust project: https://github.com/nbari/test_pipeline. Special thanks to nbari for setting an BSD 3-Clause License on his sample project and his advices related to my not so strong suit dev-ops skills. 
