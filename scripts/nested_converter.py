#!/usr/bin/python

import csv
import json
import sys
from collections import defaultdict

'''
To run (from inside this directory):
python nested_converter.py

it should generate the file data/data_race.json

the json format is specified in data/format_spec.json
'''

def main(argv):
    input_file = 'data/data_race.csv'
    output_file = 'data/data_race.json'
    csv_to_json(input_file, output_file)

def csv_to_json(data_file, json_file):
    """ year,county,race,population,misdemeanor,felony,arrest_count """
    output = {}
    with open(data_file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        counties = {}

        for row in reader:
            if row['county'] not in counties:
                counties[row['county']] = {}
                counties[row['county']]['race'] = {}
                counties[row['county']]['years'] = []

            # NB: we assume the years are in order in the CSV
            if not counties[row['county']]['years'] or row['year'] != counties[row['county']]['years'][-1]:
                counties[row['county']]['years'].append(row['year'])

            if row['race'] not in counties[row['county']]['race']:
                counties[row['county']]['race'][row['race']] = defaultdict(list)
            race_dict = counties[row['county']]['race'][row['race']]
            race_dict['population'].append(int(row['population']))
            race_dict['misdemeanor'].append(float(row['misdemeanor']))
            race_dict['felony'].append(float(row['felony']))
            race_dict['arrest_count'].append(int(row['arrest_count']))
        write_json(counties, json_file)

def write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1:])

