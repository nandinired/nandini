import json
import logging
import boto3
import pycurl
import StringIO



def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.debug(json.dumps(event))
    response2 = StringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://www.google.com')
    c.setopt(c.WRITEFUNCTION, response.write)
    c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
    c.setopt(c.POSTFIELDS, '@request.json')
    c.perform()
    c.close()
    logger.info(response2.getvalue())
    response2.close()

    codepipeline = boto3.client('codepipeline')
    s3 = boto3.client('s3')
    job_id = event['CodePipeline.job']['id']

    try:
        logger.info(job_id)
        response1 = codepipeline.list_pipelines()
        logger.info(response1)
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
