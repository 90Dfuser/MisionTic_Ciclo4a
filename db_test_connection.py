import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://90franco:<password>@misiontic2022.qpubgli.mongodb.net/?retryWrites=true&w=majority"
)
db = client.test
