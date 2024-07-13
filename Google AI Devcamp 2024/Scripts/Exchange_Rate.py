# Discord script

import os
import requests
import urllib.parse

def get_currency_rate(base_currency: str, target_currency: str):
    url = f"https://api.exchangerate-api.com/v4/latest/{urllib.parse.quote(base_currency)}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            rate = data["rates"].get(target_currency)
            if rate is not None:
                return rate
            else:
                print(f"Target currency '{target_currency}' not found")
                return None
        except KeyError:
            print(f"Error processing data for currency '{base_currency}'")
            return None
    else:
        print(
            f"Failed to retrieve data for currency '{base_currency}': {response.status_code}"
        )
        return None


class Tools:
    def __init__(self):
        pass

    def get_exchange_rate(self, base_currency: str, target_currency: str) -> str:
        """Get the current exchange rate from one currency to another.

        :param base_currency: The base currency code (e.g., 'USD').
        :param target_currency: The target currency code (e.g., 'EUR').
        :return: The current exchange rate or an error message.
        """
        rate = get_currency_rate(base_currency, target_currency)

        if rate is not None:
            return f"The current exchange rate from {base_currency} to {target_currency} is {rate:.2f}."
        else:
            return "Error fetching exchange rate data."
        

if __name__ == "__main__":
    rate = get_currency_rate("EUR", "GBP")
    print(f"EUR/GBP: {rate}")