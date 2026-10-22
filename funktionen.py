def berechne_bmi(gewicht,groesse):
	bmi=round(gewicht/(groesse/100)**2,2)
	

	if bmi < 18.5:
		print("untergewcht")
	elif bmi > 25:
		print("Übergewicht")
	else:  
		print("Normalgewicht")
	return bmi

print(berechne_bmi(85,195))



