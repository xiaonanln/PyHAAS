import sys
import asyncio
import os
from .errors import RegisterError

if os.name == 'posix':
	try:
		import uvloop
	except ImportError:
		print('uvloop is not used', file=sys.stderr)
	else:
		asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
# elif os.name == 'nt':
# 	print('Using', asyncio.ProactorEventLoop.__doc__, file=sys.stderr)
# 	asyncio.set_event_loop(asyncio.ProactorEventLoop())

loop = asyncio.get_event_loop()
registeredServices = {}
runningServices = {}

def Run():
	print('call checkServices later...')
	loop.call_later(1.0, checkServices)
	print('PyHAAS start running ...', file=sys.stderr)
	loop.run_forever()

def Register(serviceClass):
	if serviceClass.__name__ in registeredServices:
		raise RegisterError(serviceClass.__name__)

	registeredServices[serviceClass.__name__] = serviceClass
	runningServices[serviceClass.__name__] = set()

def checkServices():
	try:
		checkServicesImpl()
	finally:
		print('call checkServices later...')
		loop.call_later(1.0, checkServices)

def checkServicesImpl():
	for className, serviceClass in registeredServices.items():
		# print('registered service %s: %s' % (className, serviceClass), file=sys.stderr)
		runningSet = runningServices[className]
		if len(runningSet) < 1:
			s = serviceClass()
			runningSet.add( s )
			s.start()
