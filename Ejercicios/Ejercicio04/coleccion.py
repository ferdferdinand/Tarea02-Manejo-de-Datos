# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:18:04 2023

@author: HP
"""
from abc import ABC, abstractmethod
from busqueda_binaria import *
from excepciones import *


class ColeccionABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def limpiar(self):
        pass

    @abstractmethod
    def tamanio(self):
        pass

    @abstractmethod
    def eliminar_min(self):
        pass

    @abstractmethod
    def eliminar_max(self):
        pass

    @abstractmethod
    def agregar(self):
        pass

    @abstractmethod
    def buscar_elemento(self):
        pass

    @abstractmethod
    def cuantos(self):
        pass

    @abstractmethod
    def obtener_subcoleccion(self):
        pass

    @abstractmethod
    def obtener_subcoleccion_rango(self):
        pass

    @abstractmethod
    def subcoleccion_sin_repeticion(self):
        pass

    @abstractmethod
    def reemplazar(self):
        pass

    @abstractmethod
    def __eq__(self):
        pass

    @abstractmethod
    def imprimir_ascendentes(self):
        pass

    @abstractmethod
    def imprimir_descendente(self):
        pass


class Coleccion(ColeccionABC):

    def __init__(self):
        self.coleccion = []
        self.elementos = 0

    def esta_vacia(self) -> None:
        return self.elementos == 0

    def limpiar(self) -> None:
        self.coleccion = []  # O(1)
        self.elementos = 0   # O(1)

    def tamanio(self) -> int:
        return self.elementos  # O(1)

    def eliminar_min(self):
        minimo = self.coleccion[0]
        i = 0
        igual = True
        while i < self.tamanio() and igual:
            if self.coleccion[i] == minimo:
                self.coleccion = self.coleccion[i + 1:]
                self.elementos -= 1
                i -= 1
            else:
                igual = False
            i += 1

    def eliminar_max(self):
        maximo = self.coleccion[self.tamanio() - 1]
        i = self.tamanio() - 1
        igual = True
        while i > 0 and igual:
            if self.coleccion[i] == maximo:
                self.coleccion = self.coleccion[:i]
                self.elementos -= 1
            else:
                igual = False
            i -= 1

    def agregar(self, elemento: int):
        indice = BuscarPosicion().buscar(self.coleccion, elemento)
        self.coleccion.insert(indice, elemento)
        self.elementos += 1

    def buscar_elemento(self, elemento: int) -> int:
        return BuscarElemento().buscar(self.coleccion, elemento)

    def cuantos(self, elemento: int) -> int:
        indice = self.buscar_elemento(elemento)
        count = 0
        if indice != -1:
            while indice < self.tamanio() and self.coleccion[indice] == elemento:
                count += 1
                indice += 1
        return count

    def obtener_subcoleccion(self, elemento: int) -> list:
        indice = self.buscar_elemento(elemento)
        if indice != -1:
            return self.coleccion[indice:]
        else:
            raise NoExisteSubcoleccion(elemento)

    def obtener_subcoleccion_rango(self, primer_elemento: int, segundo_elemento: int) -> list:
        indice_1 = BuscarElemento().buscar(self.coleccion, primer_elemento)
        indice_2 = BuscarUltimoElemento().buscar(self.coleccion,
                                                 segundo_elemento)
        if indice_1 != -1 and indice_2 != -1:
            return self.coleccion[indice_1: indice_2+1]
        elif indice_1 == indice_2 == -1:
            raise NoExisteSubcoleccionRango(primer_elemento, segundo_elemento)
        elif indice_1 == -1:
            raise NoExisteSubcoleccionRango(primer_elemento)
        else:
            raise NoExisteSubcoleccionRango(segundo_elemento)

    def subcoleccion_sin_repeticion(self) -> list:
        subcoleccion = []
        for elemento in self.coleccion:
            if elemento not in subcoleccion:
                subcoleccion.append(elemento)
        return subcoleccion

    def reemplazar(self, elemento: int, nuevo: int) -> None:
        count = self.cuantos(elemento)
        if count != 0:
            indice = self.buscar_elemento(elemento)
            self.coleccion = self.coleccion[:indice] + self.coleccion[indice + count:]
            self.elementos -= count
            for i in range(count):
                self.agregar(nuevo)

    def __eq__(self, coleccion: ColeccionABC) -> bool:
        if isinstance(coleccion, Coleccion):
            if self.tamanio() == coleccion.tamanio():
                i = 0
                while i < self.tamanio() and self.coleccion[i] == coleccion.coleccion[i]:
                    i += 1
                return i == self.tamanio()
            return False
        return False

    def imprimir_ascendentes(self) -> None:
        for elemento in self.coleccion:
            if elemento is not None:
                print(elemento)

    def imprimir_descendente(self) -> None:
        for i in range(self.tamanio()-1, -1, -1):
            if self.coleccion[i] is not None:
                print(self.coleccion[i])
