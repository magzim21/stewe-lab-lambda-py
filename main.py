def lambda_handler(event, context):
    # message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    message = 'Hello World from Python!'  
    return { 
        'message' : message
    }