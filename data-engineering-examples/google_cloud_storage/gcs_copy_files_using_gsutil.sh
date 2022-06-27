# Copy local file to GCS Bucket using gsutil
gsutil cp ./data.csv gs://gcp-practice-123/single-file-copy/

# Copy multiple files to GCS Bucket using gsutil
gsutil cp -r ./multiple-files/*.csv gs://gcp-practice-123/multiple-files-copy/

# run this script in cloud shell or local gcloud sdk using below command
# bash gcs_copy_files_using_gsutil.sh
