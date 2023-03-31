#'C:\Users\patry\AppData\Local\Programs\Python\Python310\python.exe'

#'C:\Scraping\exercise_sending_emails.ipynb'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup 
import pandas as pd
import time

from email.message import EmailMessage
from passwo import password
import ssl
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from passwo import password

smtp_port = 587         
# serwer SMTP google        
smtp_server = "smtp.gmail.com" 


email_from = "patryk90020@gmail.com"
email_list = ["koko786@niepodam.pl"]


pswd = password



subject = "Wiadomosc z zalacznikiem"

def send_emails(email_list,path):

    for person in email_list:

       
        body = f"""
        Dzien dobry
        Przesylam zalacznik plik .csv
        """

        
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Dolaczenie ciala do email
        msg.attach(MIMEText(body, 'plain'))

        # plik do wyslania
        source = path
        file = path.split("\\")[4]
        attachment= open(source, 'rb')  

        # encode 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + file)
        msg.attach(attachment_package)

        
        text = msg.as_string()

        # polaczenie z serwerem SMTP
        print("Connecting")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")


        # wysylanie wiadomosci
        print(f"Sending email to: {person}")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")

    # zamykanie portu
    TIE_server.quit()


#### SENDING
driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
driver.get('https://pl.indeed.com/')

time.sleep(2)
job = driver.find_element('xpath','//*[@id="text-input-what"]')
job.send_keys('data analyst')

place = driver.find_element('xpath','//*[@id="text-input-where"]')
place.send_keys('Rzeszów, podkarpackie')

driver.find_element('xpath','//*[@id="jobsearch"]/button').click()

time.sleep(1)

postings = []


driver.execute_script('scrollTo(0, document.body.scrollHeight)')
time.sleep(2)



part_link = 'https://pl.indeed.com'
iterator = 0
df = pd.DataFrame({"Link": [], "Name":[], "Company":[], "Kind": []})

soup = BeautifulSoup(driver.page_source, 'lxml')
boxes = soup.find_all('div',{'class':'slider_container css-77eoo7 eu4oa1w0'})

while True:
    
    for box in boxes:
        try:
            name = box.find('a',{'class':'jcs-JobTitle css-jspxzf eu4oa1w0'}).text
            company = box.find('span',{'class':'companyName'}).text
            link = box.find('a',{'class' : 'jcs-JobTitle css-jspxzf eu4oa1w0'}).get('href')
            kind = box.find('div',{'class':'attribute_snippet'}).text
            full_link = part_link+link
            df = df.append({'Name': name, 'Link': full_link, 'Company':company, 'Kind':kind}, ignore_index = True)
        except:
            pass
   
   
    time.sleep(2)
    try:
        #button = soup.find('svg',class_ = 'css-13p07ha e8ju0x50').get('href')
        driver.find_element('xpath','//*[@id="jobsearch-JapanPage"]/div/div/div[5]/div[1]/nav/div[3]/a').click()                                  
        #driver.get(part_link+button) 
        soup = BeautifulSoup(driver.page_source, 'lxml')
        driver.execute_script('scrollTo(0, document.body.scrollHeight)')
        boxes = soup.find_all('div',{'class':'slider_container css-77eoo7 eu4oa1w0'})
    except:
        pass
    iterator +=1
    ramka = df.to_csv(r'C:\\Scraping\\email.csv')
    path = r'C:\\Scraping\\email.csv'
    if iterator == 2:
        send_emails(email_list,path)
        break