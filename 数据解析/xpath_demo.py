## xpath 的编码流程
'''
    1 创建一个etree 类型的对象，把被解析的数据加载到该对象中
    2 调用etree
    标签是遵从一个树状结构


'''
import requests

'''
from lxml import etree

tree = etree.parse("test.html")
tree.xpath("xpath 表达式")
tag  = tree.xpath('/html/head/title')#绝对路径
tag = tree.xpath('//title')#相对路径
tag = tree.xpath('//div[@class = "song"]')#属性定位 定位class属性值为song的div标签
tag = tree.xpath('//*[@class = "song"]')#属性定位 定位class属性值为song的div标签
tag = tree.xpath('//div[@class = "song"]/p')
tag = tree.xpath('//div[@class = "song"]/p[3]')

tag = tree.xpath('//div[@class = "tang"]/url/li')
tag = tree.xpath('//div[@class = "tang"]//li')

tag = tree.xpath('//title/text()')#string
tag = tree.xpath('//dev[@class = "song"]//text()')#text

tag = tree.xpath('//img/@src')[0]#取属性

'''
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
url = "https://pic.netbian.com/4kmeinv"

response = requests.get(url = url,headers = headers)
response.encoding = "gbk"
page_text = response.text

#数据解析：图片的地址和图片的名称
tree = etree.HTML(page_text)
#全局解析
li_list = tree.xpath('//div[@class = "slist"]/ul/li')

for li in li_list:
    #局部解析
    img_src = "https://pic.netbian.com" + li.xpath('./a/img/@src')[0]
    img_title = 'picture/' +li.xpath('./a/b/text()')[0] + '.jpg'
    print(img_title)

    #对图片地址发请求
    image_data = requests.get(url=img_src,headers=headers).content
    with open(img_title,"wb") as fp:
        fp.write(image_data)
        print(image_data,":保存成功")


# 爬取https://sc.chinaz.com/tupian/meinvtupian.html
#1如果要爬取多页的时候，注意一个知识点: 图片懒加载。



def lanjiazai():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    url = "https://sc.chinaz.com/tupian/meinvtupian.html"

    page_text = requests.get(url = url,headers =  headers).text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('/html/body/div[3]/div[2]/div')

    for div in div_list:
        src = "https:" + div.xpath('./img/@data-original')[0]
        print(src)

