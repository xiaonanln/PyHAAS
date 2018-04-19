
import asyncio
import haas

class DummyService1(haas.Service):
	async def run(self):
		while True:
			await asyncio.sleep(1.0)
			print('i am dummy 1 ...')
			
class DummyService2(haas.Service):
	async def run(self):
		while True:
			await asyncio.sleep(1.0)
			print('i am dummy 2 ...')
