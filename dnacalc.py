#!/usr/bin/env python

#Too hot! Call thepolice and the fireman.

#DNAseq = raw_input( "Enter a DNA sequence:" )
#DNAseq = 'ATTGCGTAGCTAAGCTAGCAGACTCCGGAAA'
DNAseq = 'ACTGATTGGCAAA'
DNAseq = DNAseq.upper()

print( 'Sequence ' + DNAseq )

Seqlength = float( len( DNAseq ))

print( 'Length is ' + str(Seqlength) )

NumberA = DNAseq.count('A')
NumberT = DNAseq.count('T')
NumberG = DNAseq.count('G')
NumberC = DNAseq.count('C')

print('A: {:.2f}'.format( NumberA / Seqlength ))
print('T: {:.2f}'.format( NumberT / Seqlength ))
print('C: {:.2f}'.format( NumberC / Seqlength ))
print('G: {:.2f}'.format( NumberG / Seqlength ))

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if Seqlength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + (2 * TotalWeak )
else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / Seqlength
	
print( 'Melting temp: {}'.format(MeltTemp) )

print ( 'Done.' )