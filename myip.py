import bs4, requests

def getip():
    s = requests.get('https://2ip.ua/ru/')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    a = b.select(" .ipblockgradient .ip")[0].getText()
    a = a.strip()
    return a
#print(getip())