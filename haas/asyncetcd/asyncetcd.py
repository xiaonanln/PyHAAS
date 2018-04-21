
import sys
import time
import etcd
import threading
import queue
import asyncio
import traceback
from .. import globals

etcdManThread = None

OP_GET = 1
OP_SET = 2

class EtcdManThread(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.client = etcd.Client(host=self.host, port=self.port)
		self.requestQueue = queue.Queue()

	def addRequest(self, req):
		self.requestQueue.put( req )

	def run(self):
		loop = globals.loop
		while True:
			try:
				self.loop_once(loop)
			except Exception as ex:
				traceback.print_exc()
				time.sleep(1)

	def loop_once(self, loop):
		f, op, *args = self.requestQueue.get()
		try:
			if op == OP_GET:
				res = self.client.get( args[0] )
			elif op == OP_SET:
				key, val = args
				res = self.client.set(key, val)
			else:
				raise RuntimeError("unknown etcd operation: %s", op)
		except Exception as ex:
			loop.call_soon_threadsafe(f.set_exception, ex)
		else:
			loop.call_soon_threadsafe(f.set_result, res)

	def assureConnected(self):
		if self.client is None:
			print('connected etcd: %s ...' % self.client, file=sys.stderr)

def SetEtcdAddress(host, port):
	global etcdManThread
	etcdManThread = EtcdManThread( host, port )
	etcdManThread.setDaemon(True)
	etcdManThread.start()

async def Set( key, val ):
	f = asyncio.Future()
	etcdManThread.addRequest( (f, OP_SET, key, val) )
	res = await f
	return res

async def Get(key):
	f = asyncio.Future()
	etcdManThread.addRequest( (f, OP_GET, key) )
	res = await f
	return res
