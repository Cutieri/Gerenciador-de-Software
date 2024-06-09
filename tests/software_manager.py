# tests/test_software_manager.py

import pytest
from src.software_manager import SoftwareManager

def test_get_software_list():
    # Crie uma instância de SoftwareManager
    software_manager = SoftwareManager()

    # Chame o método get_software_list
    software_list = software_manager.get_software_list()

    # Verifique se o método get_software_list retorna uma lista
    assert isinstance(software_list, list)

def test_add_software():
    # Crie uma instância de SoftwareManager
    software_manager = SoftwareManager()

    # Crie um software fake
    software = {"name": "Test Software", "version": "1.0"}

    # Chame o método add_software
    software_manager.add_software(software)

    # Verifique se o software foi adicionado à lista
    assert software in software_manager.get_software_list()

def test_remove_software():
    # Crie uma instância de SoftwareManager
    software_manager = SoftwareManager()

    # Crie um software fake
    software = {"name": "Test Software", "version": "1.0"}

    # Adicione o software à lista
    software_manager.add_software(software)

    # Chame o método remove_software
    software_manager.remove_software(software["name"])

    # Verifique se o software foi removido da lista
    assert software not in software_manager.get_software_list()