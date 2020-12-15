s1 = input("The spacing betw horizontal anchors (in)")

n1 = input("number of anchors in a row")

s2 = input("The spacing betw vertical anchors (in)")

n2 = input(" number of anchors in a column")

if s1<3*h_ef and s2<3*h_ef:

	a = ((n1-1)*s1+3*h_ef)
	b = ((n2-1)*s2+3*h_ef)
	
elif s1<3*h_ef and s2>= 3*h_ef:

	a = ((n1-1)*s1+3*h_ef)
	b = n2
	
elif s2<3*h_ef and s1>= 3*h_ef:

	b = ((n2-1)*s2+3*h_ef)
	a = n1
	
else:
		a = n1*3*h_ef
		b = n2*3*h_ef
		
A_Nc = a*b

output("The projected area of failured surface of the group anchors", A_Nc)