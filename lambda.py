import boto3
import os
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ses_client = boto3.client('ses', region_name='us-east-1')

    # Fetch configurations from environment variables
    sender_email = os.getenv('SENDER_EMAIL', 'your-verified-email@example.com')
    recipient_email = event.get('recipient_email', 'default-recipient@example.com')
    subject = event.get('subject', 'Test Email from AWS Lambda')
    body_text = event.get('body_text', 'This is a test email sent from an AWS Lambda function.')
    body_html = event.get('body_html', """
    <html>
    <head></head>
    <body>
      <h1>Test Email from AWS Lambda</h1>
      <p>This is a test email sent from an AWS Lambda function.</p>
    </body>
    </html>
    """)

    # Log the email details for debugging purposes
    logger.info(f'Sending email from {sender_email} to {recipient_email} with subject "{subject}"')

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=sender_email,
        )
        logger.info(f'Email sent successfully: {response}')
        return {
            'statusCode': 200,
            'body': 'Email sent!',
            'response': response
        }
    except ses_client.exceptions.MessageRejected as e:
        logger.error(f'Email rejected: {str(e)}')
        return {
            'statusCode': 400,
            'body': f'Email rejected: {str(e)}'
        }
    except ses_client.exceptions.MailFromDomainNotVerifiedException as e:
        logger.error(f'Sender email domain not verified: {str(e)}')
        return {
            'statusCode': 400,
            'body': f'Sender email domain not verified: {str(e)}'
        }
    except Exception as e:
        logger.error(f'Error sending email: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Error sending email: {str(e)}'
        }
