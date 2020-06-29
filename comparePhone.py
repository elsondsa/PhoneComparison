from urllib.request import Request, urlopen
import urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

phone1 =input('Enter phone 1: ')
phone2 =input('Enter phone 2: ')

params = dict()
query = phone1 + ' and ' + phone2

params['q'] = query

serviceurl = 'http://www.google.com/search?'

url = serviceurl + urllib.parse.urlencode(params)

print(url)


        

uh = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
uhl = urlopen(uh, context=ctx)
data = uhl.read().decode()
soup = BeautifulSoup(data, 'html.parser')

tags = soup('a')

for i in range(0,len(tags)):
    target = tags[i].get('href', None)
    a = target.find('gadgetsnow.com')
    if a!=-1:
        print(target)
        break

url = 'http://www.google.com'+target

uh = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
uhl = urlopen(uh, context=ctx)
data = uhl.read().decode()
soup = BeautifulSoup(data, 'html.parser')



headings = soup.findAll('div', {'class' : "compare_hdn"})


i=-1
bigdata = {}

tables = soup.findAll( "table", {"class":"inr_tbl"} )

for table in tables:
    i = i+1
    data = {}
    rows = table.findAll('tr')
    for tr in range(0,len(rows)):
        key = rows[tr].find( "td", {"class":"title"} ).text
        values = rows[tr].findAll( "td", {"class":"val"} )
        value1 = values[0].text
        value2 = values[1].text
        l=[]
        l.append(value1)
        l.append(value2)
        data[key] = l
    bigdata[headings[i].text] = data

for heading in bigdata:
    print(heading,"\n")
    for key in bigdata[heading]:
        print(key,": ",bigdata[heading][key],"\n")
    print("\n\n\n")
            
