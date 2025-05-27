#!/usr/bin/env python3
# Simple CLI command consuming Shodan API
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history, date format ISO 8601:
#  2025-01-14  1.0 Initial version

# Modules to import
import json           # JSON encoder and decoder
import shodan         # Shodan Python library
import sys            # system-specific parameters and functions


def readConf():
    """ 
    read_conf() reads the application's configuration from an external file.
    The file is JSON-formatted and contains the API key.
    """
    with open('token.json', 'r') as config_in:
        config_json = json.load(config_in)
    return config_json


def main():
    if len(sys.argv) == 1:
        print('Usage: %s <search query>' % sys.argv[0])
        sys.exit(1)

    try:
        # Search Shodan
        config = readConf()
        API_KEY = config['SHODAN_API_KEY']
        api = shodan.Shodan(API_KEY)

        query = ' '.join(sys.argv[1:])
        results = api.search(query)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print('Port: {}'.format(result['port']))
#            print(result['data'])
            print('')

    except shodan.APIError as e:
        print('Error: {}'.format(e))


# Main function
if __name__ == '__main__':
    main()
