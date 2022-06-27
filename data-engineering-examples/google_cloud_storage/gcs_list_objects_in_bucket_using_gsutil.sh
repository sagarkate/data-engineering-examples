# List the objects from GCS Bucket using gsutil
gsutil ls gs://gcp-practice-123/

# Recursively List all the objects in a bucket
gsutil ls gs://gcp-practice-123/*
# or
gsutil ls -r gs://gcp-practice-123/

<<output

@cloudshell:~ (gcp-practice-)$ gsutil ls gs://gcp-practice-123/
gs://gcp-practice-123/multiple-files-copy/
gs://gcp-practice-123/single-file-copy/


@cloudshell:~ (gcp-practice-)$ gsutil ls gs://gcp-practice-123/*
gs://gcp-practice-123/multiple-files-copy/:
gs://gcp-practice-123/multiple-files-copy/
gs://gcp-practice-123/multiple-files-copy/data1.csv
gs://gcp-practice-123/multiple-files-copy/data2.csv
gs://gcp-practice-123/multiple-files-copy/data3.csv
gs://gcp-practice-123/multiple-files-copy/data4.csv

gs://gcp-practice-123/single-file-copy/:
gs://gcp-practice-123/single-file-copy/
gs://gcp-practice-123/single-file-copy/data.csv


@cloudshell:~ (gcp-practice-)$ gsutil ls -r gs://gcp-practice-123/
gs://gcp-practice-123/multiple-files-copy/:
gs://gcp-practice-123/multiple-files-copy/
gs://gcp-practice-123/multiple-files-copy/data1.csv
gs://gcp-practice-123/multiple-files-copy/data2.csv
gs://gcp-practice-123/multiple-files-copy/data3.csv
gs://gcp-practice-123/multiple-files-copy/data4.csv

gs://gcp-practice-123/single-file-copy/:
gs://gcp-practice-123/single-file-copy/
gs://gcp-practice-123/single-file-copy/data.csv

output
