#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Rappel Python de Bases + Programmation Orientée Objet


# In[ ]:


###Section A : Intermediaire 


# In[ ]:


Structures de données/Liste  


# In[ ]:


#Exemple
#Remplacer un élément dans une liste 
liste = ["Obama", "Michelle", "Spider-man", "Mickey", "Hulk"] 
nom_a_chercher = "Mickey" nouveau_nom ="Mini" 
liste = [x.replace(nom_a_chercher, nouveau_nom) 
for x in liste] 
    print(liste)


# In[ ]:


Fonction Lambda 


# In[13]:


##-----Pratique -----:
def cube(n):
    return n**3
print(cube(2)) 

#créer une expression lambda qui calcule le cube d'un nombre donné?


# In[ ]:


##-----Pratique -----:
#Ecrire du code pour additionner deux variables
# indciation utiliser une expression lambda au lieu d une fonction
'''def add(a,b):
    return a+b

print(add(10,20))'''
## solution
l=lambda a,b:a+b
print(l(10,20))


# In[14]:


##-----Pratique / Solution -----:
def cube(n):
    return n**3
print(cube(2)) 

#créer une expression lambda qui calcule le cube d'un nombre donné?
#Solution
f = lambda n:n**3
print(f(2))


# In[ ]:


##-----Pratique -----:
#créer une expression lambda qui retournera oui si le nombre donné est pair et 
#non si le nombre donné est impair?


# In[17]:


##-----Pratique /Solution-----:
#Ecrire une expression lambda qui retourne oui si le nombre donné est pair et non 
#si le nombre donné est impair?
l= lambda x: 'YES' if x%2==0 else 'NO'
print(l(4))
print(l(5))


# In[ ]:


##-----Pratique /Solution-----:
#Ecrire du code simple pour multiplier chaque element de la liste par 2
#indication: expression lambda et map()
lst=[2,3,4,5]
#créer une expre
result = list(map(lambda n:n*2,lst))
print(result)
print(lst)


# In[ ]:


##-----Pratique /Solution-----:
#Ecrire du code simple pour recuperer uniquement les elements de la liste qui sont divisible par 2
#indication: expression lambda et filter()

lst=[10,2,33,45,89,2]

result = list(filter(lambda x:x%2==0,lst))
print(result)
for i in result:print(i)


# In[ ]:


##-----Pratique /Solution-----:
#Ecrire du code simple pour aditionner les elements d une liste un a un
#indication: expression lambda et reduce()
lst=[5,10,15,20]
result=reduce(lambda x,y:x+y, lst)
print(result)


# In[ ]:


###Structures de données/Tuple & Fonction Lambda  


# In[ ]:


#Exemple
#Trier une liste de tuples liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)] 
liste.sort(key=lambda x: x[1]) print(liste) [('Wall-E', 3), ('Blade Runner', 4), ('Harry Potter', 5)]


# In[ ]:


### PRogrammation Orientee Objet / Class


# In[3]:


#-------Pratique / Solution
#Écrire un programme qui définit la classe Employee avec les attributs suivants: 
#nom, (courriel) email  et la méthode changer_courriel()
# verifier si le courriel est bin formate et le nom n’est pas vide  

class employee ():
    def __init__(self, name, email):
        self.name =name
        self.email=email
    
    def changeCourriel(mail):
        self.email = mail


# In[ ]:


#-------Pratique / Solution
#------Écrire un programme qui définit une classe Téléphone avec les attributs privés numéro et modèle
#---Ajouter au programme de la question 7) les méthodes getnumero et setnumero

class telephone ():
    def __init__(self, numero, modele):
        self.__numero =numero
        self.__modele=modele

    def getNumero(self):
        return self.__numero

    def setNumero(self):
        self.__numero=numero

