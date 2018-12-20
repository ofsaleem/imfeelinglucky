'''
This function handles a Slack slash command and echoes the details back to the user.

Follow these steps to configure the slash command in Slack:

  1. Navigate to https://<your-team-domain>.slack.com/services/new

  2. Search for and select "Slash Commands".

  3. Enter a name for your command and click "Add Slash Command Integration".

  4. Copy the token string from the integration settings and use it in the next section.

  5. After you complete this blueprint, enter the provided API endpoint URL in the URL field.


Follow these steps to encrypt your Slack token for use in this function:

  1. Create a KMS key - http://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html.

  2. Encrypt the token using the AWS CLI.
     $ aws kms encrypt --key-id alias/<KMS key name> --plaintext "<COMMAND_TOKEN>"

  3. Copy the base-64 encoded, encrypted key (CiphertextBlob) to the kmsEncyptedToken variable.

  4. Give your function's role permission for the kms:Decrypt action.
     Example:
       {
         "Version": "2012-10-17",
         "Statement": [
           {
             "Effect": "Allow",
             "Action": [
               "kms:Decrypt"
             ],
             "Resource": [
               "<your KMS key ARN>"
             ]
           }
         ]
       }

Follow these steps to complete the configuration of your command API endpoint

  1. When completing the blueprint configuration select "POST" for method and
     "Open" for security on the Endpoint Configuration page.

  2. After completing the function creation, open the newly created API in the
     API Gateway console.

  3. Add a mapping template for the application/x-www-form-urlencoded content type with the
     following body: { "body": $input.json("$") }

  4. Deploy the API to the prod stage.

  5. Update the URL for your Slack slash command with the invocation URL for the
     created API resource in the prod stage.
'''
'''
test block
'''

import boto3
from base64 import b64decode
from urlparse import parse_qs
import logging


expected_token = "REDACTED"
#put token here

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    req_body = event['body']
    params = parse_qs(req_body)
    token = params['token'][0]
    if token != expected_token:
        logger.error("Request token (%s) does not match exptected", token)
        raise Exception("Invalid request token")
    response = "Let me Google that for you! http://google.com/search?q=%s&btnI" % (params['text'][0]).replace(" ", "+")
    return {'text': response, 'response_type': 'in_channel'}
