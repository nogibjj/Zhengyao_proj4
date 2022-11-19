from fastapi import FastAPI
import uvicorn
#from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Databricks"}


@app.get("/multiply/{num1}/{num2}")
async def multiply(num1: int, num2: int):
    """multiply two numbers together"""

    total = num1 * num2
    return {"total": total}


@app.get("/sort/{arr1}")
async def sort(arr1: str):
    """sort an array"""

    res = ''.join(sorted(arr1))
    return {"sorted arr": res}


# @app.get("/query")
# async def query():
#     """Execute a SQL query"""

#     result = querydb()
#     return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")