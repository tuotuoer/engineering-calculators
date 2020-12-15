# Analysis procedure for a singly reinf conc beam
print "  "
print " Given section properties, the analysis can be generalized..."
print "  "
size = raw_input(" The size of rebars = ")
print "  "
size = float(size)

number = raw_input(" The number of rebars = ")
print "  "
number = float(number)

#Calculate diameter(in) of the rebar 
dia = size/8

area = (3.1415*(dia*dia))/4
As = area*number

print " The reinf area As = %f in^2" %As
print "  "

fc = raw_input(" The compressive strength of conc(ksi) = ")
fc = float(fc)
print "  "
fy = raw_input(" The yeild strength of steel reinf(ksi) = ")
fy = float(fy)
print "  "
b = raw_input(" The width of the beam (in) = ")
b = float(b)
print "  "

a = (As*fy)/(0.85*fc*b)
print " The equivalent depth of rectangular stress block = %f in" %a
print "  "

d = raw_input(" the effective depth of beam = d (in) = ")
d = float(d)
print "  "


rho_t = 0.319*0.85*fc/fy
print " The max. reinf. ratio for a tension controlled section = rho_t = %f " %rho_t
print "  "

rho = As/(b*d)

print " The reinf ratio in this beam = rho = %f " %rho
print "  "
if rho<=rho_t:
	print " The beam section is tension controlled"
else:
	print " The beam section is not tension controlled."
print "  "	
	
lever_arm = d-(a/2)

Mn = As*fy*lever_arm/12
print " The nominal resisting moment(flexural strength) = Mn = As*fy*lever_arm/12(in/ft) = %f ft-kips" %Mn
print "  "	
# calculate strength reduction factor 
c = a/0.85
x = c/d
print " c/d = ", x
print "  "	

if x <=0.375:
	phi = 0.9
	print " strength reduction factor of this section = phi = %f" %phi
	
elif x >= 0.6:
	phi = 0.65
	print " strength reduction factor of this section = phi = %f" %phi
else:
	phi = 0.65+0.25*((1/x)-(5/3))
	print " strength reduction factor of this section = phi = %f" %phi
	
print "  "	

Mu = phi*Mn

print" Thus, the max. permissble moment of this section = Mu = %f ft-kips" %Mu

