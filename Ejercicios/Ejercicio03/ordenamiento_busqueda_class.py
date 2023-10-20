# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:04:18 2023

@author: Fernando
"""

from abc import ABC, abstractmethod


class OrdenableIterativoAbstractClass(ABC):

    @abstractmethod
    def ordenar(elementos):
        pass

    def intercambiar(self, elementos, i, j):
        elementos[i], elementos[j] = elementos[j], elementos[i]


class QuickSortNombre(OrdenableIterativoAbstractClass):

    def dividir_elementos(self, elementos):
        pivote = elementos[0].nombre
        pos_izq = 1
        pos_der = len(elementos) - 1

        while True:
            while pos_izq <= pos_der and elementos[pos_izq].nombre <= pivote:
                pos_izq += 1
            while pos_izq <= pos_der and elementos[pos_der].nombre >= pivote:
                pos_der -= 1
            if pos_der < pos_izq:
                break

            else:
                self.intercambiar(elementos, pos_izq, pos_der)
        self.intercambiar(elementos, 0, pos_der)

        return pos_der

    def ordenar(self, elementos):
        if len(elementos) > 1:
            pos_pivote = self.dividir_elementos(elementos)
            elementos[:pos_pivote] = self.ordenar(elementos[:pos_pivote])
            elementos[pos_pivote +
                      1:] = self.ordenar(elementos[pos_pivote + 1:])

        return elementos


class QuickSortNumero(OrdenableIterativoAbstractClass):

    def dividir_elementos(self, elementos):
        pivote = elementos[0].numero
        pos_izq = 1
        pos_der = len(elementos) - 1

        while True:
            while pos_izq <= pos_der and elementos[pos_izq].numero <= pivote:
                pos_izq += 1
            while pos_izq <= pos_der and elementos[pos_der].numero >= pivote:
                pos_der -= 1

            if pos_der < pos_izq:
                break

            else:
                self.intercambiar(elementos, pos_izq, pos_der)
        self.intercambiar(elementos, 0, pos_der)

        return pos_der

    def ordenar(self, elementos):
        if len(elementos) > 1:
            pos_pivote = self.dividir_elementos(elementos)
            elementos[:pos_pivote] = self.ordenar(elementos[:pos_pivote])
            elementos[pos_pivote +
                      1:] = self.ordenar(elementos[pos_pivote + 1:])

        return elementos


class BusquedaBinaria(ABC):

    @abstractmethod
    def buscar(self):
        pass


class BuscarNombre(BusquedaBinaria):

    def buscar(self, elementos, elemento):
        izq = 0
        der = len(elementos) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if elementos[medio].nombre == elemento:
                return medio
            elif elementos[medio].nombre < elemento:
                izq = medio + 1
            else:
                der = medio - 1

        return -1  # Si el elemento no se encuentra en el arreglo


class BuscarNumero(BusquedaBinaria):

    def buscar(self, elementos, elemento):
        izq = 0
        der = len(elementos) - 1
        while izq <= der:
            medio = (izq + der) // 2
            if elementos[medio].numero == elemento:
                return medio
            elif elementos[medio].numero < elemento:
                izq = medio + 1
            else:
                der = medio - 1

        return -1  # Si el elemento no se encuentra en el arreglo
