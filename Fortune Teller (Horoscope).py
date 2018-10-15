#Fortune Teller (Horoscope)
import urllib.request
import urllib.parse
from time import sleep
import re
zodiac=input('enter the zodiac sign')
print('here is the result for a week starting paragrapgh from monday till friday then weekend.Enjoy!!')
try:
    #url ='https://www.google.com/search?q=http://astrostyle.com/daily-horoscopes/gemini-daily-horoscope/'
    #url ='http://astrostyle.com/daily-horoscopes/gemini-daily-horoscope/'
    a ='http://astrostyle.com/daily-horoscopes/'
    c='-daily-horoscope/'
    url =a+zodiac+c
    #print(url)
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"


    values ={'q':'Gemini','submit':'search'}
    data =urllib.parse.urlencode(values)
    data = data.encode('utf-8')#bytes conversion

    req =urllib.request.Request(url,data=data,headers =headers)
    #pass the side tag above in req headers =headers

    resp =urllib.request.urlopen(req)
    respdata =resp.read()
    #print(respdata)
    savefile = open('withheaders.txt','w')
    savefile.write(str(respdata))
    savefile.close()
    paragraph =re.findall(r'<p>(.*?)</p>',str(respdata))
    for eachP in paragraph:
        print(eachP)
    sleep(10)

except Exception as e:
    print(str(e))


