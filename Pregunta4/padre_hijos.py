# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 06:05:54 2022

@author: Display
"""

from pyswip import Prolog

prolog = Prolog()
prolog.assertz("padre(guido,yessika)")
prolog.assertz("padre(guido,lenard)")
list(prolog.query("padre(guido,X)"))==[{'X':'yessica'},{'X':'lenard'}] 
for soln in prolog.query("padre(X,Y)"):
    print (soln["X"], "es padre de", soln["Y"])

#list(prolog.query("padre(lucas,X)"))==[{"X":"rosa"}, {"Y":"miguel"}]
#for elemento in prolog.query("abuelo(X,Y)"):
 #   print(elemento["X"], "es abuelo de ", elemento["Y"])
#for elemento in prolog.query("nieto(X,Y)"):
 #   print(elemento["X"], "es nieto de ",elemento["Y"])
#for elemento in prolog.query("es_primo(X,Y)"):
  #  print(elemento["X"],"es primo de ", elemento["Y"])