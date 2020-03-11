#kiva抓照片，且用id取圖片名稱
import requests
from bs4 import BeautifulSoup
import json
    
test = open("/Users/liujinhao/Desktop/kiva/kiva_photo/test.txt","w",encoding='UTF-8')
url_page = "https://www.kiva.org/lend-by-category/women"
j=0 #為了印頁數
for i in range(262):
    p = requests.Session()
    r = requests.get(url_page)
    a = []
#     print(r)
    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.borrower-image-wrapper.offset-borrower-image a.borrower-image-link")
    u = soup.select("li.pagination-next a")
    print ("本頁的URL為"+url_page)
    for s in sel:
        a.append(s["href"])
#     print(a)
    
    q=0 #為了印張數
    j+=1
    print ("第",j,"頁的URL為:"+url_page)
    for i in a[0:]:
        url = "https://www.kiva.org"+i
        test.write("第 {} 頁的URL為: {} \n".format(j,url))
        url=requests.get(url)
        soup = BeautifulSoup(url.text,"html.parser")
        sel_jpg = soup.select("img.loan-image")
        for c in sel_jpg:
            q+=1
            print(c)
            print("第",q,"張:",c["src"])
            test.write("%\n""第 {} 張: {} \n".format(q,c["src"])) 
            pic=requests.get(c["src"])
            img2 = pic.content
            pic_out = open("/Users/liujinhao/Desktop/kiva/kiva_photo/"+str(i[-7:])+".png",'wb')
            pic_out.write(img2)
            pic_out.close()
    url_page ="https://www.kiva.org/"+ u[0]["href"]


test.close()
print("爬蟲結束")