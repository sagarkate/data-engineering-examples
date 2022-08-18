# Code is copied from below github url for backup
# https://gist.github.com/rajathithan/6bcc735f9fc810f2c9e5d8459fcac95f#file-identify-the-tollbooth-culprit-py

# Code is explained in below medium article
# https://medium.com/analytics-vidhya/how-to-run-a-dataflow-job-in-google-cloud-dc0d57ca7a7c

# Make sure you create below required GCS buckets in your GCP project.
# gs://gcp-practice-101-squirrelwink/input/
# gs://gcp-practice-101-squirrelwink/output/
# gs://gcp-practice-101-squirrelwink/temp/
# gs://gcp-practice-101-squirrelwink/staging/

# Copy below files in input bucket
# tollbooth_logs.csv
# tollbooth_check_file.csv

# Running the Code in Cloud Shell or gcloud sdk
# python3 google_dataflow_analyticsvidhya_find_tollbooth_culprit.py --project <your-project-id>

# Author Rajathithan Rajasekar
# Date 03/07/2021 
# Dataset courtesy - Turalabs

import sys
import os
import logging
import argparse
from datetime import datetime
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.options.pipeline_options import SetupOptions

# setup python logging
logging.basicConfig(format='[%(levelname)-8s] [%(asctime)s] [%(module)-35s][%(lineno)04d] : %(message)s', level=logging.INFO)
logger = logging

TOLLBOOTH_HEADERS = 'date,tollbooth,license_plate,cornsilk,slate_gray,navajo_white'
CHECK_HEADERS = 'tollbooth,month,total'

# Create a dictonary of values
def parse_csv(line, headers):
    values = [v.strip(' "\n') for v in str(line).split(',')]
    keys = headers.split(',')
    return dict(zip(keys, values))

# Create tuple key Value pairs
def tuple_csv(line, headers):
    values = [v.strip(' "\n') for v in str(line).split(',')]
    return (int(values[0]), values[1]), float(values[2])

# Create key Value pairs
def key_by_tollbooth_month(element):
    return (int(element['tollbooth']), element['month']), float(element['total'])

# Identify the difference amount
def finddifference(element):
    return element[0] , (element[1][0][0]-element[1][1][0])

# Filter the nonzero values
def filternonzero(element):
    if element[1] != 0:
        element =  (element[0][0] , element[1])
        element = ','.join([str(k) for k in element])
        return element

# Identify the total amount swindled
def identifyculprit(element):
    t = 0
    toll = 0 
    for x in element:
        if x is not None:
            l = x.split(',')
            toll = l[0]
            t = t + float(l[1])
    return f"Total amount swindled by tollbooth- {toll} for the entire year is ${t} "
        
# Append the dictionary with total price and month
class ParseRecordsAndAddTotals(beam.DoFn):
    
    def process(self, element, nutprices, *args, **kwargs):
        # convert values into correct data types
        record_date = datetime.strptime(element['date'], '%Y.%m.%d')  # parse date
        element['tollbooth'] = int(element['tollbooth'])
        element['cornsilk'] = int(element['cornsilk'])
        element['slate_gray'] = int(element['slate_gray'])
        element['navajo_white'] = int(element['navajo_white'])

        # add calculated columns: total toll, week of year, and month
        element['total'] = (
                (nutprices['cornsilk'] * element['cornsilk']) +
                (nutprices['slate_gray'] * element['slate_gray']) +
                (nutprices['navajo_white'] * element['navajo_white'])
        )
        element['week'] = record_date.isocalendar()[1]      # week number in year
        element['month'] = record_date.strftime("%Y.%m")

        yield element


