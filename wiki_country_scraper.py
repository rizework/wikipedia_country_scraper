from bs4 import BeautifulSoup
import urllib2


class WikiCScraper:
    wiki_url = "https://en.wikipedia.org/wiki/"

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def get_country_info(self, country_name):
        req = urllib2.Request(self.wiki_url + country_name, headers=self.headers)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page, "html.parser")

        table = soup.find("table", {"class": "infobox geography vcard"})

        key = []
        val = []

        for row in table.findAll("tr"):
            cells = row.findAll("td")
            ths = row.findAll("th")
            if len(cells) > 0:
                if len(cells) == 2:
                    key.append(cells[0].find(text=True))
                    val.append(cells[1].find(text=True))
                elif len(cells) == 3:
                    key.append(cells[1].find(text=True))
                    val.append(cells[2].find(text=True))
                elif len(cells) == 1 and len(ths) == 1:
                    key.append(ths[0].find(text=True))
                    val.append(cells[0].find(text=True))

        dictionary = dict(zip(key, val))
        return dictionary
