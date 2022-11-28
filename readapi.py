# import urllib library
from urllib.request import urlopen
# import json
import json

# importing the library
import requests
from bs4 import BeautifulSoup

def geteventsasjson(days, attribute, keyword):
    # store the URL in url as 
    # parameter for urlopen
    if days == -1:
        url = "https://calendar.duke.edu/events/index.json?&future_days=5&feed_type=simple"
    else:
        url = "https://calendar.duke.edu/events/index.json?&future_days="+str(days)+"&feed_type=simple"
    # store the response of URL
    response = urlopen(url)
    # storing the JSON response 
    # from url in data
    dict = json.loads(response.read())
    procdict = dict["events"]

    #if no need to search attribute, return all
    if attribute == "":
        return procdict
    #else return target events
    else:
        result = []
        for dic in procdict:
            if keyword in dic[attribute]:
                print("+++++++++++++++++++++add one++++++++++++++++++++++")
                result.append(dic)
        return result



def getweather():
    # enter city name
    city = "durham"
    # create url
    url = "https://www.google.com/search?q="+"weather"+city
    # requests instance
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    # list having all div tags having particular class name
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    # particular list with required data
    strd = listdiv[5].text
    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]
    # printing all the data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)
    return "Temperature is" + temp + "," + "Time: " + time + "," + "Sky Description: " + sky

if __name__ == "__main__":
    geteventsasjson()