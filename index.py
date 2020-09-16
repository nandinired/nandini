from __future__ import print_function
import json
import os
import shutil
import boto3
import traceback
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

def continue_job_later(job, message):
    """Notify CodePipeline of a continuing job

    This will cause CodePipeline to invoke the function again with the
    supplied continuation token.

    Args:
        job: The JobID
        message: A message to be logged relating to the job status
        continuation_token: The continuation token

    Raises:
        Exception: Any exception thrown by .put_job_success_result()

    """

    # Use the continuation token to keep track of any job execution state
    # This data will be available when a new job is scheduled to continue the current execution
    continuation_token = json.dumps({'previous_job_id': job})

    print('Putting job continuation')
    print(message)
    code_pipeline.put_job_success_result(jobId=job, continuationToken=continuation_token)
def lambda_handler(event, context):
   
  try:
        # Extract the Job ID
      job_id = event['CodePipeline.job']['id']
        
        # Extract the Job Data 
      job_data = event['CodePipeline.job']['data']
      source = 'develop/'
      dest1 = '/mnt/src'
      files = os.listdir(source)
      for f in files:
          shutil.copy(source+f, dest1)
      code_pipeline.put_job_success_result(jobId=job_id)
  except Exception as e:
     # If any other exceptions which we didn't expect are raised
     # then fail the job and log the exception message.
     print('Function failed due to exception.')
     print(e)
     traceback.print_exc()
     put_job_failure(job_id, 'Function exception: ' + str(e))
