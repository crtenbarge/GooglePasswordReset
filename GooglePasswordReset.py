##Requires CSV File with the following columns

## Row 0 = Firstname
## Row 1 = Lastname
## Row 2 = Email
## Row 3 = Password
## Row 4 = School 
## Row 5 = Grade

##Lets filter by school and grade. If this is not desired, uncomment line 44 and comment line 43 
school = 'SCHOOL NAME'
grade = 'GRADE'


x=0
import csv
import os
dirpath = os.path.dirname(os.path.realpath(__file__))

##Remove stray files
bashCommandX = 'rm '+dirpath+'/skyward.csv '+dirpath+'/skyward.xls '+dirpath+'/skyward.xml'
os.system(bashCommandX)

##Only necessary when converting from XLS to CSV. Requires LibreOffice and OS X
bashcommandZ = 'mv '+dirpath+'/*skyread*.xls '+dirpath+'/skyward.xls'
os.system(bashcommandZ)
bashCommandA = '/Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to xml '+dirpath+'/skyward.xls'
os.system(bashCommandA)
bashCommandB = '/Applications/LibreOffice.app/Contents/MacOS/soffice -headless --convert-to csv '+dirpath+'/skyward.xml'
os.system(bashCommandB)
bashCommandY = 'mv '+dirpath+'/skyward.csv '+dirpath+'/skyward.csv'
os.system(bashCommandY)


##Moves the CSV file through GAM

with open('skyward.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	x = x+1;
    	if x==1:
    		print 'lets get this party started!'
    	elif row[4] == school and row[5] == grade:
##		else
				bashCommand1 = 'python ~/gam/gam.py update user %s firstname "%s" lastname "%s" password %s000' % (row[2],row[0],row[1],row[3])
				os.system(bashCommand1)
				print 'Done: %s %s\'s password was reset' % (row[0], row[1])
    print 'Sync complete'
