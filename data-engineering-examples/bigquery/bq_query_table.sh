# Query table using "bq query" command
bq query \
--use_legacy_sql=false \
'SELECT * FROM test_dataset.test_table1'
