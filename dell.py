import bs4, requests
from forex_python.converter import CurrencyRates

# Downloads the page.
response = requests.get("https://www.dell.com/en-ca/shop/dell-laptops/inspiron-15-laptop/spd/inspiron-15-5515-laptop/ni155515_sb_h109e")

# Check for status code.
response.raise_for_status()

# Parses the code.
soup = bs4.BeautifulSoup(response.text, "lxml")

# The selector for that element.
element = soup.select("body > main > section.container.mt-3.back-to-top-container > div.row.hero-content > div:nth-child(1) > div:nth-child(2) > div.mb-1 > span:nth-child(2) > span")

# Only the first element which is price in canadian dollars.
cad = element[0].text

# Calls the currency object.
c = CurrencyRates()

exchange_rate = c.get_rate("CAD", "INR")

print(f"Inspiron-15: {cad}")

# Formats the amount in float strips away comma.
number = float(cad[5:].replace(",", ""))

# The price in Indian rupees.
print(f"\nRs {int(number*exchange_rate)}")
