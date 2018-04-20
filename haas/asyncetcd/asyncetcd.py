
import sys
import time
import etcd
import threading
import queue

etcdManThread = None

class EtcdManThread(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port
		self.client = None
		self.requestQueue = queue.Queue()

	def addRequest(self, req):
		pass

	def run(self):
		while True:
			self.assureConnected()

			self.client.set('test_key', 'test_val')
			print('test_key is set to', self.client.get('test_key').value)

			time.sleep(1)

	def assureConnected(self):
		if self.client is None:
			self.client = etcd.Client(host=self.host, port=self.port)
			print('connected etcd: %s ...' % self.client, file=sys.stderr)

def SetEtcdAddress(host, port):
	global etcdManThread
	etcdManThread = EtcdManThread( host, port )
	etcdManThread.setDaemon(True)
	etcdManThread.start()

async def Set( key, val ):
	pass

async def Get(key):
	pass
