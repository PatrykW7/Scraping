import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


url = "https://www.nfl.com/standings/league/2019/REG"
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.text,"lxml")

table = soup.find_all("table",{"summary":re.compile("Standings - Detailed View")})[0]
#table = soup.find_all("table",{"class":re.compile("d3-o-table d3-o-table--row-striping d3-o-table--detailed d3-o-standings--detailed d3-o-table--sortable {sortlist: [[4,1]], sortinitialorder: 'desc'}")})
#print(len(table)) 


headers = table.find_all("th")
#print(headers)

header_list = []
for header in headers:
    i = header.text
    header_list.append(i)
#print(header_list)

df = None
df = pd.DataFrame(columns = header_list)

# getting datas

rows = table.find_all("tr")[1:]


for row in rows:
    # W pierwszej komorce sa nazwy zespolow
    team_name = row.find_all("td")[0].find("div",{"class":"d3-o-club-fullname"}).text
    #print(team_name)
    wiersz = row.find_all("td")[1:]
    cell = [k.text for k in wiersz]
    cell.insert(0,team_name)
    length = len(df)
    df.loc[length] = cell
    
    
row.find_all("td")[1:]
print(df)