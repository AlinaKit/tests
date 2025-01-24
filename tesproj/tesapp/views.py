import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Defs
def index(request):
    logger.info('Accessed: index page')
    return HttpResponse('Hello. Welcome to test server.')

def about(request):
    try:
        res = 1 / 0
    except Exception as ex:
        logger.exception(f'Error: {ex}')
        return HttpResponse('Wrong!')
    else:
        logger.debug('Accessed: about page')
        return HttpResponse('About server')

# Lines
