import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
url = 'https://bixuejian.5000yan.com'
responses = requests.get(url=url, headers=headers)
responses.encoding = "utf-8"
page_text = responses.text
soup = BeautifulSoup(page_text, 'lxml')
#print(page_text)
#print(soup)
a_list = soup.select('.paiban > li > a')#class 标签属性为paiban

for a in a_list:
    title = a.string
    detail = a["href"]
    print(title,detail)

    detail_response = requests.get(url=detail,headers=headers)
    detail_response.encoding = "utf-8"
    detail_page_text = detail_response.text
    detail_soup = BeautifulSoup(detail_page_text,"lxml")
    p_list = detail_soup.find("div",class_ = "grap")
    content = p_list.text

    fileName = 'xiaoshuo/' + title + ".text"
    with open(fileName,"w") as fp:
        fp.write(title + '\n' + content)

