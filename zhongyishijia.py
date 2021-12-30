import requests
import bs4


def open_url(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    return requests.get(url,headers=headers)

def main():
    url = 'http://www.zysj.com.cn/index.html'
    res = open_url(url)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    targets = soup.select('#content > dl:nth-child(4) > dd > ul > li > a')
    for each in targets:
        print(each.text)

if __name__ == '__main__':
    main()
