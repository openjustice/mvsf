#!/usr/bin/python

import csv
import json
import sys, getopt

'''

To run (from inside this directory):
python data_converter.py -i ../data/data_clean.csv -o ../data/test.json

(from main directory)
python scripts/data_converter.py -i data/data_clean.csv -o data/test.json

'''

def main(argv):
  input_file = ''
  output_file = ''
  try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
      print('data_converter.py -i <path to inputfile> -o <path to outputfile>')
      sys.exit(2)
  for opt, arg in opts:
      if opt == '-h':
          print('data_converter.py -i <path to inputfile> -o <path to outputfile>')
          sys.exit()
      elif opt in ("-i", "--ifile"):
          input_file = arg
      elif opt in ("-o", "--ofile"):
          output_file = arg
  csv_to_json(input_file, output_file)

def csv_to_json(file, json_file):
  csv_rows = []
  with open(file) as csvfile:
    reader = csv.DictReader(csvfile)
    title = reader.fieldnames
    counties = {}

    for row in reader:
      if row['county'] in counties:
        counties[row['county']]['felony'].append([int(row['year']), float(row['felony'])])
        counties[row['county']]['misdemeanor'].append([int(row['year']), float(row['misdemeanor'])])
        counties[row['county']]['population'].append([int(row['year']), int(row['population'])])

      else:
        counties[row['county']] = {'county': row['county']}
        counties[row['county']]['felony'] = [[int(row['year']), float(row['felony'])]]
        counties[row['county']]['misdemeanor'] = [[int(row['year']), float(row['misdemeanor'])]]
        counties[row['county']]['population'] = [[int(row['year']), int(row['population'])]]


    print(counties.values())
    write_json(list(counties.values()), json_file)
     

def write_json(data, json_file):
  with open(json_file, "w") as f:
    f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False))

if __name__ == "__main__":
   main(sys.argv[1:])
    