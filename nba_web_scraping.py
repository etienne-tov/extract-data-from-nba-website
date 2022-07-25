import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.basketball-reference.com/leagues/NBA_2022_per_game.html"

response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find_all(class_="full_table")

players = []
for i in range(len(table)):
    player = []
    for j in table[i].find_all('td'):
        player.append(j.text)
    players.append(player)

head = soup.find(class_='thead')
column_name = [head.text for i in head][0]
column_name_clean = column_name.split('\n')[2:-1]

df = pd.DataFrame(players, columns=column_name_clean)
df.to_csv('nba.csv',index=False)
