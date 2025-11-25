from fastapi import FastAPI
# import psycopg2
import pandas as pd

# create FastAPI object
app = FastAPI()


# def getConnection():
#     # create connection
#     conn = psycopg2.connect(
#         dbname="neondb", user="neondb_owner", password="npg_sLfVg8iW4EwO",
#         host="ep-steep-water-a102fmjl-pooler.ap-southeast-1.aws.neon.tech",
#     )

#     return conn


@app.get('/')
async def getWelcome():
    return {
        "msg": "sample-fastapi-pg"
    }

# endpoint untuk menampilkan data csv
@app.get('/data')
def getData():
    df = pd.read_csv('data.csv')

    return df.to_dict(orient="records")

@app.get('/data/{lokasi}')
def getData(lokasi: str):
    # membaca data csv
    df = pd.read_csv('data.csv')

    # filter
    result = df.loc[df.lokasi == lokasi]

    # response
    return result.to_dict(orient="records")

#     @app.get(...)
#     async def getProfiles():
#         pass


#     @app.get(...)
#     async def getProfileById():
#         pass


#     @app.post(...)
#     async def createProfile():
#         pass


#     @app.patch(...)
#     async def updateProfile():
#         pass


#     @app.delete(...)
#     async def deleteProfile():
#         pass
