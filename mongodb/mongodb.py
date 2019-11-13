import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client['pythonbase']

collection = db['students']

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

# result = collection.insert_many([student, student2])
result = collection.insert_one(student)

print(result.inserted_id)

result = collection.find_one({'name': 'Mike'})

print(type(result))
print(result)

