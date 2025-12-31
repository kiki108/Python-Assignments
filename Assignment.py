def taxes():
	print("Filing Statuses")
	print("1 for married filing jointly or qualified widow or widower")
	print("2 for married filing separately")
	print("3 for head of household")
	filing_status = int(input("select a number: "))
	
	income = float(input("Input your income: "))
	
	if filing_status == 0:
		tRate1, tRate2, tRate3, tRate4, tRate5 = 8350, 33950, 82250, 171550, 372950
	elif filing_status == 1:
		tRate1, tRate2, tRate3, tRate4, tRate5 = 16700, 67900, 137050, 208850, 372950
	elif filing_status == 2:
		tRate1, tRate2, tRate3, tRate4, tRate5 = 8350, 33950, 68525, 104425, 186475
	else:
		tRate1, tRate2, tRate3, tRate4, tRate5 = 11950, 45500, 117450, 190200, 372950
	
	tax = 0.0
	
	if income <= tRate1:
		tax = income *0.10
	elif income <= tRate2:
	   tax = (tRate1 * 0.10) + ((income - tRate1) * 0.15)
	elif income <= tRate3:
		tax = (tRate1 * 0.10) + ((tRate2 - tRate1) * 0.15) + ((income - tRate2) * 0.25)
	elif income <= tRate4:
		tax = (tRate1 * 0.10) + ((tRate2 - tRate1) * 0.15) + ((tRate3 - tRate2) * 0.25) + ((income - tRate3) * 0.28)
	elif income <= tRate5:
		tax = (tRate1 * 0.10) + ((tRate2 - tRate1) * 0.15) + ((tRate3 - tRate2) * 0.25) + ((tRate4 - tRate3) * 0.28) + ((income - tRate4) * 0.33)
	else:
		tax = (tRate1 * 0.10) + ((tRate2 - tRate1) * 0.15) + ((tRate3 - tRate2) * 0.25) + ((tRate4 - tRate3) * 0.28) + ((tRate5 - tRate4) * 0.33) + ((income - tRate5) * 0.35)
	
	print(f"Your personal income tax is ${tax:.2f}")

taxes()