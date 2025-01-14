#!/usr/bin/env python3

import shodan
import sys

SHODAN_API_KEY = "<put_personal_api_token_here>"

if len(sys.argv) == 1:
        print('Usage: %s <search query>' % sys.argv[0])
        sys.exit(1)

try:
    # Search Shodan
    api = shodan.Shodan(SHODAN_API_KEY)

    query = ' '.join(sys.argv[1:])
    results = api.search(query)

    # Show the results
    print('Results found: {}'.format(results['total']))
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print('Port: {}'.format(result['port']))
        print(result['data'])
        print('')

except shodan.APIError as e:
    print('Error: {}'.format(e))
