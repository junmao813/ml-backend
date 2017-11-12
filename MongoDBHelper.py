#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from pprint import pprint
from pymongo import MongoClient,InsertOne, DeleteMany, ReplaceOne, UpdateOne
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)

# create database
db = client.test_db
# db = client['test-database']

# create collection
collection = db.test_collection
# collection = db['test-collection']

# 以上语句封装了一个JSON格式的post, 并使用insert_one()方法插入了名为posts的collection.
# 其中post中的datetime.datetime.utcnow()会被自动转换成BSON格式
# 插入成功之后会返回一个inserted_id, 对于每个document是独一无二的.
# 对于每个插入的document, mongodb会自动为其添加一个名为_id的key, 其value也为inserted_id
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}

posts = db.posts
# post_id = posts.insert_one(post).inserted_id

# 搜索
# post1 = posts.find_one({"author": "Mike"})
# print(post1)
# post1 = posts.find_one({"_id": post_id})
# print(post1)
# post1 = posts.find_one({'_id': ObjectId("5a07a674dcfba13028c7022b")})
# print(post1)

# posts.remove({"author": "Mike"})
# bulk insert
# ids = posts.insert_many([{'i': i} for i in range(10000)]).inserted_ids
# print("count of posts:", posts.count())


posts.remove({})
result = posts.bulk_write([
    DeleteMany({}),  # Remove all documents from the previous example.
    InsertOne({'_id': 1}),
    InsertOne({'_id': 2}),
    InsertOne({'_id': 3}),
    UpdateOne({'_id': 1}, {'$set': {'foo': 'bar'}}),
    UpdateOne({'_id': 4}, {'$inc': {'j': 1}}, upsert=True),
    ReplaceOne({'j': 1}, {'j': 2})])

pprint(result.bulk_api_result)

for post in posts.find():
    pprint(post)
