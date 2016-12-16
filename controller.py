import json
import logger


commands = []
responses = []
events = []



try:
    with open('base.json') as data_file:
        data = json.load(data_file)
        debug = data['debug']
        verbose = data['verbose']
        repository_url = data['repository_url']
except Exception as e:
    print  'Error reading config: ' + repr(e)