def run():

    print("Identify the toll-culprit from the Town of Squirrel-wink Bureau Of Tolls and Nuts Affair")

    parser = argparse.ArgumentParser(description="Town of Squirrel-wink Bureau Of Tolls and Nuts Affair")

    parser.add_argument('-i', '--input', 
                        type=str,
                        default='gs://gcp-practice-101-squirrelwink/input/',
                        help='Input Path')

    parser.add_argument('-o', '--output', 
                        type=str,
                        default='gs://gcp-practice-101-squirrelwink/output/',
                        help='Output Path')
    
    parser.add_argument('-s','--staging_location', 
                        dest='staging_location', 
                        required=False,
                        default='gs://gcp-practice-101-squirrelwink/staging/',
                        help='staging_location')

    parser.add_argument('-r','--region', 
                        dest='region', 
                        required=False, 
                        default='us-central1',
                        help='Region')

    parser.add_argument('-t','--temp_location', 
                        dest='temp_location', 
                        required=False,
                        default='gs://gcp-practice-101-squirrelwink/temp/',
                        help='temp location')

    parser.add_argument('--project', 
                        dest='project', 
                        required=True, 
                         help='Project name')

    parser.add_argument('--runner', 
                        dest='runner', 
                        required=False, 
                        default='DataflowRunner',
                        help='Runner Name')

    parser.add_argument('--jobname', 
                        dest='job_name', 
                        required=False, 
                        default='tollboothculprit',
                        help='jobName')
    

    known_args, beam_args = parser.parse_known_args(sys.argv)

    pipeline_options = {
    'input': known_args.input,
    'output': known_args.output,
    'project': known_args.project,
    'staging_location': known_args.staging_location,
    'runner': known_args.runner,
    'job_name': known_args.job_name,
    'region': known_args.region,
    'temp_location': known_args.temp_location,
    }

    # construct pipeline and run
    options = PipelineOptions.from_dictionary(pipeline_options)
    options.view_as(SetupOptions).save_main_session = True

    with beam.Pipeline(options=options) as pipeline:


        # Create a Pcollection of nut prices
        logger.info("creating the inflated toll fees")
        nut_prices = (pipeline
                        | "Create nut prices" >> beam.Create([
                            ('cornsilk',2.0),
                            ('slate_gray',3.5),
                            ('navajo_white',7.0),
                        ])
        )

        # read input file, separate csv columns, parse and add totals
        # Create a Pcollection of the actual records
        def records_pipeline(csvfile):
            return (
                pipeline
                   | "Read toll records" >> beam.io.ReadFromText(os.path.join(known_args.input, csvfile), skip_header_lines=1)
                   | "Create the dictionary" >> beam.Map(parse_csv, headers=TOLLBOOTH_HEADERS)
                   | "Calculate the prices" >> beam.ParDo(ParseRecordsAndAddTotals(),nutprices=beam.pvalue.AsDict(nut_prices))
                   | "Pair month & booth" >> beam.Map(key_by_tollbooth_month)      
                   | "Do summation by Key" >> beam.CombinePerKey(sum)
            )

        # Create a Pcollection of the expected records
        def checkrecords_pipeline(csvfile):
            return (
                pipeline
                    | "Read check records" >> beam.io.ReadFromText(os.path.join(known_args.input, csvfile),skip_header_lines=1)
                    | "Convert to kv pairs" >> beam.Map(tuple_csv, headers=CHECK_HEADERS)

            )
 
        logger.info("reading tollboth logs csv file and parsing records")
        records = records_pipeline('tollbooth_logs.csv')

        logger.info("reading tollboth check csv file and parsing records")
        checkrecords =  checkrecords_pipeline('tollbooth_check_file.csv')

        logger.info("Combining pcollections to identify the difference")
        # Combine both the pcollections and CoGroupByKey 
        results = (
                    (records, checkrecords)  
                    | 'group_by_name' >> beam.CoGroupByKey() 
                    | "find total diff" >> beam.Map(finddifference)
                    | "filter non-zero" >> beam.Map(filternonzero)
                    | "Convert to a list" >> beam.combiners.ToList() 
                    | "Identify the total" >> beam.Map(identifyculprit)
                    | "Write to GCS file" >> beam.io.WriteToText(os.path.join(known_args.output, "swindled-amount"),file_name_suffix='.txt')
        )

if __name__ == '__main__':
    run()