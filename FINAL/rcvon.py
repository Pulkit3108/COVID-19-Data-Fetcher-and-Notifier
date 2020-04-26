#Run this Python code from your terminal: Due to security reasons we dont execute code directly. Stay safe




from plyer import notification
import requests
from bs4 import BeautifulSoup
import time 

def notify_me(title,message) :
    notification.notify(
        title = title, message = message ,  app_icon = "coronaIcon.ico" , timeout = 2
    )

def getDataFromUrl(url) :
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    
    
    myHtmlData = getDataFromUrl('https://www.mohfw.gov.in/')   
    
    soup = BeautifulSoup(myHtmlData , 'html.parser')
    myDataStr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDataStr += tr.get_text()
    myDataStr = myDataStr[1:]
    itemList = myDataStr.split('\n\n') 
    
    states = ['Delhi','Goa','Uttarakhand','Chandigarh','Jammu and Kashmir','West Bengal','Ladakh'] 
    for item in itemList[0:32]:
        dataList = item.split('\n')
        if dataList[1] in states :
            print(dataList)
            nTitle = 'Cases of covid-19'
            nText = f"STATE : {dataList[1]}\nTotal confirmed cases : {dataList[2]}\n Cured/Discharged : {dataList[3]}\nDeaths  : {dataList[4]}"
            notify_me(nTitle,nText)   
            time.sleep(2)
          
          