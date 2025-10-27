import ase
from ase.build import *
from ase.io import read, write
bulkatoms = read("grani.vasp")
#bulkatoms *= (3, 3, 3)
#sur = surface(bulkatoms, (0,0,1),2)
#sur.center(vacuum=10, axis=2)
#sur *= (2, 2, 1)
sorted_atoms = sort(bulkatoms) 
sorted_atoms.write("sort.vasp")  #, direct=True)
 
