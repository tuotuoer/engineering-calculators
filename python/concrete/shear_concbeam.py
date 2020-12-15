
print "\n Conc Beam Design for Shear \n"

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
	

# Shear capacity of concrete

b = input("The width of the conc section(in)")

d = input("The effective depth of the section(in)")

fc = input("The compressive strength of conc(psi)")

fy = input(" The yeild strength of steel reinf(psi)")

Vc = 2.0*b*d*1.0*(fc**(0.5))

output("The nominal shear capacity of conc (psi)", Vc)

Vc_factored = 0.75*Vc
lowerlimit = Vc_factored/2.0/1000.0

output("The lowerlimit of the concrete section w/ min. shear reinf.(kips)", lowerlimit)

upperlimit = Vc_factored/1000.0
output("The upperlimit of the concrete section w/ min. shear reinf.(kips)", upperlimit)

Vu = input("Applied factored shear force(kips)")

if Vu < lowerlimit :
	print " The concrete section is adequate to carry shear without any shear reinf."
	
elif Vu>= lowerlimit and Vu<= upperlimit:
	print " This concrete section require a minimum shear reinf."
	Av_min = 50.0*b*12.0/fy
	output(" Mininmum shear reinf. area/ft = ", Av_min)
else :
	print "\n We need to calculate the needed nominal shear capacity of stirrups."
	Vs_factored = Vu-upperlimit
	Vs = Vs_factored/0.75
	output(" The needed nominal shear capacity of stirrups (kips)", Vs)
	# Check if we need to increase the size of conc beam
	Vs_max = 8*(fc**(0.5))*b*d/1000.0
	Vs_spacingcheck = 4*(fc**(0.5))*b*d/1000.0
	
	if Vs > Vs_max:
		print "\n The size of the concrete section must be increased!"
		
	else:
		print " The size of the section does not need to be increased."
		Av_needed = Vs*1000.0*12.0/fy/d
		output(" The minimum shear reinf. area(in^2)/ft of this section" , Av_needed)
		
		if Vs <= Vs_spacingcheck :
			s = min(d/2.0, 24.0)
			output(" The maximum stirrup spacing(in)", s)
		else:
			s = min(d/4.0, 12.0)
			output(" The maximum stirrup spacing(in)", s)
			
			

	




