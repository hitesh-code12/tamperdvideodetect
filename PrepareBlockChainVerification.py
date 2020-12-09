import hashlib

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['videoverification']
coll = db['videoKeysForVerification']


str1 = "PROUD TO BE INDIAN"
result = hashlib.sha256(str1)
coll.insert({"keyIndex":0,"fileName":"firstKey","key":result.hexdigest()})


data=coll.find({"countBlock":1})
for i in data:
	count = i['count']

import base64

pKeyData=coll.find({"keyIndex":0})
for j in pKeyData:
	p_key=str( j["key"] )


for i in range(1,count+1):
	fileName = "image" + str(i) + ".jpg" 
	with open(  "imagesVerification/" + fileName , "rb" ) as imageFile:
		str1 = base64.b64encode(imageFile.read())
    		result = hashlib.sha256 ( p_key + hashlib.sha256( str1 ).hexdigest() )
		coll.insert({"keyIndex":i,"fileName":fileName ,"key":result.hexdigest()})
	p_key = result.hexdigest()

coll1 = db['videoKeys']
