while True:
	a = list(raw_input("Give text:"))
	for i in range (len(a)):
		b = ord(a[i])
		if b > 126 or b < 32:
			e = 0
			break
		else:
			e = 1
			if(b >= 65 and b <= 90 ):
				b += 13
				if b > 90:
					b -= 26
			if (b >= 97 and b <= 122):
				b += 13
				if b > 122:
					b -= 26
		a[i] = chr(b)
	if e == 1:
		print "Show the text in ROT13: " + "".join(a)
	else:
		print "The system doesn't understand"