from __future__ import print_function
from botocore.exceptions import ClientError
import json
import os
import shutil
import boto3
import traceback
import hashlib
import time
import logging
def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.debug(json.dumps(event))
 
    codepipeline = boto3.client('codepipeline')
    job_id = event['CodePipeline.job']['id']
 
    try:
        raise ValueError('This message will appear in the CodePipeline UI.')
        logger.info('Doing cool stuff!')
        print("hello")
        response = codepipeline.put_job_success_result(jobId=job_id)
        logger.debug(response)
    except Exception as error:
        logger.exception(error)
        response = codepipeline.put_job_failure_result(
            jobId=job_id,
            failureDetails={
              'type': 'JobFailed',
              'message': f'{error.__class__.__name__}: {str(error)}'
            }
        )
        logger.debug(response)
