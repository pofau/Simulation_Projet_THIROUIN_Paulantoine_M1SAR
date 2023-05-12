#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:00:11 2023

@author: pofau
"""
from class_vecteur3D import Vecteur3D
from class_torseur import Torseur
from class_force import Force_Harmonique, Ressort_Amortisseur, force_Ponctuelle, Tige, Tige_CDM, gravite, force_const, Viscosite, Attracteur, Prisme, Rod
from class_particule import Particule

import numpy as np
import matplotlib.pyplot as plt
import sys
from math import pi,atan2
import pygame
from pylab import show, legend, title, plot
from pygame.locals import *
import random
import numpy as np
import matplotlib.pyplot as plt

# class_PID.py
class PIDController(object):
    """classe simulant le PID
    """
    
    def __init__(self, kp, ki, kd, dt, p1=Particule(), p2=Particule(), start = 0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.error_sum = 0
        self.last_error = 0
        self.p1 = p1
        self.p2 = p2
        self.start = start


    def setForce(self, p):
        """fonction qui renvoie un vecteur3D
        permettant de contrôleur le système via un PID
        """
        
        if p is self.p1:
            angle = atan2(self.p2.getPosition().y - p.getPosition().y, self.p2.getPosition().x - p.getPosition().x)
            error = self.start - angle

            # Proportional term
            p_term = self.kp * error

            # Integral term
            self.error_sum += error * self.dt
            i_term = self.ki * self.error_sum

            # Derivative term
            d_term = self.kd * (error - self.last_error) / self.dt
            self.last_error = error

            return Vecteur3D(p_term + i_term + d_term)
        
        else:
            return Vecteur3D()