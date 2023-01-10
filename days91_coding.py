angka = int(input("masukkan angka : "))

for i in range (1,angka) :
	if i > 1 :
		for n in range (2,i) :
			if i % n == 0:
				break
		else :
			print (i)