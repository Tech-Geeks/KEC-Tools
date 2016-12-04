#7th sem GPA calculator by Prab(https://github.com/PrabakarSundar)
class stud:
	def cgpa(self,tqm,Is,gmm,soa,cc,ooad,gmm_lab,Is_lab,ooad_lab):
		credit=0
		if((tqm=="ra" or tqm=="RA" or tqm=="rA" or tqm=="Ra") or (Is=="ra" or Is=="RA" or Is=="rA" or Is=="Ra") or (soa=="ra" or soa=="RA" or soa=="rA" or soa=="Ra") or (ooad=="ra" or ooad=="RA" or ooad=="rA" or ooad=="Ra") or (cc=="ra" or cc=="RA" or cc=="rA" or cc=="Ra") or (gmm=="ra" or gmm=="RA" or gmm=="rA" or gmm=="Ra") or (Is_lab=="ra" or Is_lab=="RA" or Is_lab=="rA" or Is_lab=="Ra") or (gmm_lab=="ra" or gmm_lab=="RA" or gmm_lab=="rA" or gmm_lab=="Ra") or (ooad=="ra" or ooad=="RA" or ooad=="rA" or ooad_lab=="Ra")):			
			print("No GPA for this semester")
		
		elif((tqm=="s" or tqm=="S" or tqm=="a" or tqm=="A" or tqm=="b" or tqm=="B" or tqm=="c" or tqm=="C" or tqm=="d" or tqm=="D" or tqm=="e" or tqm=="E") or(Is=="s" or Is=="S" or Is=="a" or Is=="A" or Is=="b" or Is=="B" or Is=="c" or Is=="C" or Is=="d" or Is=="D" or Is=="e" or Is=="E") or (gmm=="s" or gmm=="S" or gmm=="a" or gmm=="A" or gmm=="b" or gmm=="B" or gmm=="c" or gmm=="C" or gmm=="d" or gmm=="D" or gmm=="e" or gmm=="E") or (soa=="s" or soa=="S" or soa=="a" or soa=="A" or soa=="b" or soa=="B" or soa=="c" or soa=="C" or soa=="d" or soa=="D" or soa=="e" or soa=="E") or (cc=="s" or cc=="S" or cc=="a" or cc=="A" or cc=="b" or cc=="B" or cc=="c" or cc=="C" or cc=="d" or cc=="D" or cc=="e" or cc=="E") or (ooad=="s" or ooad=="S" or ooad=="a" or ooad=="A" or ooad=="b" or ooad=="B" or ooad=="c" or ooad=="C" or ooad=="d" or ooad=="D" or ooad=="e" or ooad=="E") or (Is_lab=="s" or Is_lab=="S" or Is_lab=="a" or Is_lab=="A" or Is_lab=="b" or Is_lab=="B" or Is_lab=="c" or Is_lab=="C" or Is_lab=="d" or Is_lab=="D" or Is_lab=="e" or Is_lab=="E") or (gmm_lab=="s" or gmm_lab=="S" or gmm_lab=="a" or gmm_lab=="A" or gmm_lab=="b" or gmm_lab=="B" or gmm_lab=="c" or gmm_lab=="C" or gmm_lab=="d" or gmm_lab=="D" or gmm_lab=="e" or gmm_lab=="E") or (ooad_lab=="s" or ooad_lab=="S" or ooad_lab=="a" or ooad_lab=="A" or ooad_lab=="b" or ooad_lab=="B" or ooad_lab=="c" or ooad_lab=="C" or ooad_lab=="d" or ooad_lab=="D" or ooad_lab=="e" or ooad_lab=="E")):
			if(tqm=="S" or tqm=="s"):
				credit=credit+3*10
			elif(tqm=="A" or tqm=="a"):
				credit=credit+3*9
			elif(tqm=="B" or tqm=="b"):
				credit=credit+3*8
			elif(tqm=="C" or tqm=="c"):
				credit=credit+3*7
			elif(tqm=="D" or tqm=="d"):
				credit=credit+3*6
			elif(tqm=="E" or tqm=="e"):
				credit=credit+3*5
			#print("TQM credits:",credit)	
				
			if(Is=="S" or Is=="s"):
				credit=credit+3*10
			elif(Is=="A" or Is=="a"):
				credit=credit+3*9
			elif(Is=="B" or Is=="b"):
				credit=credit+3*8
			elif(Is=="C" or Is=="c"):
				credit=credit+3*7
			elif(Is=="D" or Is=="d"):
				credit=credit+3*6
			elif(Is=="E" or Is=="e"):
				credit=credit+3*5
			#print("IS credits:",credit)
		
			if(gmm=="S" or gmm=="s"):
				credit=credit+3*10
			elif(gmm=="A" or gmm=="a"):
				credit=credit+3*9
			elif(gmm=="B" or gmm=="b"):
				credit=credit+3*8
			elif(gmm=="C" or gmm=="c"):
				credit=credit+3*7
			elif(gmm=="D" or gmm=="d"):
				credit=credit+3*6
			elif(gmm=="E" or gmm=="e"):
				credit=credit+3*5
			#print("GMM credits:",credit)	
				
			if(soa=="S" or soa=="s"):
				credit=credit+3*10
			elif(soa=="A" or soa=="a"):
				credit=credit+3*9
			elif(soa=="B" or soa=="b"):
				credit=credit+3*8
			elif(soa=="C" or soa=="c"):
				credit=credit+3*7
			elif(soa=="D" or soa=="d"):
				credit=credit+3*6
			elif(soa=="E" or soa=="e"):
				credit=credit+3*5
			#print("SOA credits:",credit)	
				
			if(ooad=="S" or ooad=="s"):
				credit=credit+3*10
			elif(ooad=="A" or ooad=="a"):
				credit=credit+3*9
			elif(ooad=="B" or ooad=="b"):
				credit=credit+3*8
			elif(ooad=="C" or ooad=="c"):
				credit=credit+3*7
			elif(ooad=="D" or ooad=="d"):
				credit=credit+3*6
			elif(ooad=="E" or ooad=="e"):
				credit=credit+3*5
			#print("OOAD credits:",credit)	
				
			if(cc=="S" or cc=="s"):
				credit=credit+3*10
			elif(cc=="A" or cc=="a"):
				credit=credit+3*9
			elif(cc=="B" or cc=="b"):
				credit=credit+3*8
			elif(cc=="C" or cc=="c"):
				credit=credit+3*7
			elif(cc=="D" or cc=="d"):
				credit=credit+3*6
			elif(cc=="E" or cc=="e"):
				credit=credit+3*5
			#print("CC credits:",credit)	
					
				
			if(Is_lab=="S" or Is_lab=="s"):
				credit=credit+1*10
			elif(Is_lab=="A" or Is_lab=="a"):
				credit=credit+1*9
			elif(Is_lab=="B" or Is_lab=="b"):
				credit=credit+1*8
			elif(Is_lab=="C" or Is_lab=="c"):
				credit=credit+1*7
			elif(Is_lab=="D" or Is_lab=="d"):
				credit=credit+1*6
			elif(Is_lab=="E" or Is_lab=="e"):
				credit=credit+1*5
				
				
			if(gmm_lab=="S" or gmm_lab=="s"):
				credit=credit+1*10
			elif(gmm_lab=="A" or gmm_lab=="a"):
				credit=credit+1*9
			elif(gmm_lab=="B" or gmm_lab=="b"):
				credit=credit+1*8
			elif(gmm_lab=="C" or gmm_lab=="c"):
				credit=credit+1*7
			elif(gmm_lab=="D" or gmm_lab=="d"):
				credit=credit+1*6
			elif(gmm_lab=="E" or gmm_lab=="e"):
				credit=credit+1*5
			
				
			if(ooad_lab=="S" or ooad_lab=="s"):
				credit=credit+1*10
			elif(ooad_lab=="A" or ooad_lab=="a"):
				credit=credit+1*9
			elif(ooad_lab=="B" or ooad_lab=="b"):
				credit=credit+1*8
			elif(ooad_lab=="C" or ooad_lab=="c"):
				credit=credit+1*7
			elif(ooad_lab=="D" or ooad_lab=="d"):
				credit=credit+1*6
			elif(ooad_lab=="E" or ooad_lab=="e"):
				credit=credit+1*5
		else:
			print("Oops!invalid Grade.select one of these Grades(S,A,B,C,D,E,RA)")
		#print("Total credits:",credit)
		print("your current semester gpa:",credit/21)

			
	
obj1=stud()
print("Enter your grades")
tqm=input("TQM:")
Is=input("IS:")
gmm=input("GMM:")
soa=input("SOA:")
cc=input("CC:")
ooad=input("OOAD:")
gmm_lab=input("GMM Lab:")
Is_lab=input("IS Lab:")
ooad_lab=input("OOAD Lab:")
obj1.cgpa(tqm,Is,gmm,soa,cc,ooad,gmm_lab,Is_lab,ooad_lab)
