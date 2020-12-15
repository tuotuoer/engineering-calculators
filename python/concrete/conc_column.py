
print "\n Conc Column \n"

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
	

# concrete column reinforcement requirements

b = input("The width of the conc section(in)")
h = input("The depth of the conc section(in)")

Ag = b*h
output(" The total area of the conc column ", Ag)

As_min = 0.01*Ag
output(" The minimum area of longitudinal reinf", As_min)

As_max = 0.08*Ag
output(" The maximum area of longitudinal reinf", As_max)

size_bar = input("Size of longitudinal rebar")
db = size_bar/8.0
Area_bar = 3.1415*(db**2.0)/4.0
num_bar = input("number of longitudinal rebar")

Ast= num_bar*Area_bar
output(" The total area of the longitudinal rebar ", Ast)

size_tie = input("Size of lateral tie")
dt =size_tie/8.0

least_dim = min(b,h)

Smax = min(48.0*dt, 16.0*db, least_dim)

output("The maximum lateral tie spacing(in)", Smax)
	
sidsway = raw_input(" Non Sway = N or Sway = S ? >>> ")


if sidesway == "N" :
	print " This column is in a non sway frame."
	# Effective length factor
	k = 1.0
	r = 0.3*h
	lu = input("The unsupported height of the column (ft)")
	SR = k*lu*12/r
	output(" The slenderness ratio of the column", SR)
	M1 = input("The end moment M1")
	M2 = input("The end moment M2")
	Non_sway = 34.0-12*(M1/M2)
	
	if SR <= Non_sway:
		print " This non sway column is a short column."
		
		
	else:
		print " This non sway column is a long column."
		print " Slenderness effect must be considered."	
else:
	print " This column is in a sway frame."
	k = input("The effective length factor of the column ")
	r = 0.3*h
	lu = input("The unsupported height of the column (ft)")
	SR = k*lu*12/r
	output(" The slenderness ratio of the column", SR)
	if SR <= 22:
		print " This sway column is a short column."
		
		
	else:
		print " This sway column is a long column."
		print " Slenderness effect must be considered."	
			

	




