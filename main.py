import requests
import json
from bs4 import BeautifulSoup

URL = "https://docs.microsoft.com/en-us/lifecycle/products/internet-information-services-iis"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Find the right tabel heading
results = soup.find(id="releases")

table = results.find_next_sibling('table')

#Table name
table_name = table.find('th')
# print(table_name.text + "                  " + "Start Date")

dict = {}

# for child in table:
#     for td in child:
#         version = td.find('td')
#         if type (version) != int:
#             words = str(version).lstrip("<td>").rstrip("</td>")
#             start_date = str(td.find('local-time'))
#             start_date_1 = start_date[48:]
#             start_date_1 = start_date_1[:-13]
#             dict[words] = start_date_1
ceva_lista = []
for child in soup.find_all('table'):
    #Aleg tabelul de care am nevoie, table ca variabila e definit mai sus
    if child == table:
        # print(child)
        for tr in child.find_all('tr'):
            for td in tr.find_all('td'):
                stringuri = str(td)
                ceva_lista.append(stringuri)

# for i in range(0, len(ceva_lista)-1):
#     # primul = ceva_lista[i].lstrip("<td>").rstrip("</td>")
#     print(ceva_lista[i])
version_list = []
for i in (ceva_lista[0:len(ceva_lista)-1:3]):
    version = i.lstrip("<td>").rstrip("</td>")
    version_list.append(version)
    # print(version)
for j in (ceva_lista[1:len(ceva_lista)-1:3]):
    start_date = j[67:]
    start_date = start_date[:-19]
    version_list.append(start_date)
    # print(start_date)
for k in (ceva_lista[2:len(ceva_lista)-1:3]):
    end_date = k[67:]
    end_date = end_date[:-19]
    version_list.append(end_date)
print(version_list)

    # print(i.lstrip("<td>").rstrip("</td>"))

# for i in (ceva_lista[1:len(ceva_lista)-1:3]):
#     word = i[67:]
#     word = word[:-19]
#     print(word)
#
# for i in (ceva_lista[2:len(ceva_lista)-1:3]):
#     word = i[67:]
#     word = word[:-19]
#     print(word)


# print(dict)
# with open('newtry.txt', 'w') as json_file:
#   json.dump(version_list, json_file)

