f = open("expmnt.txt", "r+")
f2 = open("expmnt2.txt","w")


lines = f.readlines()

for a in range(len(lines)):
	if a == 3:
		f2.write("hello world\n")
	f2.write(lines[a])

f.close()
f2.close()