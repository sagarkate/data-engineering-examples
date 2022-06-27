# create dataset using bq command
bq mk test_dataset

bq ls

<<output

@cloudshell:~ (gcp-practice-)$ bash bq_create_dataset.sh
Dataset '<project-id>:test_dataset' successfully created.
 -test_dataset-

output
