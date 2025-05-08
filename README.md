# Shodan API
Shodan is developed with an API-first approach: anything that can be done using their websites you can also do directly via the API. The [REST API](https://developer.shodan.io/api/introduction) provides methods to search Shodan, look up hosts, get summary information on queries and a variety of utility methods to make developing easier. 
In this repository a Python wrapper to Shodan's API is provided that can be used to run quick, CLI-based, searches. The wrapper is based on Shodan's [Python library](https://github.com/achillean/shodan-python) simplifying the way users can reach the REST endpoints.
This is a simple alternative to the more feature-rich [`shodan` CLI command](https://cli.shodan.io/).

----

### Installation
Clone the GitHub repo:
```
$ git clone https://github.com/carmelo0x63/Shodan-API
```

Create a Python3 virtual environment and activate its dependencies:
```
$ cd Shodan-API

$ python3 -m venv .

$ source bin/activate

$ python3 -m pip install --upgrade pip setuptools wheel

$ python3 -m pip install --upgrade shodan
```

----

### Examples

