from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import retailMgmt_db

app = Flask(__name__)

app.secret_key = "98app13oct87nxs2020rma6597"

@app.route('/')
def index():
	#get all data from DB
	retailer_info = retailMgmt_db.get_retailerInfo()
	rtlrInfo_list = []
	for r in retailer_info:
		rtlrInfo_list.append(r)
	return render_template('retailer_mgmt.html', rtlrList = rtlrInfo_list )


def setData():
	#Empty List
	retailerRecords = {}
	#request data from UI
	ProgramName = request.form['pName']
	Account = request.form['accN']
	Address1 = request.form['addrs']
	City = request.form['city']
	State =  request.form['state']
	Zip = request.form['zCode']
	Country = request.form['cntry']
	Hire = request.form['strDate']
	Status = request.form['status']

	Jobtitle =  request.form['jobTitle']
	FirstName = request.form['fName']
	LastName = request.form['lName']
	Phone1 = request.form['phone']
	PhoneExt = request.form['ext']
	Mobile1 =  request.form['mobile']
	Email1 = request.form['email']
	
	Jobtitle2 =  request.form['jobTitle2']
	FirstName2 = request.form['fName2']
	LastName2 = request.form['lName2']
	Phone2 = request.form['phone2']
	Mobile2 =  request.form['mobile2']
	Email2 = request.form['email2']

	"""Jobtitle3 =  request.form['jobTitle3']
	FirstName3 = request.form['fName3']
	LastName3 = request.form['lName3']
	Phone3 = request.form['phone3']
	Mobile3 =  request.form['mobile3']
	Email3 = request.form['email3']

	Jobtitle4 =  request.form['jobTitle4']
	FirstName4 = request.form['fName4']
	LastName4 = request.form['lName4']
	Phone4 = request.form['phone4']
	Mobile4 =  request.form['mobile4']
	Email4 = request.form['email4']

	ANtlAcctRepFirst = request.form['NARepfName']
	ANtlAcctRepLast = request.form['NARepLName']
	ANtlAcctRepPhone = request.form['NARepMobile']
	ANtlAcctRepEmail = request.form['NARepMail']"""

	#set data to the Empty list
	retailerRecords["ProgramName"]=ProgramName 
	retailerRecords["Account"]=Account
	retailerRecords["Address1"]=Address1
	retailerRecords["City"]=City
	retailerRecords["State"]=State
	retailerRecords["Zip"]=Zip 
	retailerRecords["Country"]=Country
	retailerRecords["Hire"]=Hire
	retailerRecords["Status"]=Status

	retailerRecords["Jobtitle"]=Jobtitle
	retailerRecords["FirstName"]=FirstName 
	retailerRecords["LastName"]=LastName
	retailerRecords["Phone1"]=Phone1
	retailerRecords["PhoneExt"]=PhoneExt
	retailerRecords["Mobile1"]=Mobile1
	retailerRecords["Email1"]=Email1

	retailerRecords["Jobtitle2"]=Jobtitle2
	retailerRecords["FirstName2"]=FirstName2
	retailerRecords["LastName2"]=LastName2
	retailerRecords["Phone2"]=Phone2
	retailerRecords["Mobile2"]=Mobile2
	retailerRecords["Email2"]=Email2
	
	"""retailerRecords["Jobtitle3"]=Jobtitle3
	retailerRecords["FirstName3"]=FirstName3
	retailerRecords["LastName3"]=LastName3
	retailerRecords["Phone3"]=Phone3
	retailerRecords["Mobile3"]=Mobile3
	retailerRecords["Email3"]=Email3

	retailerRecords["Jobtitle4"]=Jobtitle4
	retailerRecords["FirstName4"]=FirstName4
	retailerRecords["LastName4"]=LastName4
	retailerRecords["Phone4"]=Phone4
	retailerRecords["Mobile4"]=Mobile4
	retailerRecords["Email4"]=Email4

	retailerRecords["ANtlAcctRepFirst"]=ANtlAcctRepFirst
	retailerRecords["ANtlAcctRepLast"]=ANtlAcctRepLast
	retailerRecords["ANtlAcctRepPhone"]=ANtlAcctRepPhone
	retailerRecords["ANtlAcctRepEmail"]=ANtlAcctRepEmail"""

	return retailerRecords


@app.route("/", methods=['POST'])
def update_retailerRecords():	
	retailerRecords = setData()
	#print records in cmd
	print(retailerRecords)
	retailMgmt_db.save_retailer_info(retailerRecords)
	return redirect(url_for('index'))


@app.route("/update", methods=['POST'])
def update_oneRetailer_Records():
	retailerRecords = setData()
	#print records in cmd
	print(retailerRecords)
	print(request.form['rid'])
	#send to db
	retailerId=request.form['rid']
	#update_emp = emp_db.get_one_emplyoee_details(empid)
	#print(update_emp)
	retailMgmt_db.update_one_record(retailerId, retailerRecords)
	return redirect(url_for('index'))



@app.route("/edit/<retailer_id>", methods=['POST'])
def edit_record(retailer_id):
	retailer_one_record = retailMgmt_db.get_one_retailer_details(retailer_id)
	return render_template('edit_record.html', retailer_list = retailer_one_record)






if(__name__) == '__main__':
	app.run(debug=True)