# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:21:36 2023

@author: HP
"""


class NoExisteSubcoleccion(Exception):

    def __init__(self, elemento: int):
        super().__init__(f"No existe subcolección con el elemento: {elemento}")


class NoExisteSubcoleccionRango(Exception):

    def __init__(self, *args):
        cadena = "No se puede obtener la subcolección porque no se encuentra el"
        if len(args) > 1:
            valor = f" {args[0]} y {args[1]}"
        else:
            valor = f" {args[0]}"
        super().__init__(cadena + valor)
