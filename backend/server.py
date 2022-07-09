from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://Python:{password}@cluster0.mdtopao.mongodb.net/?retryWrites=true&w=majority"

client =  MongoClient(connection_string)

dbs = client.list_database_names()

test_db = client.test

collections = test_db.list_collection_names()

# Insert a data to database
def insert_test_doc():
    collection = test_db.test
    test_document = {
        "name": "Rokas",
        "type": "Test"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    print(inserted_id)

production = client.prduction
person_collection = production.person_collection

# Create a doccument
def create_documents():
    first_names = ["Rokas", "Morta", "Jonas", "Simona"]
    last_names = ["Norvilis", "Macijauskaite", "Kederys", "Juozapaitytė"]
    ages = [22, 21, 25, 30]

    docs = []

# Merge using loop
    for first_name, last_name, age in zip(first_names, last_names, ages):
        doc = {"first_name": first_name, "last_name": last_name, "age": age}
        docs.append(doc)

    person_collection.insert_many(docs)

# Formater
printer = pprint.PrettyPrinter()

# Find all peoples
def find_all_people():
    people = person_collection.find()

    for person in people:
        printer.pprint(person)

# Look specific doccument  based on the field value

def find_rokas():
    rokas = person_collection.find_one({"first_name": "Rokas"})
    printer.pprint(rokas)

# count all people

def count_all_people():
    count = person_collection.count_documents(filter={})
    print("Number of people", count)

# Find by ID

def get_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)
    person = person_collection.find_one({"_id": _id})
    printer.pprint(person)

# Get a range

def get_age_range(min_age, max_age):
    query = {"$and": [
        {"age": {"$gte": min_age}},
        {"age": {"$lte": max_age}}
    ]}
    
    people = person_collection.find(query).sort("age")
    for person in people:
        printer.pprint(person)

# Projection to get not all info just some of it

def project_columns():
    columns  = {"_id": 0, "first_name": 1, "last_name": 1}
    people = person_collection.find({}, columns)
    for person in people:
        printer.pprint(person)

# Updating documents

def update_person_by_id(person_id):
    from bson.objectid import ObjectId

    _id = ObjectId(person_id)

    all_updates = {
        "$set": {"new_field": True},
        "$inc": {"age": 1},
        "$rename": {"first_name": "first", "last_name": "last"}
    }
    person_collection.update_one({"_id": _id}, all_updates)

# Replace doccument

def replace_one(person_id):
        from bson.objectid import ObjectId
        _id = ObjectId(person_id)

        new_doc = {
            "first_name": "new first name",
            "last_name": "new last name",
            "age": 22
        }

        person_collection.replace_one({"_id": _id}, new_doc)

# Delete doccuments

def delete_doc_by_id(person_id):
    from bson.objectid import ObjectId
    _id = ObjectId(person_id)
    person_collection.delete_one({"_id": _id})

delete_doc_by_id("62c67e7af33ac42408403b68")    

# Relationships to join

address = {
    "_id": "61c67e7af33ac42402403b69",
    "street": "Vingio g.",
    "number": 14,
    "city": "Vilnius",
    "country": "Lithuania",
    "zip": "56733",
}

# 1 method

def add_address_embed(person_id, address):
    from bson.objectid import ObjectId
    _id = ObjectId(person_id)

    person_collection.update_one({"_id": _id}, {"$addToSet": {"addresses": address}})

# 2 method

def add_address_relationships(person_id, address):
    from bson.objectid import ObjectId
    _id = ObjectId(person_id)

    address = address.copy()
    address["owner_id"] = person_id

    address_collection = production.address 
    address_collection.insert_one(address) 


