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

m = 3
for b in range(0,3):
    if m!=b:
        suma ='#' * b
        print(suma)
    
    
    if m == b:
        suma1 = '#' * m
        print(suma1)
        

    

"""
if n != 0:
    print ('#' * (n-n))
if n != 1:
    print ('#' * (n-(n-1)))
if n != 2:
    print ('#' * (n-(n-2)))
if n == 3:
    print ('#' * (n-(n-3))) """

