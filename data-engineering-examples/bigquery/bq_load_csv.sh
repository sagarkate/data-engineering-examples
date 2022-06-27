# Load CSV into a BigQuery table using "bq load" command
<<syntax
bq load --location location \
--source_format=format \
dataset.table \
path_to_source \
schema

syntax

bq load \
--source_format=CSV \
test_dataset.test_table1 \
gs://gcp-practice-123/single-file-copy/data.csv \
name:STRING,city:STRING
