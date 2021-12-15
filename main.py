import requests
import json
from bs4 import BeautifulSoup

URL = "https://docs.microsoft.com/en-us/lifecycle/products/internet-information-services-iis"
page = requests.get(URL)

#print(page.text)
soup = BeautifulSoup(page.content, "html.parser")

#Find the right tabel heading
results = soup.find(id="releases")

table = results.find_next_sibling('table')

#Table name
#table_name = table.find('th')
#
# first_td = table.find('td')
# #Version date
# version_date = table.find('local-time')
#
#print(table_name.text)
# print(first_td.text, " ",  version_date.text)

for child in table.children:
    for td in child:
        version = td.find('td')
        if type (version) != int:
            words = str(version).lstrip("<td>").rstrip("</td>")
            print(words)

#
# with open('releases.txt', 'w') as outfile:
#     json.dump(str(first_td), outfile)

