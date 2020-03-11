#抓kiva文字資料
import requests
from bs4 import BeautifulSoup
import json
import csv
    
with open("/Users/liujinhao/Desktop/kiva/women_photoID_新增.csv",'r',newline='',encoding='utf-8-sig') as csvfile:
    rows = csv.DictReader(csvfile)
    ID_array = []
    for row in rows:
        ID_array.append(row['ID'])
q = 0
for i in range(len(ID_array)):
    q+=1
    url_page = "https://www.kiva.org/lend/"+ID_array[i]+"?minimal=false"
    p = requests.Session()
    url = requests.get(url_page)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_story = soup.select("div.green-bolded.endorsement")
    # print("第",q,"位story:",sel_story[0].text.strip())
        
        

    story = sel_story[0].text.strip()

    story_out = open("/Users/liujinhao/Desktop/python_practice/kiva_special_story/"+str(ID_array[i][-7:])+".txt",'w',encoding='UTF-8')
    story_out.write(story)
    story_out.close()
        
        
        
    print("第",q,"位id:",ID_array[i])

print("爬蟲結束")