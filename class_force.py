#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:14:23 2023

@author: pofau
"""
# Importer les modules nécessaires

from class_vecteur3D import Vecteur3D
import numpy as np


###Class Rod : Tige
class Rod(object):
    """classe qui instancie une tige rigide
    """

    def __init__(self, particules = []):
        self.raid = 10000
        self.c = 1000
        self.particules = particules #[p1 p2]
        self.l0 = (self.particules[1].getPosition()-self.particules[0].getPosition()).mod()
        
        
    def setForce(self, p): 
        """fonction qui renvoie les efforts de la tige
        """
        if p is self.particules[0] : #force vers P2
            d = self.particules[1].getPosition()-self.particules[0].getPosition()
            dv = (p.vitesse[-1]-self.particules[1].vitesse[-1])
        
        elif p is self.particules[1] : #force vers P1
            d = self.particules[0].getPosition()-self.particules[1].getPosition()
            dv = (p.vitesse[-1]-self.particules[0].vitesse[-1])
                    
        else : 
            return Vecteur3D()
        
        F_ressort =  ((d.mod() - self.l0) * self.raid) * d.norm()
        F_amortisseur = - self.c * (dv ** d.norm())*d.norm()
        return F_ressort + F_amortisseur  


    
###Class Prismatique
class Prisme(object):
    """classe simulant une liaison prismatique
    """
    
    def __init__(self, axe = Vecteur3D()):
        self.axe = axe  #ex : Vecteur3D(1, 0, 0)
        
        
    def setForce(self):
        """fonction renvoyant la contrainte de mouvement
        sous forme de Vecteur3D
        """
        return self.axe



###Class Force Constante
class force_const(object):
    """classe qui simule un effort constant
    """
    
    def __init__(self, force=Vecteur3D(),particule=[], etat = True):
        self.force = force
        self.particule = particule
        self.etat = etat
    
    def setEtat(self, etat):
        self.etat = etat

    def setForce(self, particule):
        
        if self.etat == False :
            force_const = Vecteur3D()
            
        elif self.etat == True :
            if particule in self.particule:
                force_const = particule.masse * self.force

            else : 
                force_const = Vecteur3D()

        return force_const


###Class Force Harmonique
class Force_Harmonique(object):
    """
    Classe pour représenter une force harmonique qui agit sur une particule.
    """
    
    def __init__(self, V3D = Vecteur3D(), etat=True, omega=0, u = [], particule = []):
        self.etat = etat       # Booléen pour savoir si la force est active ou non
        self.w = omega         # Fréquence angulaire de la force harmonique
        self.particule = particule  # Particule sur laquelle la force agit
        self.V3D = V3D
        self.u = u[0]

    def setEtat(self, etat):
        self.etat = etat

    def setForce(self, particule):
        """
        Calcule et renvoie la force harmonique agissant sur une particule à un temps donné 't'.
        
        Args:
        - particule: la particule sur laquelle la force pourrait agir
        - t: temps actuel
        
        Returns:
        - Vecteur3D: force harmonique agissant sur la particule (si la force est active et la particule correspond)
        """
        # Si la force est active et agit sur la particule donnée
        
        if self.etat == False :
            force_harmo = Vecteur3D()
            
        elif self.etat == True :
            if particule in self.particule or len(self.particule) == 0:
                t = self.u.getTime()
                force_harmo = np.cos(self.w * t) * self.V3D
            else : 
                force_harmo = Vecteur3D()

        return force_harmo

        
###Class Ressort
class Ressort_Amortisseur(object):
    """classe simulant un ressort avec amortisseur
    """
    
    def __init__(self, raideur=0, c=0, l0=0, particules = []):
        self.raid = raideur
        self.l0 = l0
        self.c = c
        self.particules = particules #[p1 p2]
        
        
    def setForce(self, p): 
        """fonction renvoyant les efforts du ressort amortisseur
        sur la particule concerné
        """
        
        if p is self.particules[0] : #force vers P2
            d = self.particules[1].getPosition()-self.particules[0].getPosition()
            dv = (p.vitesse[-1]-self.particules[1].vitesse[-1])
        
        elif p is self.particules[1] : #force vers P1
            d = self.particules[0].getPosition()-self.particules[1].getPosition()
            dv = (p.vitesse[-1]-self.particules[0].vitesse[-1])
                    
        else : 
            return Vecteur3D()
        
        F_ressort =  ((d.mod() - self.l0) * self.raid) * d.norm()
        F_amortisseur = - self.c * (dv ** d.norm())*d.norm()
        return F_ressort + F_amortisseur   
    

###class Tige (pour les coeffs)
class Tige(object):
    """classe donnant les bons coefficients pour les tiges
    """
    
    def __init__(self):
        self.k = 10000
        self.c = 1000
        
    def setCoeff(self):
        """fonction renvoyant les coeffs
        """
        return self.k, self.c
    
    
#### Tige avec centre de masse : classe non utilisé
class Tige_CDM(object):
    """la classe simule une tige avec un centre de masse
    """
    
    def __init__(self, particule=[], masse = 0.1):
        self.k = 10000
        self.c = 1000
        self.particule = particule
        self.masse = masse
    
    def setTige(self):
        """renvoie le centre de masse de la tige
        """
        #On suppose que la barre est homogène
        #d nous donne la distance moyenne entre les deux extrémités de la tige : ainsi on aura le CdM
        d = self.particules[1].getPosition()-self.particules[0].getPosition()
        d = d.mod()/2
        
        
###Class Gravite
class gravite(object):
    """classe simulant les efforts de la gravité sur une particule
    """
    
    def __init__(self, gravite=Vecteur3D(0,0,0), *Args):
        self.gravite=gravite
        self.p = Args
        
        
    def setForce(self, particule):
        """fonction renvoyant les efforts de gravité appliqué à la particule
        """
        if particule in self.p or len(self.p)==0:
            return particule.masse*self.gravite
        else :
            return Vecteur3D()


###Class Viscosite
class Viscosite(object):
    """classe simulant les effets de la viscosité
    sur la trajectoire d'une particule
    """
    
    def __init__(self, coeff=0):
        self.coeff = coeff
        
        
    def setForce(self, particule):
        """fonction renvoyant les effets de la viscosité sur la particule
        """
        return -(particule.vitesse[-1]*self.coeff)
    

###Class Attracteur
class Attracteur(object):
    """classe simulant un champ attracteur sur des particules
    """
    
    def __init__(self, coeff=1, position=Vecteur3D(), *args):
        self.coeff = 1/coeff
        self.position = position
        self.particules = args
        
        
    def setForce(self, particule):
        """fonction qui renvoie les effets du champ
        attracteur sur la particule
        """
        if len(self.particules) == 0 :
            return (self.position-particule.position[-1])*self.coeff
        else : 
            for p in self.particules :
                if p is particule :
                    return (self.position-particule.position[-1])*self.coeff
                else :
                    return Vecteur3D()

###Force Ponctuelle (exemple : lancement)
class force_Ponctuelle(object):
    """classe qui simule une force ponctuelle à un instant précis
    sur une particule
    """
    
    def __init__(self, force=Vecteur3D(), particule=[]):
        self.force = force
        self.lancer = True
        self.particule = particule
        
        
    def setForce(self, particule):
        """fonction renvoyant les effets de la force ponctuelle
        sur la particule
        """
        if self.lancer == True:
            self.lancer == False
            return particule.masse*self.force
        else :
            return Vecteur3D()

#%%
if __name__=="__main__": #false lors d'un import    
    p1 = Particule()
    p2 = Particule()
    u1 = Univers()
    
    rod = Rod([p1, p2])
    rod.setForce(p1)
    
    prisme = Prisme()
    prisme.setForce()
    
    force_const = force_const()
    force_const.setForce(p1)
    
    f_h = Force_Harmonique(u = [u1], particule=[p1])
    f_h.setForce(p1)
    
    r_a = Ressort_Amortisseur() 
    
    tige = Tige()
    tige.setCoeff()
    
    #t_cdm = Tige_CDM()
    gravite = gravite()
    gravite.setForce(p1)
    
    viscosite = Viscosite()
    viscosite.setForce(p1)
    
    attracteur = Attracteur()
    attracteur.setForce(p1)
    
    f_p = force_Ponctuelle()
    f_p.setForce(p1)
    
    