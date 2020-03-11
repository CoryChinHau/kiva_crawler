#抓kiva文字資料
import requests
from bs4 import BeautifulSoup
import json
import csv
    
path = "/Users/liujinhao/Desktop/kiva/url_output.csv"
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
    sel_url = soup.select("img.loan-image")
    pic = sel_url[0]["src"]
    print(pic)

    print("第",q,"位id:",ID_array[i])        
        
    ID = ID_array[i]
    if len(sel_url) == 0:
        url = "Null"
    else:
        url = pic
    
    # with open(path,'w') as f:
    #     csv_write = csv.writer(f)
    #     csv_head=["ID","name", "country", "typeName", "total_loan","amount_raised","amount-to-go", "lender_numbers" ,"days_left", "loan_use", "loan_length", "repayment_schedule", "sel_disbursed_date", "funding_model", "currency_exchange_loss", "field_partner", "borrower_paying_interest"]
    #     csv_write.writerow(csv_head)
    with open(path, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ID, url])

print("爬蟲結束")