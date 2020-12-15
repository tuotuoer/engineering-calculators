
print "\n Soil Pressure Distribution \n"

def input(nonmenclature):
	print "  "
	print nonmenclature
	parameter = raw_input(" = ")
	parameter = float(parameter)
	return parameter

def output(nonmenclature2, result):
	print "  "
	print nonmenclature2
	print " = %f" %result

	
L = input("Length of footing (ft)")	
B = input("width of footing (ft)")
P = input("Axial load (kips)")

M = input("Bending moment (Kip-ft)")

h = input("Thickness of footing (in)")

W = 145*L*B*h/1000.0/12.0

output("The weight of the footing (kip)”，W)

Pt = P + W

output("The total load on the soil (kip)", Pt)

e = M/Pt

output("The equivalent eccentricity of the total load", e)

if e <= L/6:
	print " The eccentricity is located within middle third of the base"
	q_max = (Pt/B/L)*(1+6*e/L)
	
else:
	print " The eccentricity is located outside of middle third of the base"
	e_prime = (L/2.0)-e
	q_max = 2*Pt/3.0/B/e_prime
	
output("The max. soil pressure", q_max)


	


 
