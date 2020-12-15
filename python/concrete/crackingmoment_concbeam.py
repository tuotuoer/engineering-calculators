

print "\n Cracking moment Mcr of a conc beam section \n"

fc = raw_input(" The compressive strength of conc(psi) = ")
fc = float(fc)
print "  "
b = raw_input(" The width of the beam = b(in) = ")
b = float(b)
print "  "

h = raw_input(" The total depth of the beam = h(in) = ")
h = float(h)
print "  "

Ig = (1/12.0)*b*(h**3)

print " The gross moment of inertia of the section = Ig = %f in^4" %Ig

fr = 7.5*1.0*fc**(1./2.)

print "\n Modulus of rupture of conc = fr = %f psi \n" %fr

yt = h/2

Mcr = fr*Ig/yt/1000.0/12.0

#lb-in to ft-kip 

print " The cracking moment of the section = Mcr = fr*Ig/yt = %f ft-k" %Mcr
