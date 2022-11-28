from fastapi import FastAPI
from api_process import queryWeather, queryTemp
import uvicorn
#from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to fast weather API"}

@app.get("/cityweather/{city}")
async def getWeather(city: str):
    weatherinfo = queryWeather(city)
    temp = weatherinfo[0]
    sky = weatherinfo[2]
    return {"City: " + city + ", " + "Temperature: " + temp + ", " +  sky}


@app.get("/cmptemp/{city1}/{city2}")
async def getWeather(city1: str, city2: str):
    tempinfo1 = queryTemp(city1)
    tempinfo2 = queryTemp(city2)
    if tempinfo1 < tempinfo2:
        return {city2 + " is hotter than " + city1}
    elif tempinfo1 > tempinfo2:
        return {city1 + " is hotter than " + city2}
    else:
        return {city1 + " has the same temperature as the " + city2}


@app.get("/sorttemp/{cities}")
async def sortWeather(cities: str):
    list = cities.split(' ')
    tempdic = {}
    for city in list:
        temp = queryTemp(city)
        tempdic[temp] = city
    print(tempdic)
    dic = dict(sorted(tempdic.items()))
    str = ""
    for x in dic.values():
        str += x
        str += ' '
    return str


# @app.get("/multiply/{num1}/{num2}")
# async def multiply(num1: int, num2: int):
#     """multiply two numbers together"""

#     total = num1 * num2
#     return {"total": total}


# @app.get("/sort/{arr1}")
# async def sort(arr1: str):
#     """sort an array"""

#     res = ''.join(sorted(arr1))
#     return {"sorted arr": res}


# @app.get("/query")
# async def query():
#     """Execute a SQL query"""

#     result = querydb()
#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")