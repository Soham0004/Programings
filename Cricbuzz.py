import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cricbuzz.com/cricket-series/5945/indian-premier-league-2023/points-table"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='cb-col cb-col-100 cb-ltst-wgt-hdr')
rows = table.find_all('tr')
data = []
for row in rows[1:]:
    cols = [ele.get_text(strip=True) for ele in row.find_all('td')]
    if cols:
        data.append(cols)
df = pd.DataFrame(data, columns=["Team", "Matches", "Won", "Lost", "Tied", "No Result", "Points", "NRR"])
print(df)
