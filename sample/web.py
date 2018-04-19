import tornado.ioloop
import tornado.web
from tornado import gen
import haas

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument('n', '1'))
        res = fib(n)
        self.write(str(res))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def runwebservice():
    app = make_app()
    app.listen(25000)
    tornado.ioloop.IOLoop.current().start()

class WebService(haas.Service):
    pass