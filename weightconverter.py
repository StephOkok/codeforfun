weight=float(input("Enter Weight: ")
unit=input("Enter unit in Lbs(L) or Kgs (K): ")
if unit.upper()=='L':
	convert= weight*0.45
	print(f"The weight is {convert} kilos")
else:
		convert=weight/0.45
		print(f"The weight is {convert} pounds")
