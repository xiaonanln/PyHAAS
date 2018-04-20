import tornado.ioloop
import tornado.web
import haas
from fib import fib
from haas import logging

class MainHandler(tornado.web.RequestHandler):
	async def get(self):
		n = int(self.get_argument('n', '1'))
		res = fib(n)
		self.write(str(res))

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

class WebService(haas.Service):

	async def run(self):
		app = make_app()
		app.listen(25000)
		logging.info('Listening on localhost:25000 ...')
