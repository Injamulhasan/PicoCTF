#!/usr/bin/env python3

import string
flag=[]

with open("message.txt") as flip:

	contents = flip.read()
	nums = [int(val) for val in contents.split()]

	for num in nums:
		modulus = num % 37

		if modulus in range(26):
			flag.append(string.ascii_uppercase[modulus])
		elif modulus in range(26,36):
			flag.append(string.digits[modulus -26])
		else:
			flag.append("_")
print("picoCTF{%s}" % "".join(flag))
print("picoCTF{" + "".join(flag) + "}")