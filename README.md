## magik-scraper
Scrap & Save lastes updated fund performance to csv

## Features
* Currently NAV
* NAV Change
* Bid
* Offer
* Datetime

## Requirement
* Python 3.6+
* Requests 2.22.0
* Beautiful Soup 4.7.1

## Download
Clone or Download as zip

## Quickstart
```python
import magik

# url from Fund Performance not a Fund Profile!
url = 'https://www.wealthmagik.com/FundInfo/FundPerformance-TMBAM-MIXBAL-TMBAALF-กองทุนเปิดทหารไทยจัดทัพลงทุน%20ระยะยาว'
filename = 'TMBAALF'
magik.scrape(url, filename)
