
import sys
import etcd
import threading

class EtcdManThread(threading.Thread):
	def __init__(self, host, port):
		threading.Thread.__init__(self)
		self.host = host
		self.port = port

	def run(self):
		self.client = etcd.Client(host=self.host, port=self.port)
		print('connected etcd: %s ...' % self.client, file=sys.stderr)

def SetEtcdAddress(host, port):
	t = EtcdManThread( host, port )
	t.start()
