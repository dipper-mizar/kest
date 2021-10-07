from webob import Response
from webob.dec import wsgify
from paste.deploy import loadapp

from wsgiref.simple_server import make_server

import os


@wsgify
def application(req):
    return Response('hello world!\n')


def app_factory(global_config, **local_config):
    return application


if __name__ == '__main__':
    configname = 'paste.ini'
    appname = 'main'

    print('listen on 8000...')

    wsgi_app = loadapp('config:%s' % os.path.abspath(configname), appname)

    httpd = make_server('127.0.0.1', 8000, wsgi_app)
    httpd.serve_forever()
