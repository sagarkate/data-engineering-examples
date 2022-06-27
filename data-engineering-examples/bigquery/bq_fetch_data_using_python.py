# Below Code will help us understand how to access BigQuery table data from Python script

from google.cloud import bigquery

PROJECT_ID = "gcp-practice-123"
client = bigquery.Client(project=PROJECT_ID)
query_job = client.query('''
    SELECT
        name, city
    FROM test_dataset.test_table1
''')
# client.query() returns QueryJob object
# QueryJob.result() returns a RowIterator which we can use to iterate over rows if that's what we want
# Each row is a Row Object.

# if we want to work on pandas dataframe, 
# we can call to_dataframe() method on QueryJob object to get pandas dataframe
dataframe = query_job.to_dataframe()

# Print First few rows of a pandas df
dataframe.head()

# Print last few rows from a pandas df
dataframe.tail()

# Get the summary of numeric columns of pandas dataframe
dataframe.describe()
