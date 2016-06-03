#!/usr/bin/env python

#Too hot! Call thepolice and the fireman.

DNAseq = 'ATGAAC'

print( 'Sequence ' + DNAseq )

Seqlength = float( len( DNAseq ))

print( 'Length is ' + str(Seqlength) )

NumberA = DNAseq.count('A')
NumberT = DNAseq.count('T')
NumberG = DNAseq.count('G')
NumberC = DNAseq.count('C')

print('A: ' + str( NumberA / Seqlength ))
print('T: ' + str( NumberT / Seqlength ))
print('C: ' + str( NumberC / Seqlength ))
print('G: ' + str( NumberG / Seqlength ))
