# Run this Python code from your terminal: Due to security reasons, we don't execute code directly. Stay safe.

from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import requests


def getDataFromUrl(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    myHtmlData = getDataFromUrl('https://www.mygov.in/covid-19')
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    stateName = list()
    confirmed = list()
    active = list()
    discharged = list()
    deaths = list()
    vaccination = list()
    for i in range(36):
        stateName.append(soup.find_all(
            "span", {"class": "st_name"})[i].get_text())
        dataList = soup.find_all("div", {"class": "st_all_counts"})[
            i].get_text().split('\n')
        confirmed.append(dataList[1].split(' ')[1])
        active.append(dataList[2].split(' ')[1])
        discharged.append(dataList[3].split(' ')[1])
        deaths.append(dataList[4].split(' ')[1])
        vaccination.append(dataList[6].split(' ')[1])
    dataDict = {
        'S.No': list(range(1, 37)),
        'State': stateName,
        'Confirmed': confirmed,
        'Active': active,
        'Discharged': discharged,
        'Deaths': deaths,
        'Vaccinations': vaccination,
    }
    print('\n\n-----------------------------------COVID-19 Data Fetcher-----------------------------------\n')
    while(1):
        print('Enter 1 to save data in a CSV file:')
        print('Enter 2 to display data:')
        print('Enter 0 to exit:')
        c = int(input('\nEnter your choice: '))
        if(c == 0):
            break
        elif(c == 1):
            fileName = input('Enter name of the file: ')
            df = pd.DataFrame.from_dict(dataDict)
            df.to_csv(fileName, index=False, header=True)
        elif(c == 2):
            print('\n')
            print(tabulate(dataDict, headers='keys', tablefmt='psql'))
        else:
            print('\nInvalid Choice')
        print('\n')
