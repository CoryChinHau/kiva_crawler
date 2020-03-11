#抓kiva文字資料
import requests
from bs4 import BeautifulSoup
import json
import csv
    
path = "/Users/liujinhao/Desktop/kiva/fundedd_Rate.csv"
with open("/Users/liujinhao/Desktop/python_practice/women_photoID_fundedRate.csv",'r',newline='',encoding='utf-8-sig') as csvfile:
    rows = csv.DictReader(csvfile)
    ID_array = []
    for row in rows:
        ID_array.append(row['ID'])
q = 0
for i in range(len(ID_array)):
    q+=1
    url_page = "https://api.kivaws.org/v1/loans/"+ID_array[i]+".xml"
    p = requests.Session()
    url = requests.get(url_page)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_name = soup.select('loan name')
    sel_posted_date = soup.select('loan posted_date')       
    sel_funded_date = soup.select('loan funded_date')
        
    print("第",q,"位id:",ID_array[i])

    ID = ID_array[i]
    if len(sel_name) == 0:
        name = "Null"
        print(ID_array[i],"未完成")
        break
    else:
        name = sel_name[0].text

    
    if len(sel_posted_date) == 0:
        posted_date = "Null"
    else:
        posted_date = sel_posted_date[0].text

    if len(sel_funded_date) == 0:
        funded_date = "Null"
    else:
        funded_date = sel_funded_date[0].text

    
    with open(path, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ID, name, posted_date,funded_date])

print("爬蟲結束")