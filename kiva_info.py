#抓kiva文字資料
import requests
from bs4 import BeautifulSoup
import json
import csv
    
path = "/Users/liujinhao/Desktop/kiva/output.csv"
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
    sel_name = soup.select("div.loan-gist h1.borrower-name")
    sel_country = soup.select("div.country-text.columns.small-10 a.black-underlined")
    sel_typeName = soup.select("div.country-text.columns.small-10 span.typeName")
    sel_total_loan = soup.select("div.loan-total")
    sel_amount_raised = soup.select("div.current-status-meter div.amount-raised h2.green-bolded.inline")
    sel_amount_to_go = soup.select("div.amount-to-go-stat ")
    sel_lender_numbers = soup.select("div.raised-info.row  a.lender-count.black-underlined")
    sel_days_left = soup.select("div.days-left-stat ")
    sel_loan_use = soup.select("div.loan-use h2")
    sel_loan_length = soup.select("div.ac-body div.loan-term.print-5.columns div.green-bolded")
    sel_repayment_schedule = soup.select("div.loan-stats.print-7.columns #repayment-schedule strong")
    sel_disbursed_date = soup.select("div.loan-stats.print-7.columns #disbursed-date strong")
    sel_funding_model = soup.select("div.loan-stats.print-7.columns #funding-model strong")
    sel_currency_exchange_loss = soup.select("div.loan-stats.print-7.columns #currency-exchange-loss strong")
    sel_field_partner = soup.select("div.loan-stats.print-7.columns #field-partner strong")
    sel_borrower_paying_interest = soup.select("div.loan-stats.print-7.columns #borrower-paying-interest strong")
        
        
        
        
    print("第",q,"位id:",ID_array[i])
    # print("第",q,"位姓名:",sel_name[0].text)
    # print("第",q,"位國家:",sel_country[0].text)
    # print("第",q,"位類型:",sel_typeName[0].text)
    # print("第",q,"位募款金額:",sel_total_loan[0].text.strip().replace('Total loan: ', ''))
    # print("第",q,"位已募金額:",sel_amount_raised[0].text.strip())
    # print("第",q,"位剩餘金額:",sel_amount_to_go[0].text.replace(' to go', ''))
    # if len(sel_lender_numbers) == 0:
    #     print("第",q,"位贊助者人數:","0")
    # else:
    #     print("第",q,"位贊助者人數:",sel_lender_numbers[0].text.strip().replace('Powered by ', ''))

    # # print("第",q,"位贊助者人數:",sel_lender_numbers[0].text.strip().replace('Powered by ', ''))
    # print("第",q,"位剩餘天數:",sel_days_left[0].text.replace(' left', ''))
    # print("第",q,"位募款目的:",sel_loan_use[0].text.strip())
    # print("第",q,"位借款時間長度:",sel_loan_length[0].text)
    # print("第",q,"位還款頻率:",sel_Repayment_schedule[0].text)
    # print("第",q,"位支付日:",sel_disbursed_date[0].text)
    # print("第",q,"位支付模式:",sel_funding_model[0].text)
    # print("第",q,"位合夥人承擔損失:",sel_currency_exchange_loss[0].text)
    # print("第",q,"位合夥人:",sel_field_partner[0].text)
    # print("第",q,"位是否支付利息:",sel_borrower_paying_interest[0].text.strip())
        
        
    ID = ID_array[i]
    if len(sel_name) == 0:
        name = "Null"
    else:
        name = sel_name[0].text
    if len(sel_country) == 0:
        country = "Null"
    else:
        country = sel_country[0].text
    if len(sel_typeName) == 0:
        typeName = "Null"
    else:    
        typeName = sel_typeName[0].text
    if len(sel_total_loan) == 0:
        total_loan = "Null"
    else:        
        total_loan = sel_total_loan[0].text.strip().replace('Total loan: ', '')
    if len(sel_amount_raised) == 0:
        amount_raised = "Null"
    else:
        amount_raised = sel_amount_raised[0].text.strip()
    if len(sel_amount_to_go) == 0:
        amount_to_go = "Null"
    else:
        amount_to_go = sel_amount_to_go[0].text.replace(' to go', '')
    if len(sel_lender_numbers) == 0:
        lender_numbers = 0
    else:
        lender_numbers = sel_lender_numbers[0].text.strip().replace('Powered by ', '')
    if len(sel_days_left) == 0:
        days_left = "Null"
    else:
        days_left = sel_days_left[0].text.replace(' left', '')
    if len(sel_loan_use) == 0:
        loan_use = 0
    else:
        loan_use = sel_loan_use[0].text.strip()
    if len(sel_loan_length) == 0:
        loan_length = 0
    else:
        loan_length = sel_loan_length[0].text
    if len(sel_repayment_schedule) == 0:
        repayment_schedule = 0
    else:
        repayment_schedule = sel_repayment_schedule[0].text
    if len(sel_disbursed_date) == 0:
        disbursed_date = 0
    else:
        disbursed_date = sel_disbursed_date[0].text
    if len(sel_funding_model) == 0:
        funding_model = 0
    else:
        funding_model = sel_funding_model[0].text
    if len(sel_currency_exchange_loss) == 0:
        currency_exchange_loss = 0
    else:
        currency_exchange_loss = sel_currency_exchange_loss[0].text
    if len(sel_field_partner) == 0:
        field_partner = 0
    else:
        field_partner = sel_field_partner[0].text
    if len(sel_borrower_paying_interest) == 0:
        borrower_paying_interest = 0
    else:
        borrower_paying_interest = sel_borrower_paying_interest[0].text.strip()
    
    # with open(path,'w') as f:
    #     csv_write = csv.writer(f)
    #     csv_head=["ID","name", "country", "typeName", "total_loan","amount_raised","amount-to-go", "lender_numbers" ,"days_left", "loan_use", "loan_length", "repayment_schedule", "sel_disbursed_date", "funding_model", "currency_exchange_loss", "field_partner", "borrower_paying_interest"]
    #     csv_write.writerow(csv_head)
    with open(path, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ID, name, country, typeName, total_loan, amount_raised, amount_to_go, lender_numbers, days_left, loan_use, loan_length, repayment_schedule, disbursed_date, funding_model, currency_exchange_loss, field_partner, borrower_paying_interest])

print("爬蟲結束")