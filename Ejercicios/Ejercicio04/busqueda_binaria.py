# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 11:27:51 2023

@author: Fernando
"""

"""
Ejercicio01
"""

from abc import ABC, abstractmethod


class BusquedaBinaria(ABC):

    @abstractmethod
    def buscar(self):
        pass


class BuscarElemento(BusquedaBinaria):

    def buscar(self, elementos, elemento):
        izq = 0
        der = len(elementos) - 1
        primer_pos = -1

        while izq <= der:
            medio = izq + (der - izq) // 2

            if elementos[medio] == elemento:
                primer_pos = medio
                der = medio - 1
            elif elementos[medio] < elemento:
                izq = medio + 1
            else:
                der = medio - 1

        return primer_pos # Si el elemento no se encuentra en el arreglo

class BuscarUltimoElemento(BusquedaBinaria):

    def buscar(self, elementos, elemento):
        izq = 0
        der = len(elementos) - 1
        ultima_pos = -1

        while izq <= der:
            medio = (izq + der)// 2
            if elementos[medio] == elemento:
                ultima_pos = medio
                izq = medio + 1
            elif elementos[medio] < elemento:
                izq = medio + 1
            else:
                der = medio - 1

        return ultima_pos # Si el elemento no se encuentra en el arreglo


class BuscarPosicion(BusquedaBinaria):

    def buscar(self, elementos: list, elemento: int) -> int:
        izq = 0
        der = len(elementos) - 1

        while izq <= der:
            medio = (izq + der) // 2

            if elementos[medio] == elemento:
                return medio  # El elemento ya está en la lista en esta posición.
            elif elementos[medio] < elemento:
                izq = medio + 1
            else:
                der = medio - 1
        # Cuando no se encuentra el elemento, izquierda apunta a la
        # posición de inserción.
        return izq