import csv

# What Ya Readin' Boi?
inputfile = open('Prod195_1111_ni_sample.dat', 'r')

# Company Record Writer
outputfile = open('companyRecord.csv', 'wb')
csv_writer = csv.writer(outputfile)
csv_writer.writerow(["companyNumber","recordType","companyStatus","numberOfOfficers","companyNameLenght","companyName"])

# Person Record Writer
personfile = open('personRecord.csv', 'wb')
person_writer = csv.writer(personfile)
person_writer.writerow(["companyNumber","recordType","appDateOrigin","appointmentType","corporateIndicator","appointmentDate",
						"resignationDate","personPostcode","partialDateOfBirth","fullDateOfBirth","variableData"])

# Skip Header Identifier
next(inputfile)

#Loop That Thang
for index, row in enumerate(inputfile):
	# Where Ya @ Boi?
	if (index-1)%10000 == 0:
		print str(index-1) + ' ROWS COMPLETED! YOUPIDOU!'

	# Magic Happens Here
	try :
		# Company Record Do This
		if row[8] == '1':
			companyNumber = row[0:8]
			recordType = row[8]
			companyStatus = row[9]
			numberOfOfficers = row[32:36]
			companyNameLenght = row[36:40]
			endOfInput = 40 + int(companyNameLenght)
			companyName = row[40:endOfInput]
			csv_writer.writerow([companyNumber,recordType,companyStatus,numberOfOfficers,companyNameLenght,companyName])
		# End Of File Identifier
		elif row[0:8] == '99999999':
			break
		#Person Record Do That
		else:
			companyNumber = row[0:8]
			recordType = row[8]
			appDateOrigin = row[9]
			appointmentType = row[10:12]
			personNumber = row[12:24]
			corporateIndicator = row[24]
			appointmentDate = row[32:40]
			resignationDate = row[40:48]
			personPostcode = row[48:56]
			partialDateOfBirth = row[56:64]
			fullDateOfBirth = row[64:72]
			variableDataLenght = row[72:76]
			endOfInput = 76 + int(variableDataLenght)
			variableData = row[76:endOfInput]
			person_writer.writerow([companyNumber,recordType,appDateOrigin,appointmentType,corporateIndicator,appointmentDate,
									resignationDate,personPostcode,partialDateOfBirth,fullDateOfBirth,variableData])
	# Error Watch
	except IndexError:
		print "GAME OVER! ROW " + str(index+1) + " KILLED YOU!" 
		