---
layout:     post
title:      Walkthrough
date:       2016-06-05
Summary:	Walkthrough of how to create such a visualization
---

Are you interested in one of the datasets on the [OpenJustice CA portal][OJ], but you want visualize it differently from their default? This is a walkthrough of how two hackers at the [National Day of Civic Hacking][NDoCH] identified a problem in one of the OpenJustice visualizations, and  created a new, better visualization to improve OpenJustice.

[OJ]: http://openjustice.doj.ca.gov/
[NDoCH]: https://www.eventbrite.com/e/national-day-of-civic-hacking-tickets-25188025061

## Objective: Improve DOJ Visualization

This is the OpenJustice visualization that <a href="https://github.com/saikirandulla" class="github-username">@saikirandulla</a> and <a href="https://github.com/aprilw" class="github-username">@aprilw</a> were looking at:

![msdemeanor vs felony arrests by county](images/existing_chart.png)

It plots [the rates of misdemeanor vs felony arrests by county](http://openjustice.doj.ca.gov/agencies/charts), providing a notion of the spread. They wondered, how has that changed over time? Well, you can filter by year:

![msdemeanor vs felony arrests by county with years filter](images/existing_chart_years.png)


## Limitation

Okay...that provides the information we want, but given the filtering, it makes it hard to view time trends over time. The hackers decided to fix this.

##Inspiration for Improvement

The interactive animation "The Wealth & Health of Nations" suggests one possibility for imporvement: displaying on year at a time, and animating the time parameter:

[![The Wealth & Health of Nations](images/wealth_and_health_of_nations.png)](https://bost.ocks.org/mike/nations/)

##Original JS for visualization


[The JS for original visualization is found here](https://github.com/openjustice/mvsf/blob/master/original_chart_js)

##Changes to the Code

```
Insert the changes to code here
```

There was also a need to create a python script to convert a csv file into the correct json format. Code for this here.
```
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

```


## Final Visualization

This is the result of all the hard work!

![screenshot](images/screenshot.png)

[And a link to the interactive version](http://openjustice.github.io/mvsf/)
