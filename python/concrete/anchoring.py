# Anchoring to Concrete

# A_brg = net bearing area of the head of bolt

# A_Nc = projected conc failure surface of a single anchor 
#		 or groups of anchors

# A_Nco = projected conc failure surface of a single anchor 

# A_se_N = effective cross section area of anchor in tension

# A_se_V = effective cross section area of anchor in shear

# A_Vco = projected conc failure surface of a single anchor 
#		  for shear strength calculation

# c_ac = critical edge dist required to develop basic 
#		 conc breakout strength of a post-installed anchor 
#		 in uncracked conc

# c_a_max = max. dist from center of anchor shaft to edge of conc.

# c_a_min = min. dist from center of anchor shaft to edge of conc.

# c_a1 = dist from the center of anchor to edge of conc in one direction

# c_a2 = dist from the center of anchor to edge of conc in direction
#		 perpendicular to c_a1

# d_a = outside diameter of anchor

# d_prime_a = substitued for d_a for an oversized anchor

# e_h = dist from inner surface of the shaft of a j or L bolt to
#		the outer lip of the J or L bolt

# e_prime_N = dist betw resultant tension load on a group of anchors 
#			  loaded in tension and the centroid of the group of anchor 

# f_uta = specified tensile strength of the anchor

# f_ya = specified yeild strength of anchor 

# h_a = thkness of member in which anchor is located

# h_ef = effective embedment depth of anchor

# k_cp = pryout coefficient 

# l_e = load bearing length of the anchor for shear

# n = number of anchors

# N_b = basic concrete breakout strength in tension
#		of a single anchor in cracked concrete

# N_cb = nominal conrete breakout strength in tension
#		of a single anchor

# N_cbg = nominal concrete breakout strength in tension 
#		  of a group of anchors

# N_n = nominal strength in tension 

# N_p = pullout strength in tension of a single
#		anchor in cracked concrete

# N_pn = nominal pullout strength in tension of a single anchor

# N_sa = nominal strength of a single anchor or group
#		of anchors in tension as governed by steel strength

# N_sb = side face blowout strength of a single anchor

# N_sbg = side face blowout strength of a group of anchors

# N_ua = factored tensile force applied to anchor or group of anchors

# V_cb = nominal concrete breakout strength in shear of a single anchor

# V_cbg = nominal concrete breakout strength in shear of a group of anchors

# V_cp = nominal concrete pryout strength of a single anchor

# V_cpg = nominal concrete pryout strength of a group of anchors

# V_n = nominal shear strength

# V_sa = nominal strength in shear of a single anchor or group
#		of anchors as governed by the steel strength

# V_ua = factored shear force applied to a single anchor or group of anchors

# phi = strength reduction factor 

# psi_c_N = factor to modify tensile strength of anchors based on 
#		   presence or absence of cracks in concrete

# psi_c_P = factor to modify pullout strength of anchor based on 
#			presence or absence of cracks in concrete

# psi_c_V = factor to modify shear strength of anchor based on 
#			presence or absence of cracks in concrete

# psi_cP_N = factor to modify tensile strength of post-installed 
#			anchor intended for use in uncracked concrete w/o supplementary

# psi_ec_N = factor to modify tensile strength of anchors based on 
#			eccentricity of applied load

# psi_ec_V = factor to modify shear strength of anchors based on 
#			eccentricity of applied load

# psi_ed_N = factor to modify tensile strength of anchors based on 
#			proximity to edges of concrete members

# psi_ed_V = factor to modify shear strength of anchors based on 
#			proximity to edges of concrete member

# psi_h_V = factor to modify shear strength of anchors located 
#			in concrete members with ha<1.5*c_a1


print "\n concrete anchorage \n"

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

h_ef = input("The effective embedment depth of the anchor (in)")

n = input("The number of anchors ")

dia = input("The diameter of the anchors (in)")

A_se_N = input("The effective cross sectional area in tension (in^2)")

A_se_V = 3.1415*(dia**2)/4.0

output("The effective cross sectional area in shear (in^2)", A_se_V)

f_uta = input("The minimum specified tensile strength of steel anchor (ksi)")

fc = input("The compressive strength of concrete")

A_brg = input("The effective bearing area of the bolt head (in^2)")

N_ua = input("The factored tensile force applied to the anchors (kips)")

V_ua = input("The factored shear force applied to the anchors (kips)")

# Check Tension**************************************************************

# 1: Check steel anchor ductile or brittle
# pick a strength reduction factor
# for ductile steel anchor
if f_uta >= 60:
	phi_tension = 0.75
	phi_shear = 0.65
# for brittle steel anchor
else:
	phi_tension = 0.65 
	phi_shear = 0.6
output("The strength reduction factor", phi_tension)

# Check steel strength of anchors in tension

N_sa = A_se_N*f_uta
output("The nominal strength of anchor in tension",N_sa)

N_sa_design = n*phi_tension*N_sa

output("The design strength of anchor/group anchors in tension", N_sa_design)

# 2: Check concrete breakout strength in tension 


A_Nco = 9*h_ef**2

output(" The projection area of failure surface for one single anchor on the conc outer surface",A_Nco)

A_Nc = input("The projected area of the failure surface")

c_a_min = input("The smallest of the influencing edge distances")

	
if c_a_min>= 1.5*h_ef:

	psi_ed_N = 1.0
 else:
	psi_ed_N = 0.7+0.3*(c_a_min/1.5/h_ef)
	
output("The modification factor for edge effect in tension", psi_ed_N)
print "  "
anchor_type = raw_input("Cast-in (c) or Post installed (p)?")
print "  "

if anchor_type =="c":
	kc = 24
else:
	kc = 17
	

N_b = kc*(fc**0.5)*h_ef**(1.5)/1000.0
output("The nominal concrete breakout strength for a single anchor in tension",N_b)

N_cbg = (A_Nc/A_Nco)*psi_ed_N*N_b

output("The nominal conc breakout strength for anchor group in tension", N_cbg)

# ACI section D.3.3.5 & ACI eq D-4

N_cbg_design = 0.75*0.7*N_cbg
output("The design conc breakout strength for the anchor group", N_cbg_design)

# 3: Check pullout strength of steel anchor in tension

N_p = 8* A_brg*fc/1000.0

output("The nominal pullout strength in cracked concrete", N_p)

# ACI Section D.3.3.4 & ACI eq.D-13

N_p_design = n*0.75*0.7*N_p

# Anchors in Shear*************************************************************
# strength reduction factor 
# phi_shear = 0.65 -shear on ductile anchor bolt 

# 1: Check steel strength of anchors in shear
V_sa = 0.6*A_se_V*f_uta

output("The nominal strength of anchor in shear",V_sa)

V_sa_design = n*phi_shear*V_sa

output("The design strength of anchor/group anchors in shear", V_sa_design)

# 2: Check  concrete pryouut strength in shear
# get kcp value

if h_ef >= 2.5:
	k_cp = 2.0
else:
	k_cp = 1.0
	
output("The pryout coefficient", k_cp)

V_cpg = k_cp*N_cbg

output("The nominal concrete pryout strength for cast-in anchor group in shear", V_cpg)

V_cpg_design = 0.75*phi_tension*V_cpg
output("The design concrete pryout strength for cast in anchor group in shear", V_cpg_design)









	



	
	
	


















