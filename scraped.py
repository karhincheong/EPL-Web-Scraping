from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = "https://www.theguardian.com/football/premierleague/table"
page = urlopen(URL)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')


def get_table():
    """
    Returns a list of lists containing the table data.
    """
    table = []
    for row in soup.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        table.append(row_data)
    return table


table = get_table()




