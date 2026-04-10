a = 234
b = 6786

while True:
	print("----------",a,b,"----------")
	print("1. add")
	print("2. subtract")
	print("3. multiply")
	print("4. swap")
	print("5. exit")
	z = int(input("enter choice : "))
	if z>5 or z<0 :
		print("invalid input")
		continue
	if z==1:
		a += b
		continue
	if z==2:
		a -=b
		continue

	if z==3:
		a *=b
		continue
	if z==4:
		temp = a
		a= b
		b= temp
	if z==5 :
		break