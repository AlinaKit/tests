import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Defs
def index(request):
    logger.info('Access index page')
    return HttpResponse('Hello. Welcome to test server.')

def about(request):
    return HttpResponse('About server')

# Lines
