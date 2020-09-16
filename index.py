import json
import os
import shutil
import boto3
def lambda_handler(event, context):
  source = 'develop/'
  dest1 = '/mnt/src'
  files = os.listdir(source)
  for f in files:
    shutil.copy(source+f, dest1)
