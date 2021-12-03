"""
lo que hay que conseguir:
#
##
###
####
#####
... hasta n
"""
import random
#n = random.randint(0,10)
#print (n)
n = 3
if n != 0:
    print ('#' * (n-n))
if n != 1:
    print ('#' * (n-(n-1)))
if n != 2:
    print ('#' * (n-(n-2)))
if n == 3:
    print ('#' * (n-(n-3)))

