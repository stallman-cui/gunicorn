# -*- coding: utf-8 -
#
# This file is part of grainbows released under the MIT license. 
# See the NOTICE for more information.

from wsgiref.validate import validator

import eventlet

eventlet.monkey_patch(all=False, os=False, select=True, socket=True)


@validator
def app(environ, start_response):
    """Application which cooperatively pauses 10 seconds before responding"""
    data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))    ]
    print 'request received, pausing 10 seconds'
    eventlet.sleep(10)
    start_response(status, response_headers)
    return iter([data])