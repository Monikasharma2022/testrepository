import pymongo
client = pymongo.MongoClient("mongodb+srv://monika:SKk57bzUXX6rSvV@cluster0.y431wr7.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "mane": "monika",
    "email": "monika47456@gmail.com",
    "sirname": "Gaur"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

