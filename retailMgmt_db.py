from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	# con = MongoClient('mongodb+srv://sundar:sundar@cluster0.dol3j.mongodb.net/retailerManagement_db?retryWrites=true&w=majority')
	# db = con.retailerManagement_db
	# col = db.retailer_info
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/consumer_db?retryWrites=true&w=majority')
	db = con.consumer_db
	col = db.consumerbasic_info


def get_retailerInfo():
	global col
	connect_db()
	retailerInfo_fromDB = col.find({})
	return retailerInfo_fromDB


def save_retailer_info(retailer_info):
	global col
	connect_db()
	col.insert(retailer_info)
	return "saved Successfully"

def get_one_retailer_details(retailer_id):
	global col
	connect_db()
	retailerData_fromDB = col.find({"_id": ObjectId(retailer_id)})
	return retailerData_fromDB

def update_one_record(retailerId, retailerRecords):
    global col
    connect_db()    
    col.update_one({"_id": ObjectId(retailerId)}, {'$set' :{'ProgramName':retailerRecords["ProgramName"], 'Account':retailerRecords["Account"], 'Address1':retailerRecords["Address1"], 'City':retailerRecords["City"], 'State':retailerRecords["State"], 'Zip':retailerRecords["Zip"], 'Country':retailerRecords["Country"], 'Hire':retailerRecords["Hire"], 'Status':retailerRecords["Status"], 'Jobtitle':retailerRecords["Jobtitle"], 'FirstName':retailerRecords["FirstName"], 'LastName':retailerRecords["LastName"], 'Phone1':retailerRecords["Phone1"], 'PhoneExt':retailerRecords["PhoneExt"], 'Mobile1':retailerRecords["Mobile1"],     'Email1':retailerRecords["Email1"], 'Jobtitle2':retailerRecords["Jobtitle2"], 'FirstName2':retailerRecords["FirstName2"], 'LastName2':retailerRecords["LastName2"], 'Phone2':retailerRecords["Phone2"], 'Mobile2':retailerRecords["Mobile2"], 'Email2':retailerRecords["Email2"], 'Jobtitle3':retailerRecords["Jobtitle3"], 'FirstName3':retailerRecords["FirstName3"], 'LastName3':retailerRecords["LastName3"], 'Phone3':retailerRecords["Phone3"], 'Mobile3':retailerRecords["Mobile3"], 'Email3':retailerRecords["Email3"], 'Jobtitle4':retailerRecords["Jobtitle4"], 'FirstName4':retailerRecords["FirstName4"],  'LastName4':retailerRecords["LastName4"], 'Phone4':retailerRecords["Phone4"], 'Mobile4':retailerRecords["Mobile4"], 'Email4':retailerRecords["Email4"], 'ANtlAcctRepFirst':retailerRecords["ANtlAcctRepFirst"], 'ANtlAcctRepLast':retailerRecords["ANtlAcctRepLast"], 'ANtlAcctRepPhone':retailerRecords["ANtlAcctRepPhone"], 'ANtlAcctRepEmail':retailerRecords["ANtlAcctRepEmail"]} })
    return