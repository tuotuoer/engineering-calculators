#ASCE 7-10
#Fig 7-7 Driftes formed at Windward and Leeward Steps
#Windward Snow drift - for roof projection & parapet
print " "
print " Let's calculate our windward snow drift load!"
print " "

Pg = raw_input(" Ground Snow Load = ")
Pg = float(Pg)
print " "

gemma = 0.13*Pg+14 

print " The snow density gemma = 0.13*Pg +14 < 30 psf = %f psf" %gemma
print " "

Hb = Pg / gemma

print " The height of balanced snow load = Hb = Pg / Gemma = %f ft" %Hb
print " "

height = raw_input(" Height of high low roof/parapet/projection (ft) = ")
height = float(height)
print " "

Hc = height - Hb
print " The clear height = Hc = height - Hb = %f ft" %Hc
print " "

applicability = Hc/Hb

print " Checking if snow drift is applicable..."
print " "
print " Applicability = Hc/Hb = %f " %applicability
print " "

if applicability < 0.2 :
	print " Drift loads are not required to be applied here..."
else :
	print " Drift loads are required to be applied here..."
	
print " For windward drift, Lu = length of lower roof..."
print " "
Lu = raw_input(" Lu (ft) = ")
Lu = float(Lu)

if Lu <20:
	Lu = 20
	print " Lu < 20, Use Lu = 20 ft"
else:
	print " Okay. Lu >= 20 ft."

	
a = Lu**(1./3.)

b = (Pg+10)**(1./4.)

Hd = 0.43* a*b -1.5

	print 	Hd
	

	

# for Windward drift

# Hd = 0.75*Hd

 #print " The height of windward snow drift = 0.75*Hd = %f ft" %Hd
#print " "
#if Hd <= Hc :
	#w = 4*Hd
	#drift_height = Hd
	#print " The drift width is w = 4*Hd = %f ft" %w
#else:
	#w = 4*(Hd)**2 /Hc
	#drift_height = Hc
	#print " The drift width is w = 4*(Hd)^2 /Hc = %f ft" %w
#print " "

#Pd = drift_height*gemma

#print " The maximum intensity of snow drift surcharge load = Pd = %f psf." %Pd


	





