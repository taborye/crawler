import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

url = "https://www.yuetxt.com/yuedu/885/"


data_page = requests.get(url=url,headers=headers).text

tree = etree.HTML(data_page)

dd_list = tree.xpath('//*[@id="list"]/dl/dd')
fp = open()
for dd in dd_list:
    title = dd.xpath('./a/text()')
    t_url = dd.xpath('./a/@href')[0]
    print(title,t_url)

    file = "/xiaoshuo/." + title[0]
    c_url = "https://www.yuetxt.com/" + t_url
    x_page = requests.get(url=c_url, headers=headers).text
    tree = etree.HTML(x_page)
    data = tree.xpath('//*[@id="content"]/p/text()')
    #data_str = ' '.join(data)
    #with open(file,'w') as fp:
        #fp.write(data_str)
