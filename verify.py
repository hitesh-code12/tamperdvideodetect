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

import pymongo

originalData = coll.find({}).sort('keyIndex', pymongo.ASCENDING)
verificationData = coll1.find({}).sort('keyIndex', pymongo.ASCENDING)

data=coll1.find({"countBlock":1})
for i in data:
	countOriginal = i['count']

data=coll.find({"countBlock":1})
for i in data:
	countVerification = i['count']


flag=0
if(countOriginal != countVerification ):
	print('The video is Tampered, Please report!!! ')
	exit(0)

try:
	for i in range(1,count+1):
		if(originalData[i]['key'] != verificationData [i]['key']):
			flag=1
			print(i)
			if (flag == 1):
				print('Verification Failed on frame No:' + str(i))
			break
	

	else:
		print('Congratulations!!!!!!!!!Video is Verified and Untampered')
except:
	print("The video is Tampered, Please report!!!")
	













