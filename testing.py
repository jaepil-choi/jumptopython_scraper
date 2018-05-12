import pdfkit
import requests
from bs4 import BeautifulSoup as bs

# pdfkit.from_url('https://www.google.com/', 'out.pdf') # >> 잘 반환.
# pdfkit.from_url('https://wikidocs.net/21', 'out.pdf') # >> 아무것도 업는 빈 pdf 반환.

# jump = requests.request('GET',"https://wikidocs.net/21") # >> request 200 잘 뜸.

# jump_get = requests.get('https://wikidocs.net/21')
# jump_parse = bs(jump_get.text, 'html.parser')
# content = jump_parse.select('div#load_content') # >> 리스트 안에 <class 'bs4.element.Tag'> 가 1개 들어있음.
# content_str = str(content[0])
# pdfkit.from_string(content_str, 'out.pdf') # >> 아무것도 없는 빈 pdf 반환....

## html로 내보내도 파일이 안열림.
# text = open("output.txt", 'w')
# text.write(content_str)
# text.close()

# jump_get = requests.get('https://wikidocs.net/21')
# pdfkit.from_string(jump_get.text, 'out.pdf') # 빈 pdf 반환.


##### below is done by my friend Tae Hoon Jeon (It works.) #####

a = requests.get('http://wikidocs.net/14')

doc = bs(a.text,'html.parser')

header = doc.select_one('head')
content = doc.select("div#load_content")[0]

with open('jump1.html', 'w', encoding='UTF-8') as f:
    f.write('<base href="https://wikidocs.net">'+str(header))
    f.write(str(content).replace("display:none",""))

pdfkit.from_file('jump1.html', 'out2.pdf')

