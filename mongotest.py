import pymongo
client = pymongo.MongoClient("mongodb+srv://vinaypritwani19:deepside@cluster0.snsy70w.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "emailid":"sudhanshu@ineuron,ai",
    "surname":"kumar"
}

d = {
    "name":"sudhanshu",
    "emailid":"sudhanshu@ineuron,ai",
    "surname":"kumar"
}
d = {
    "name":"sudhanshu",
    "emailid":"sudhanshu@ineuron,ai",
    "surname":"kumar"
}
d = {
    "name":"sudhanshu",
    "emailid":"sudhanshu@ineuron,ai",
    "surname":"kumar"
}
d = {
    "name":"sudhanshu",
    "emailid":"sudhanshu@ineuron,ai",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
