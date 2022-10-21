"""Practical_8_GA.ipynb

# Implement Genetic Algorithm

"""

from deap import tools
import random



population=["10101010","11110000","01010101","00001111","10111011","01000100","11100111","00000000"]



binary=[]
for i in range(len(population)):
    binary.append(int(population[i],2))



for i in range(len(population)):
    print("Individual [",i,"]: ",population[i],"\tFitness: ",binary[i])



def crossoverEP():
    #selecting parents using function selRandom()
    parents=tools.selection.selRandom(population,2)
    print("Selected Individuals\nParent 1: ",parents[0],"\tFitness: ",binary[population.index(parents[0])],"\nParent 2: ",parents[1],"\tFitness: ",binary[population.index(parents[1])],"\n")
    #Creating children using cxOnePoint() function to perform one point crossover
    children=list(tools.crossover.cxOnePoint(list(parents[0]),list(parents[1])))
    #cxOnePoint() returns character lists of two children converting them to string using .join() and calculating their fitness value using int()
    f_child1=int("".join(children[0]),2)
    f_child2=int("".join(children[1]),2)
    #printing children and their fitness value
    print("Child 1: ","".join(children[0]),"\tFitness: ",f_child1)
    print("Child 2:","".join(children[1]),"\tFitness: ",f_child2)
    #finding out which child is stronger to survive for next generation
    if(f_child1<f_child2):
       print("\nChild ","".join(children[1])," Survives to next generation")
    else:
       print("\nChild ","".join(children[0])," Survives to next generation")



def mutationEP():
    #selecting parent using selRandom()
    parent=tools.selection.selRandom(population,1)
    print("Selected Individual: ",parent[0],"\tFitness: ",binary[population.index(parent[0])])
    #converting string parent to list of characters because python strings are immutable
    child_list=list(parent[0])
    #selecting random mutation bit
    mutate_bit=random.choice(range(1,7))
    #mutation process
    if child_list[mutate_bit]=='1':
        child_list[mutate_bit]='0'
    else:
        child_list[mutate_bit]='1'
    #Calculating the fitness value of child
    child=int("".join(child_list),2)
    print("\nMutated Child: ","".join(child_list),"\tFitness: ",child,"\n")
    #finding if the child has evolved or not
    if(child<=binary[population.index(parent[0])]):
       print("Child has not evolved")
    if(child>binary[population.index(parent[0])]):
       print("Child has evolved")



while True:
    evolution=input("\nPlease Enter Choice(or to Quit type exit)\nCrossover or Mutation:").lower()
    if evolution=="crossover":
        crossoverEP()
    elif evolution=="mutation":
        mutationEP()
    elif evolution=="exit":
        break
    else:
        print("Please enter a valid choice")