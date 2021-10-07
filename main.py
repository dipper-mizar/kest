from paste.deploy import loadapp
from wsgiref.simple_server import make_server

import os

import wsgi


class Controller(object):
    def __init__(self):
        pass

    def test(self, req):
        print('req: ', req)
        return [b'Hello World']


class MyRouterApp(wsgi.Router):
    def __init__(self, mapper):
        controller = Controller()
        mapper.connect('/test', controller=wsgi.Resource(controller), action='test', conditions={'method': ['GET']})
        super(MyRouterApp, self).__init__(mapper)


# class ShowVersion(object):
#     '''
#     app
#     '''
#
#     def __init__(self, version):
#         self.version = version
#
#     def __call__(self, environ, start_response):
#         res = Response()
#         res.status = '200 OK'
#         res.content_type = "text/plain"
#         content = []
#         content.append("%s\n" % self.version)
#         res.body = '\n'.join(content)
#         return res(environ, start_response)

    # @classmethod
    # def factory(cls, global_conf, **kwargs):
    #     print('factory')
    #     print('kwargs:', kwargs)
    #     return ShowVersion(kwargs['version'])


if __name__ == '__main__':
    configname = 'paste.ini'
    appname = 'common'

    print('listen on 8000...')

    wsgi_app = loadapp('config:%s' % os.path.abspath(configname), appname)

    httpd = make_server('127.0.0.1', 8000, wsgi_app)
    httpd.serve_forever()
