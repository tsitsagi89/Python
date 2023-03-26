import requests
import sys
try:
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        r.json()
        price = float(r.json()['bpi']['USD']['rate'].replace(",", ""))
        amount =  float(sys.argv[1]) * price
        print(f"${amount:,.4f}")
except ValueError:
    print('Command-line argument is not a number')
except requests.RequestException:
    print("There was an ambiguous exception that occurred while handling your request")
