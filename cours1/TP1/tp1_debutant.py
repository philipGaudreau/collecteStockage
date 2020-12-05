#!/usr/bin/env python
# coding: utf-8

# # Rappel Python de Bases + Programmation Orientée Objet

# ###Section A : Débutant

# In[ ]:


###Conversion


# In[13]:


##-----Pratique -----:
# Convertir le nombre en chaînes de caractères 
#-------------------------------------------------
# nombre = 15
## Question: print("Le nombre est " + nombre) ?
## 2 solutions possibles 
#-------------------------------------------------
#--Solution 1
print("Le nombre est " + str(nombre))
#Solution 2
print('Le nombre {nombre}'.format(nombre=15))


# In[ ]:


###Variable locale/variable globale


# In[ ]:


#Exemple 1: 
def echange(a,b): 
    print("adresses des parametres : ", id(a),id(b)) 
    c=a a=b b=c
    x,y = 2,3 
    print("adresses de x et de y : ", id(x),id(y)) 
    echange(x,y) 
    print("x=",x) 
    print("y=",y) 

    adresses de x et de y : 140716463784240 140716463784272 
    adresses des parametres : 140716463784240 140716463784272 x= 2 y= 3


# In[ ]:


#Exemple 2: 

def echange2(a,b): 
    c=a 
    a=b 
    b=c 
    return a,b

x,y = 2,3 
x,y=echange2(x,y) 
print("x=",x) 
print("y=",y) 
print()
a=2 b=3 
a,b=echange2(a,b) 
print("a=",a) 
print("b=",b) 
print() 
x= 3 y= 2
a= 3 b= 2


# In[ ]:


#Exemple 2: 
def echange2(a,b): 
    c=a 
    a=b 
    b=c 
    return a,b

x,y = 2,3 
x,y=echange2(x,y) 
print("x=",x)
print("y=",y) 
print() 
a=2 b=3 
a,b=echange2(a,b) 
print("a=",a) 
print("b=",b) 
print() 
x= 3 y= 2
a= 3 b= 


# In[ ]:


##-----Pratique -----:
# La fonction echangeab() ne fonctionne pas.  
def echangeab():
    global a
    c=a
    a=b
    b=c
a=2
b=3
echangeab()
print("a=",a)
print("b=",b)


# In[26]:


## solution 
def echangeab():
    global a
    global b
    c=a
    a=b
    b=c
a=2
b=3
echangeab()
print("a=",a)
print("b=",b)


# In[ ]:


## Fonction qui appelle une autre fonction


# In[1]:


##-----Pratique -----:
# Ecrire une fonction qui appelle une autre fonction 
def display(fun):
    return "Bonjour "+fun

def name():
    return "le monde"

print(display(name()))


# In[ ]:


###Structures de données/Liste


# In[ ]:


#Exemple: 
#Créer une liste de nombres allant de 5 à 15 
print(list(range(5,16))) 
[5,6,7,8,9,10,11,12,13,14,15]


# In[27]:


##-----Pratique -----:
#--Créer une liste de nombres pairs de 1 à 100 ?


# In[3]:


#-------Solution
#--Créer une liste de nombres pairs de 1 à 100
print(list(range(1,101,2)))


# In[ ]:


#Exemple
#------Récupérer des éléments dans une liste 
ma_liste = ["Pierre", "Paul", "Marie"] 
print(ma_liste[0]) 
print(ma_liste[-1]) 
print(ma_liste[:2]) 
print(ma_liste[-2:])

#-------slicing :
#ma_liste[début:fin] print(ma_liste[0:2])


# In[36]:


##-----Pratique -----:
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## Récupérer un élément sur deux dans la liste ?
## Récupérer un élément sur quatre dans la liste ?
## indication: ma_liste[indice_de_depart:indice_de_fin:pas]


# In[43]:


## Solution
## Récupérer un élément sur deux dans la liste ?
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
## solution 1
#pas besoin d'indiquer d'indice spécifique pour les deux premiers nombres  
print(ma_liste[::2])
## solution 2
print(ma_liste[0:10:2])
## solution 1
print(ma_liste[::4])
## solution 2
print(ma_liste[0:10:4])


# In[ ]:


#Exemple
#------Ajouter une élément dans une liste 
ma_liste = [1, 2, 3] 
ma_liste.append(5) 
print(ma_liste)


# In[ ]:


##-----Pratique -----:
#------ Ajouter plusieurs éléments de la sous liste dans une liste ?
ma_liste = [1, 2, 3]
sous_liste=[4,5,6]
# indication 2 solutions possibles


# In[ ]:


#Exemple:
#Récupérer les éléments communs aux deux listes 
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12] 
sliste_01 = set(liste_01) 
sliste_02 = set(liste_02) 
intersect = sliste_01.intersection(sliste_02) 
print(list(intersect))


# In[49]:


##-----Pratique -----:
#------ récupérer les éléments communs et non communs aux deux listes?
#Solution
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
sliste_01 = set(liste_01)
sliste_02 = set(liste_02)
uni = sliste_01.union(sliste_02)
print(list(uni))


# In[ ]:


## Module 


# In[ ]:


##-----Pratique -----:
import math
def add(*x):
    print("Sum is"+math.fsum(x))
    
print(add(20,30))

