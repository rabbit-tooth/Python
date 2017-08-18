#coding=UTF-8
import urllib
import re

#Author by 2017/6/3

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r"http.+?\.jpg"
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    
    i = 1
    for imgurl in imglist:
        cluster = imgurl.split("http")
        imgurl = "http" + cluster[len(cluster)-1]
        urllib.urlretrieve(imgurl,'%s.jpg' % i)
        i += 1

html = getHtml("https://cn.bing.com/images/search?q=治愈系美女&FORM=ISTRTH&id=3AEBDCF84A506FCB268EEEE486C55882B20291DF&cat=美女&lpversion=")

getImg(html)