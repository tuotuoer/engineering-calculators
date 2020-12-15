# ASCE 7-10
#Sec 7.3 - Flat Roof Snow Loads

print "  "
print "* Let's calculate our flat roof snow load Pf."
print "  "

Pg = raw_input("ground snow load Pg (psf) = ")
Pg = float(Pg)
print "  "

TC = raw_input(" Terrain Category (B, C, or D?) = ")
print "  "

ER = raw_input(" Exposure of Roof (Fully Exposed = F,Partially exposed = P, or Sheltered = S?) = ")
print "  "

if TC == "B" or TC == "C" and ER == "F" :
	Ce = 0.9
elif TC == "B" or TC == "C" and ER == "P":
	Ce = 1.0
elif TC == "B" and ER == "S":
	Ce = 1.2
elif TC == "C" and ER == "S":
	Ce = 1.1
elif TC == "D" and ER == "F":
	Ce = 0.8
elif TC == "D" and ER == "P":
	Ce = 0.9
else:
	Ce = 1.0
	
print " ASCE 7-10 Table 7-2 Exposure factor"
print "  "
print " Ce = ", Ce
print "  "
TF = raw_input(" Thermal Condition (just kept above freeze w/ cold,ventilated roofs = V, Unheated and Open air = O, Kept below freezing = F, None of the above = N)  =  ")
print "  "
if TF == "V":
	Ct = 1.1
elif TF == "O":
	Ct = 1.2
elif TF == "F":
	Ct = 1.3
else:
	Ct = 1.0
	
print " ASCE 7-10 Table 7-3 Thermal factor"
print "  "
print " Ct = ", Ct
print "  "

Is = raw_input(" Importance Factor = ")
Is = float(Is)
print "  "

Pf = 0.7*Ce*Ct*Is*Pg

print " The Calculated flat roof snow load Pf based on ASCE 7-10 is :"
print "  "
print " Pf = 0.7*Ce*Ct*Is*Pg = %f  psf" % Pf


	






