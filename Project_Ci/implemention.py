# -*- coding: utf-8 -*-
"""shadshoda.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vepd2teYQg6UMvrujww_IFeo2SckuPQk
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from IPython.utils.coloransi import InputTermColors

D = int(input("Enter The Numer of Variables : "))
lower = int(input("Enter The Lower Bound Constraint : "))
upper = int(input("Enter The Upper Bound Constraint : "))
type =str(input("Enter The Objective Type : "))


F = 0.8
CR= 0.9
NP = 10
fitness = []

def intial_population(NP,D,lower,upper):
  pop = np.random.uniform(lower, upper, (NP, D))
  Generation = np.round(pop,2)
  return Generation

def mutation(pop,target_vector):
  r1, r2, r3 = random.sample(range(NP), 3)
  for i in range(0 , NP):
    p1=pop[r1]
    p2=pop[r2]
    p3=pop[r3]
    
    if(p1.all() == target_vector.all() ):
      if(r1 < NP-1) : 
          p1 = pop[r1+1]
      else:
          p1 = pop[r1-1]

    if(p2.all() == target_vector.all() ):
        if(r2 < NP-1 ) : 
           p2 = pop[r2+1]
        else:
            p2 = pop[r2-1]

    if(p3.all() == target_vector.all() ):
          if(r3 < NP-1 ) : 
              p3 = pop[r3+1]
          else:
              p3 = pop[r3-1]

  Difference = np.subtract(p1, p2) 
  mutant_vector = np.add(F*Difference,p3)
  return mutant_vector

def ssover(target_vector,mutant_vector):

  trial_vector = np.array()

  for i in range(D):
    Rn=random.uniform(0,1)
    if(Rn >= CR ):
      trial_vector[i]=target_vector[i]
    else:
      trial_vector[i]=mutant_vector[i]
  
  if(target_vector.all() == trial_vector.all()):
    r1, r2 = random.sample(range(D), 2)
    for i in range (D):
      if(i == r1 or i == r2):
        trial_vector.append(mutant_vector[i])
      else:
        trial_vector.append(target_vector[i])
  return trial_vector

def Crossover(target_vector, mutant_vector):

  # Initialize the trial vector.
  trial_vector = np.zeros(D)

  for i in range(D):
    Rn = random.uniform(0, 1)
    if (Rn >= CR):
      trial_vector[i] = target_vector[i]
    else:
      trial_vector[i] = mutant_vector[i]

  if (target_vector.all() == trial_vector.all()):
    r1, r2 = random.sample(range(D), 2)
    for i in range(D):
      if (i == r1 or i == r2):
        trial_vector[i] = mutant_vector[i]
      else:
        trial_vector[i] = target_vector[i]

  return trial_vector

def Selection(target_vector,trial_vector):
  u_fitness = np.sum(trial_vector)
  x_fitness = np.sum(target_vector)
  if(type == "Maximize" or type == "maximize"):
    if(u_fitness > x_fitness):
      return trial_vector
    else:
      return x_fitness
  elif(type == "Minimize" or type == "minimize"): 
    if(u_fitness < x_fitness):
      return trial_vector
    else:
      return target_vector

# the code of the population board 
iterations= int(input("enter the number of iterations : "))


pop = intial_population(NP,D,lower,upper)
for row in pop:
           print(" ".join(str(item).ljust(10) for item in row))

#for loop of run time 
for repeater in range (1 , iterations) : 

    for i in range (0 , NP):  
        xi= pop[i]    
        vi=mutation(pop,xi)
        ui = Crossover(xi,vi)
        new_child = Selection(xi,ui)
        pop[i] = new_child
        fitness.append(np.sum(new_child))

        
    

    print ("\n\n\nthe new generation is :") 
    new_generation=np.round(pop,1)
    np.set_printoptions(10, 2)
    for row in new_generation:
           print(" ".join(str(item).ljust(10) for item in row))
    print("\n\n------------------------------------------------------------------------------------------------------------------------------------------------\n")

    F = round(random.uniform(0, 2),2)
    CR=random.uniform(0,1)

plt.hist(fitness, density = True , bins = 30)
plt.ylabel('best-fitness')
plt.xlabel('Differentia Evaluation')
plt.show()

