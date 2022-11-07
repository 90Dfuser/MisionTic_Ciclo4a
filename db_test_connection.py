import pymongo
import certifi
ca = certifi.where()

client = pymongo.MongoClient(
    "mongodb+srv://@misiontic2022.qpubgli.mongodb.net/?retryWrites=true&w=majority",
    tlsCAFile=ca
)
db = client.test
print(db)

data_base = client['academic_db']
print(data_base.list_collection_names())

table = data_base.get_collection('table')
all_tables = table.find({})
