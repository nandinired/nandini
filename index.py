import json
import os
import shutil
import boto3
def lambda_handler(event, context):
    # TODO implement
    # api-endpoint
  source = 'develop/'
  dest1 = '/mnt/access'
  files = os.listdir(source)
  for f in files:
    shutil.copy(source+f, dest1)
