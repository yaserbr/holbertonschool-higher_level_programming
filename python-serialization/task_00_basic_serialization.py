#!/usr/bin/env python3
"""This file contain serializattion and de deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Here the function to serialize"""
    with open(filename, "w", encoding="utf-8") as createdFile:
        json.dump(data, createdFile)


def load_and_deserialize(filename):
    """Here the function to deserialize"""
    with open(filename, "r", encoding="utf-8") as loadedFile:
        return json.load(loadedFile)
