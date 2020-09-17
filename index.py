from __future__ import print_function
from boto3.session import Session

import sys
import os
import zipfile
import json
import urllib
import boto3
import zipfile
import tempfile
import botocore
import traceback
import logging
import io

# Global
AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_SESSION_TOKEN=""
AWS_DEFAULT_REGION=""

print('Loading function')

code_pipeline = boto3.client('codepipeline')
def put_job_success(job, message):
    """Notify CodePipeline of a successful job
    Args:
        job: The CodePipeline job ID
        message: A message to be logged relating to the job status
    Raises:
        Exception: Any exception thrown by .put_job_success_result()
    """
    print('Putting job success')
    print(message)
    code_pipeline.put_job_success_result(jobId=job)

def put_job_failure(job, message):
    """Notify CodePipeline of a failed job
    Args:
        job: The CodePipeline job ID
        message: A message to be logged relating to the job status
    Raises:
        Exception: Any exception thrown by .put_job_failure_result()
    """
    print('Putting job failure')
    print(message)
    code_pipeline.put_job_failure_result(jobId=job, failureDetails={'message': message, 'type': 'JobFailed'})
    
def lambda_handler(event, context):
     try:
        job_id = event['CodePipeline.job']['id']
        job_data = event['CodePipeline.job']['data']
        print(job_data)
        print(job_id)
        if 'continuationToken' in job_data:
            # If we're continuing then the create/update has already been triggered
            # we just need to check if it has finished.
            print("Job is continuing")
        else:
            source = 'develop/'
            dest1 = '/mnt/src'
            files = os.listdir(source)
            for f in files:
                shutil.copy(source+f, dest1)
                print("hello")
            put_job_success(job_id, 'copy complete')
            print("hello")
            break
     except Exception as e:
            # If any other exceptions which we didn't expect are raised
            # then fail the job and log the exception message.
        print('Function failed due to exception.') 
        print(e)
        traceback.print_exc()
        put_job_failure(job_id, 'Function exception: ' + str(e))
     print('Function complete.')   
     return "complete."
