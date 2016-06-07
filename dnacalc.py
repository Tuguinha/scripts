#!/usr/bin/env python

#Too hot! Call thepolice and the fireman.

#DNAseq = raw_input( "Enter a DNA sequence:" )
#DNAseq = 'ATTGCGTAGCTAAGCTAGCAGACTCCGGAAA'
DNAseq = 'ACTGATTGGCAAA'
DNAseq = DNAseq.upper()

print( 'Sequence ' + DNAseq )

Seqlength = float( len( DNAseq ))

print( 'Length is ' + str(Seqlength) )


#for loop

TotalStrong = 0
TotalWeak = 0

Bases = "CGTA"
for Base in Bases:
	Count = DNAseq.count( Base )
	Frequency = DNAseq.count( Base ) / Seqlength
	print ( '{}: {:.2f}'.format(Base, Frequency ) )
	if Base in 'GC': 
		TotalStrong = TotalStrong + Count
	elif Base in 'TA': 
		TotalWeak = TotalWeak + Count

		print ( TotalStrong, TotalWeak )


NumberA = DNAseq.count('A')
NumberT = DNAseq.count('T')
NumberG = DNAseq.count('G')
NumberC = DNAseq.count('C')


#before

print('A: {:.2f}'.format( NumberA / Seqlength ))
print('T: {:.2f}'.format( NumberT / Seqlength ))
print('C: {:.2f}'.format( NumberC / Seqlength ))
print('G: {:.2f}'.format( NumberG / Seqlength ))


#melting temp

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if Seqlength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + (2 * TotalWeak )
else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / Seqlength
	
print( 'Melting temp: {}'.format(MeltTemp) )

print ( 'Done.' )