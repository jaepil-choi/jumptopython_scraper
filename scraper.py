import pdfkit
import requests
from bs4 import BeautifulSoup as bs

a = requests.get('http://wikidocs.net/14')

doc = bs(a.text,'html.parser')

header = doc.select_one('head')
content = doc.select("div#load_content")[0]

with open('jump1.html', 'w', encoding='UTF-8') as f:
    f.write('<base href="https://wikidocs.net">'+str(header))
    f.write(str(content).replace("display:none",""))

pdfkit.from_file('jump1.html', 'out2.pdf')