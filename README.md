##Usage

Creating for test and learning purpose! This example uses BeautifulSoup4 for parsing.


```python
from wiki_country_scraper import WikiCScraper

scraper = WikiCScraper()

print scraper.get_country_info("pakistan")
print scraper.get_country_info("india")
```

```javascript
{u'Calling code': u'+92', u'Density': u'260.8/km', u'Demonym': u'Pakistani', u'b.': u'See also ', u'Prime Minister': u'Nawaz Sharif', u'Religion': u'Islam', u'2015\xa0estimate': u'199,085,847', u'Drives on the': u'left', u'Capital': u'Islamabad', u'HDI': u'\xa00.538', u'Islamic Republic': u'23 March 1956\xa0', u'Gini': u'30.0', u'Government': u'Federal', u'Water\xa0(%)': u'3.1', u'ISO 3166 code': u'PK', u'Flag': u'Emblem', u'Declaration': u'28 January 1933\xa0', u'Lower house': u'National Assembly', u'President': u'Mamnoon Hussain', u'Per capita': u'$1,427.08', u'Legislature': u'Majlis-e-Shoora', u'Upper house': u'Senate', u'Conception': u'29 December 1930\xa0', u'Official languages': u'English', u'Time zone': u'PST', u'a.': u'See also ', u'Dominion': u'14 August 1947\xa0', u'Recognised national\xa0languages': u'Urdu', u'Resolution': u'23 March 1940\xa0', u'GDP': u'2015\xa0estimate', u'Chief Justice': u'Anwar Zaheer Jamali', None: None, u'Internet TLD': u'.pk', u'Regional languages': u'Punjabi', u'Currency': u'Pakistani rupee', u'Largest city': u'Karachi', u'Total': u'$270.961 billion', u'Ethnic\xa0groups': u'Punjabis'}
{u'Calling code': u'+91', u'Density': u'388.9/km', u'Official languages': u'Hindi', u'Speaker of the Lower House': u'Sumitra Mahajan', u'Religion': u'79.8% ', u'2016\xa0estimate': u'1,293,057,000', u'Republic': u'26 January 1950\xa0', u'Drives on the': u'left', u'2011\xa0census': u'1,210,854,977', u'Capital': u'New Delhi', u'Currency': u'Indian rupee', u'HDI': u'\xa00.609', u'Recognised regional\xa0languages': u'\n', u'Time zone': u'IST', u'Gini': u'33.9', u'Government': u'Federal', u'Water\xa0(%)': u'9.6', u'ISO 3166 code': u'IN', u'Flag': u'State Emblem', u'Lower house': u'Lok Sabha', u'President': u'Pranab Mukherjee', u'Per capita': u'$1,820', u'Legislature': u'Parliament of India', u'Upper house': u'Rajya Sabha', u'Prime Minister': u'Narendra Modi', u'Dominion': u'15 August 1947\xa0', u'GDP': u'2016\xa0estimate', u'Chief Justice': u'T. S. Thakur', None: u'DST', u'Date format': u'dd-mm-yyyy', u'Vice-President': u'Mohammad Hamid Ansari', u'Internet TLD': u'.in', u'Demonym': u'Indian', u'National language': u'None', u'Largest city': u'Mumbai', u'Total': u'$2.384 trillion'}
```