#!/usr/bin/python3
"""Ser.. and Des... using XML as alternative of JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Ser... a dictionary to an XML file"""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Des.. on XML file to a dictionary"""

    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
