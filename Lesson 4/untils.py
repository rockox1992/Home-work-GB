from datetime import datetime
import requests


def currency_rates(currency_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    """ we get the current rate by currency code from the site """
    if not (currency_code and url):
        return print(None)
    currency_code = currency_code.upper()
    respond = requests.get(url)
    if respond:
        cur = respond.text.split(currency_code)
        if len(cur) != 2:
            return print(None)
        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))
        date = respond.headers['Date']
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        return print(value, date)
    else:
        return print(None)
