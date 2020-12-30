b = 0   # no. of reviews initially 0
c = 0   # sum of all rating initially 0
# infinite loop
while True:
	# take input
	a = int(input("\n Give your Rating under 1 to 5 : ")) 
	# validate input
	if a in range(1, 6):
		b += 1	              # increment reviews
		d = (a + c)/b         #  calculate rating 
		# print rating and reviews
		print("\n Rating☆ : ", d,"\t  reviews : ", b)
		# sum of all rating
		c += a
	# Invalide input
	else:
		print("\n please rate under 1 to 5")
