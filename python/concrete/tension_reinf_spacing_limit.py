# In accordance with ACI Sec. 10.6, 
#crack width is controlled by limiting 
#the spacing of tension reinforcement 
#to a value given by ACI Eq. 10-4, where fs is in units of kips/in2.


print "\n serviceability requirements of conc beam - control of width of crack \n"

size = raw_input(" The size of stirrup = ")
print "  "
size = float(size)

clear = raw_input(" concrete clear cover to stirrup (in) = ")
print "  "
clear = float(clear)

#Calculate diameter(in) of the stirrup 
dia = size/8

Cc = clear + dia 
print " The clear cover to tension reinf distance = %f in" %Cc
print "  "

fy = raw_input(" The yeild strength of steel reinf(ksi) = ")
fy = float(fy)
print "  "

fs = 2*fy/3

print " The steel stress at service load = fs = (2/3)*fy = %f ksi."%fs
print "  "

s = 600/fs - 2.5*Cc
s_upperlimit = 480/fs

print " The max. allowable bar spacing = s = 600/fs - 2.5*Cc = %f in < S_upperlimit = %f in" %(s,s_upperlimit)
print "  "
s_actural = raw_input(" the actural bar spacing center to center (in) = ")
s_actural = float(s_actural)
print "  "
if s_actural<=s:
	print " this bar spacing is satisfactory."
else:
	print " This bar spacing is not good."
		


