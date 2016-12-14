import json
from pprint import pprint

debug = False
verbose = False
repository_url = ''

def read():
    try:
        with open('config.json') as data_file:
            data = json.load(data_file)
            debug =  data['debug']
            verbose = data['verbose']
            repository_url = data['repository_url']
    except Exception as e:
        print  'Error reading config: ' + repr(e)

def save():
    pass

def create():
    pass


def setVerbose():

    pass

def setDebug():
    pass

def setRepositoryURL():
    pass



