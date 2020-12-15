
print "\n Neutral axis of a cracked conc beam section \n"

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
	
	
b = input("The width of the conc section(in)")

d = input("The effective depth of the section(in)")

size = input("size of rebars")

number = input("Number of tension rebars")

dia = size/8
Area = 3.1415*(dia**2.0)/4.0
As = number*Area

output("Total area of reinf (in^2)", As)

rho = As/b/d

output("Reinf. ratio rho ", rho)

fc = input("The compressive strength of conc(psi)")

wc = input("The unit weight of conc(pcf)")

Ec = wc**1.5*33*fc**(0.5)/1000.0

output("Modulus of Elasticity of conc (ksi)", Ec)

Es = input("Modulus of Elasticity of steel (ksi)")

n = Es/Ec

output("Modular ratio n", n)

x = rho*n

output("rho*n" , x)

k = (2.0*x+(x**2.0))**0.5 - x

output("Neutrual axis depth factor", k)

NA = k*d

output("Neutral axis is located at (in)", NA)




