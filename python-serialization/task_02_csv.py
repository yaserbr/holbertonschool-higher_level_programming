#!/usr/bin/env python3
"""Custom class serialization"""

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, "r") as tempfile:
            tempfile = csv.DictReader(tempfile)
            dictData = list(tempfile)

        with open("data.json", "w", encoding="utf-8") as jsonFile:
            json.dump(dictData, jsonFile)
            return True
    except (Exception):
        return False
