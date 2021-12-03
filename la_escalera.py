"""
lo que hay que conseguir:
#
##
###
####
#####
... hasta m
"""
import random
m = random.randint(1,10)
for b in range(0,m+1):
    producto ='#' * b
    print(producto)
