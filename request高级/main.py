#防盗链：主要在 爬取图片中
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
def fang_dao_lian():
    url = 'https://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1'
    headers["Referer"] = 'https://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1'
    print(headers)
    response = requests.get(url = url,headers = headers)
    page_text = response.text
    #print(page_text)
    tree = etree.HTML(page_text)
    img_list = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img')
    for img in img_list:#referer 起到防盗链的作用
        img_src = img.xpath('./@real_src')[0]
        img_data = requests.get(url = img_src,headers=headers).content
        with open('123.jpg',"wb") as fp:
            fp.write(img_data)
        break;

def shiping():#视频爬取
    url = "https://www.51miz.com/shipin"
    headers["REferer"] = "https://ckmap.mediav.com/"
    response = requests.get(url=url, headers=headers)
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    vedio_list = tree.xpath('//div[@class="category-item-preview miz-image-box"]/video/source')
    print(vedio_list)

    for vedio in vedio_list:
        src = vedio.xpath('./@src')[0]
        v_date = requests.get(url = src,headers=headers).content
        with open("./test.mp4","wb") as fp:
            fp.write(v_date)
        break;





#fang_dao_lian()

shiping()