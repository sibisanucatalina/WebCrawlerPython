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
table_name = table.find('th')
#
# first_td = table.find('td')
# second_td = first_td.find_next_sibling('td')
# third_td = second_td.find_next_sibling('td')
# print(first_td.text)
# print(second_td.text)
# print(third_td.text)
# #Version date
version_date = table.find('local-time')
#
# print(table_name.text)
# print(first_td.text, " ",  version_date.text)

for child in table:
    for td in child:
        # print(td)
        version = td.find('td')

        # start_date_1 = str(start_date)

        # time2 = time.find_next_sibling('local-time')
        if type (version) != int:
            words = str(version).lstrip("<td>").rstrip("</td>")
            start_date = str(td.find('local-time'))
            start_date_1 = start_date[48:]
            start_date_1 = start_date_1[:-13]
            # end_date = td.find('td').find_next_sibling('local-time')
            # end_date = end_date[48:]
            # end_date = end_date[:-13]
            # print(td)
            print(start_date_1)

            # print(words + "   " + start_date_1)

#
# with open('releases.txt', 'w') as outfile:
#     json.dump(str(first_td), outfile)

