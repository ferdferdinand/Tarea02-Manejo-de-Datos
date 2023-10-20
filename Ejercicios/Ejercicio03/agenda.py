# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:19:28 2023

@author: Fernando
"""

from abc import ABC, abstractmethod
from ordenamiento_busqueda_class import *


class ContactoABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Contacto(ContactoABC):

    def __init__(self, nombre: str, numero: str):
        self.nombre = nombre
        self.numero = numero

    def __str__(self):
        return f"Nombre: {self.nombre}\n"\
            + f"Número de teléfono: {self.numero}"


class AgendaABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def agregar_contacto(self):
        pass

    @abstractmethod
    def ordenar_nombre(self):
        pass

    @abstractmethod
    def ordenar_numero(self):
        pass

    @abstractmethod
    def buscar_nombre(self):
        pass

    @abstractmethod
    def buscar_numero(self):
        pass


class Agenda(AgendaABC):

    def __init__(self):
        self.agenda = []

    def agregar_contacto(self, contacto: Contacto):
        self.agenda.append(contacto)

    def ordenar_nombre(self):
        QuickSortNombre().ordenar(self.agenda)

    def ordenar_numero(self):
        QuickSortNumero().ordenar(self.agenda)

    def buscar_nombre(self, nombre: str) -> Contacto:
        self.ordenar_nombre()
        indice = BuscarNombre().buscar(self.agenda, nombre)
        if indice != -1:
            return self.agenda[indice]
        return "Contacto no encontrado"

    def buscar_numero(self, numero: str) -> Contacto:
        self.ordenar_numero()
        indice = BuscarNumero().buscar(self.agenda, numero)
        if indice != -1:
            return self.agenda[indice]
        return "Contacto no encontrado"
