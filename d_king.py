import random
import time
import csv


#data = ['a','b','c','d','e','f','g','h','i']
#new_data = []
#len_data = len(data)
timestamp = []
normal_email = []
jumlah_key = []
platform = []
username = []
vking = []
dking = []
firstname = []
lastname = []
address = []
zip_code = []
phone_number = []
paypal_email = []
shipping = []
setuju = []
saran = []
data = []
pilih_dking = []

print('Memulai Raflle.......')


#with open("responded_fix.csv") as csv_file:
with open("gmk.csv") as csv_file:
	data_csv = csv.reader(csv_file, delimiter=",")	

	for row in data_csv:
		data_timestamp = row[0]
		timestamp.append(data_timestamp)

		data_normal_email = row[1]
		normal_email.append(data_normal_email)
	
		data_jumlah_key = row[2]
		jumlah_key.append(data_jumlah_key)
		
		data_platform = row[3]
		platform.append(data_platform)

		data_username = row[4]
		username.append(data_username)

		data_vking = row[5]
		vking.append(data_vking)

		data_dking = row[6]
		dking.append(data_dking)	

		data_firstname = row[7]
		firstname.append(data_firstname)

		data_lastname = row[8]
		lastname.append(data_lastname)

		data_address = row[9]
		address.append(data_address)

		data_zip_code = row[10]
		zip_code.append(data_zip_code)

		data_phone_number = row[11]
		phone_number.append(data_phone_number)

		data_paypal_email = row[12]
		paypal_email.append(data_paypal_email)

		data_shipping = row[13]
		shipping.append(data_shipping)

		data_setuju = row[14]
		setuju.append(data_setuju)

		data_saran = row[15]
		saran.append(data_saran)


		
	for z in range(1,len(username)):
		data_full = timestamp[z],normal_email[z],jumlah_key[z],platform[z],username[z],vking[z],dking[z],firstname[z],lastname[z],address[z],zip_code[z],phone_number[z],paypal_email[z],shipping[z],setuju[z],saran[z]
		data.append(data_full)



	for datas in range(0, len(data)):
		loop = data[datas]
		if(loop[6]=="1"):
			testing_data = loop[0],loop[1],loop[2],loop[3],loop[4],loop[5],loop[6],loop[7],loop[8],loop[9],loop[10],loop[11],loop[12],loop[13],loop[14],loop[15]
			pilih_dking.append(testing_data)
	
	print(pilih_dking)
	print("=====================")


	for datas in range(0, len(pilih_dking)):
		random.shuffle(pilih_dking)
		print(pilih_dking)
		time.sleep(3)
		print("\n Eliminate....")
		pilih_dking.pop(-1)

		if len(pilih_dking) == 1:
			print("\n==== Winner Rafle Vking ====")
			for x in pilih_dking:
				print("Email Adress:",x[1])
				print("Jumlah:", x[2])
				print("Platform:",x[3])
				print("Username:",x[4])
				print("Vking:",x[5])
				print('Dking',x[6])
				print("FullName:",x[7]+x[8])
				print("Address",x[9])
				print("ZipCode:",x[10])
				print("number_phone:",x[11])
				print("Paypal Email:", x[12])
				print("Shipping:",x[13])
				print("Undestand:",x[14])
				print("Suggestion:",x[15])
				print("")
			break
