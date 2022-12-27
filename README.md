# Web Scraping NBA Data With Python, Google colab, BeautifulSoup and Pandas

### The 2021–2022 NBA season is finally upon us! To celebrate this momentous occasion 
as a budding data scientist and long-time NBA fan, I thought it would be a fun practice to web scrape data from [Basketball-Reference](https://www.basketball-reference.com/leagues/NBA_2022_per_game.html),
a site that holds statistics for all things professional basketball, from the NBA to the WNBA and G League.
Since I support the Washington Wizards (yes, it’s tough out here so far, but we have to stay loyal 😤),
the focus for this post will be to extract per game 2021–2022 statistics for each Wizards player,
as well as some other individual information.

### For the uninitiated, web scraping is the process of extracting and restructuring data from a website,
usually to allow for some kind of eventual analysis. In this case, I’ll be leveraging requests and BeautifulSoup,
two Python libraries used for accessing websites and parsing HTML , 
as well as pandas, a Python library that will allow for structuring the information into a manipulable dataframe.

