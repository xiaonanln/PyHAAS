import tornado.ioloop
import tornado.web
import haas
from haas import logging

service = None

class MainHandler(tornado.web.RequestHandler):
	async def get(self):
		n = int(self.get_argument('n', '1'))
		res = await service.call( 'FibService', 'fib', n )
		self.write(str(res))

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

class WebService(haas.Service):

	async def run(self):
		global service
		service = self

		app = make_app()
		app.listen(25000)
		logging.info('Listening on localhost:25000 ...')
