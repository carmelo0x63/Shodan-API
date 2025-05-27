# Shodan API
Shodan is developed with an API-first approach: anything that can be done using their websites you can also do directly via the API. The [REST API](https://developer.shodan.io/api/introduction) provides methods to search Shodan, look up hosts, get summary information on queries and a variety of utility methods to make developing easier. 
In this repository a Python wrapper to Shodan's API is provided that can be used to run quick, CLI-based, searches. The wrapper is based on Shodan's [Python library](https://github.com/achillean/shodan-python) simplifying the way users can reach the REST endpoints.
This is a simple alternative to the more feature-rich [`shodan` CLI command](https://cli.shodan.io/).

----

### Installation
Clone the GitHub repo:
```
$ git clone https://github.com/carmelo0x63/Shodan-API.git
```

Create a Python3 virtual environment and activate its dependencies:
```
$ cd Shodan-API

$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ python3 -m pip install --upgrade pip setuptools wheel

(venv) $ python3 -m pip install --upgrade shodan
```

----

### Examples
```
./apiquery.py IP:208.67.222.222
Results found: 4
IP: 208.67.222.222
Port: 53

IP: 208.67.222.222
Port: 80

IP: 208.67.222.222
Port: 443

IP: 208.67.222.222
Port: 5353
```

```
./apiquery.py AS:109    
Results found: 4806
IP: 51.174.72.94
Port: 443

IP: 124.122.12.64
Port: 8085

...
```
