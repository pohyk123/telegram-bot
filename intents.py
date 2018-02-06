import tfl

# Detect & Process intents here

def detectIntent(message):
    intent = 'No relevant intents detected'
    context = 'No context detected'
    if ('tube' in message and 'status' in message):
        intent = 'Retrieve Tube Status'
        context = ''

    intent = {'intent':intent,'context':context}
    return intent

def processIntent(intent):
    context = intent['context']
    intent = intent['intent']
    message = ''

    if (intent == 'Retrieve Tube Status'):
        tubeStatus = tfl.getTubeStatus()
        for line in tubeStatus:
            message+=line['id']+': '+line['status']
            message+='\n'
    else:
        message = 'No matching intents/contexts found.'

    response = {'message':message}
    return response
