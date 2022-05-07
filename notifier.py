# Run this Python code from your terminal: Due to security reasons, we don't execute code directly. Stay safe.

from plyer import notification
from bs4 import BeautifulSoup
import requests
import time


def notify_me(title, message):
    notification.notify(
        title=title, message=message,  app_icon="img/coronaIcon.ico", timeout=2
    )


def getDataFromUrl(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    myHtmlData = getDataFromUrl('https://www.mygov.in/covid-19')
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    myDataStr = dict()
    for i in range(36):
        stateName = soup.find_all("span", {"class": "st_name"})[i].get_text()
        dataList = soup.find_all("div", {"class": "st_all_counts"})[
            i].get_text().split('\n')
        myDataStr[stateName] = [dataList[1].split(' ')[1], dataList[2].split(
            ' ')[1], dataList[3].split(' ')[1], dataList[4].split(' ')[1], dataList[6].split(' ')[1]]
    print('\n\n-------------------------COVID-19 Notifier-------------------------\n')
    while(1):
        s = input("Enter the Name of The State (or Enter 0 to exit): ")
        print('\n')
        if(s == '0'):
            break
        if s in myDataStr.keys():
            nTitle = 'Cases of COVID-19'
            nText = f"STATE : {s}\nConfirmed : {myDataStr[s][0]}\nActive : {myDataStr[s][1]}\nDischarged : {myDataStr[s][2]}\nDeaths : {myDataStr[s][3]}\nVaccination : {myDataStr[s][4]}\n"
            notify_me(nTitle, nText)
            time.sleep(2)
        else:
            print('Invalid State\n')
