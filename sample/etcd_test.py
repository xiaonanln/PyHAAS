
import haas
from haas import asyncetcd
from haas import logging
import asyncio

class EtcdTestService(haas.Service):
	async def run(self):
		while True:
			try:
				setRes = await asyncetcd.Set( '/test_key', 'test_val' )
				logging.info('set etcd ok: %s', setRes)
			except asyncio.CancelledError as ex:
				logging.error('set error: %s', ex)
			except Exception as ex:
				logging.error('set error: %s', ex)

			try:
				getRes = await asyncetcd.Get('/test_key')
				logging.info('get etcd ok: %s', getRes)
			except asyncio.CancelledError as ex:
				logging.error('get error: %s', ex)
			except Exception as ex:
				logging.error('get error: %s', ex)

			await asyncio.sleep(1.0)