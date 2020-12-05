#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Rappel Python de Bases + Programmation Orientée Objet
###Section A : Avancé


# In[ ]:


#-------Pratique
##--- Récupérer un élément dans une liste sans générer d'erreur
#indication: créer une fonction qui nous permette de récupérer un élément dans une 
#liste à partir de son indice, sans retourner d'erreur au cas où l'indice est 
#en dehors des limites de la liste
## exemple:
#print(recuperer_item(liste, 0))    #--- correct
#print(recuperer_item(liste, 5))    #--- la liste ne contient pas le 4eme element
#print(recuperer_item(liste, -13))  #--- la liste ne contient pas 12 element si on la parcourt de la fin


# In[ ]:


#-------Pratique / Solution
##--- Récupérer un élément dans une liste sans générer d'erreur
#indication: créer une fonction qui nous permette de récupérer un élément dans une 
#liste à partir de son indice, sans retourner d'erreur au cas où l'indice est 
#en dehors des limites de la liste
## exemple:
#print(recuperer_item(liste, 0))    #--- correct
#print(recuperer_item(liste, 5))    #--- la liste ne contient pas le 4eme element
#print(recuperer_item(liste, -13))  #--- la liste ne contient pas 12 element si on la parcourt de la fin

def recuperer_item(liste, indice):
    if indice < 0 and abs(indice) <= len(liste):
        return liste[indice]
    elif indice > 0 and indice < len(liste):
        return liste[indice]
    elif indice == 0 and liste:
        return liste[0]
 
    return "Index {} hors de la liste".format(indice)


# In[ ]:


#-------Pratique 
#Écrire un programme qui invite l'utilisateur à entrer une chaîne et compte le nombre d'occurrences 
#de chaque lettre dans la chaîne, indépendamment de la casse


# In[ ]:


#-------Pratique 
#Écrire un programme qui invite l'utilisateur à entrer une chaîne , écrire une première fonction qui retourne sa longueur. 
#Ecrire une seconde fonction qui retourne la longueur d'une chaîne après l'avoir transformée en liste.


# In[ ]:


#-------Pratique 
#Écrire un programme qui invite l'utilisateur à entrer une phrase, puis fait des statistiques
#sur cette phrase ( donne le mot le plus long, le mot le plus court et nombre totale de mots 
#dans la phrase


# In[ ]:


#-------Pratique 
#Écrire un programme  qui nettoit une chaîne de caractères (String) de tout type de séparateurs (espaces, tabulations,
#guillemets, ponctuations et apostrophes)


# In[ ]:


#----- Pratique
#Pour acheter en ligne un billet de cinéma ( déterminer les objets à manipuler + les actions à faire)
#Objets à manipuler ( site web cinema, nom du film, date présentation, heure présentation, montant a payer) 
#Actions à faire ( entrer le site web du cinéma, choisir nom film, entrer date et heure présentation, afficher montant a payer 


# In[ ]:


# --- Pratique
#Pour prendre le bus  (déterminer les objets à manipuler + les actions à faire) 
#Objets à manipuler ( numéro bus , ticket but, date du jour, heure du jour, montant a payer) 
#Actions à faire ( aller dans la station bus, chercher le numéro de bus à apprendre, acheter ticket bus, 
#entrer date et heure, introduire montant à payer 


# In[ ]:


# --- Pratique
# pour réserver  une chambre d’hôtel  sans carte de crédit ( déterminer les objets à manipuler + les actions à faire) 
# Objets à manipuler ( nom de l’hôtel, date d’arrivée, date départ, nuitées, nombre de chambres, nombre d’adultes, nombre enfants , lit_bébé, montant à payer par nombre de chambres, montant total à payer, confirmation réservation
# Actions à faire ( introduire le nom de l’hôtel, introduire les dates d’arrivée et départ, introduire le nombre de chambres, introduire le nombre d’adultes, le nombre d’enfants 

