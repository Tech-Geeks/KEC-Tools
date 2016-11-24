#Script by Naveen K.(https://github.com/FR0ST1N)
#Change the Link and Number Range in Loop Based on Your Need.
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import urllib
import re
import csv

web_name = 'http://coe.kongu.edu/caout.php?regno=13csl'
with open('sem7.csv', 'w') as csvfile:
	fieldnames = ['Name','Roll', 'Object Oriented Analysis and Design', 'Graphics and Multimedia', 'Information Security', 'Service Oriented Architecture', 'Cloud Computing', 'Case Tools Laboratory', 'Graphics and Multimedia Laboratory', 'Network Security Laboratory']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for x in range(276,277+1):
		all_marks = []
		if x <= 9:
			web_name1 = web_name + str(0) + str(0) + str(x)
		elif x >= 10 and x <= 99:
			web_name1 = web_name + str(0) + str(x)
		else:
			web_name1 = web_name + str(x)
		print web_name1
		Soup_URL = urllib.urlopen(web_name1).read()
		soup = BeautifulSoup(Soup_URL,'html.parser')
		sum = soup.find('th',{'align': 'left' }).getText().replace('Name : ','')
		print sum
		Venus = soup.find_all('table',{'cellspacing': '0' })
		mytr = Venus[1].find_all('tr')
		for i,row in enumerate(mytr):
			 if i:
				all_marks.append(row.find_all('th')[0].getText())
		writer.writerow({'Name': sum,'Roll': '13CSR'+str(x),'Object Oriented Analysis and Design': all_marks[0],'Graphics and Multimedia':all_marks[1], 'Information Security':all_marks[2], 'Service Oriented Architecture':all_marks[3], 'Cloud Computing':all_marks[4], 'Case Tools Laboratory':all_marks[5], 'Graphics and Multimedia Laboratory':all_marks[6], 'Network Security Laboratory':all_marks[7]})