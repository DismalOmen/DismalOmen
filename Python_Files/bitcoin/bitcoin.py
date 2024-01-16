import sys
import requests
if len(sys.argv) != 2 or sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")


else:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        x = (r.json()["bpi"]["USD"]["rate"]).replace(",","")
        y = (sys.argv[1])
        math = float(x) * float(y)
        print(f"${math:,.4f}")
    except requests.RequestException:
        sys.exit("Command-line argument is not a number")