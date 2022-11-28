import requests
from bs4 import BeautifulSoup

# query temperature of the specific city
def queryTemp(city):
    list = queryWeather(city)
    tempstr = list[0]
    pos = tempstr.find("°F")
    temp = tempstr[:pos]
    return temp
    

# query weather of the specific city
def queryWeather(city):
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
    
    # formatting the string
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]
    # printing all the data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)
    return [temp, time, sky]


if __name__ == "__main__":
    city = "london"
    # list = queryWeather(city)
    # print(list)
    temp = queryTemp(city)
    print(temp)