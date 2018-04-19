import sys
import asyncio
from .errors import RegisterError

try:
    import uvloop
except ImportError:
    print('uvloop is not used', file=sys.stderr)
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

registeredServices = {}

def Run():
    loop = asyncio.get_event_loop()
    loop.run_forever()

def Register(serviceClass):
    if serviceClass.__name__ in registeredServices:
        raise RegisterError(serviceClass.__name__)
    registeredServices[serviceClass.__name__] = serviceClass
