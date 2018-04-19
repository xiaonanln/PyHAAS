# -*- coding: utf8 -*-

import abc
import asyncio
from .errors import ServiceError

class Service(abc.ABC):
	"""Base class for services"""

	def __init__(self):
		self.task = None

	def start(self):
		if self.task is not None:
			raise ServiceError('service is already started')

		self.task = asyncio.get_event_loop().create_task(self.run())

	@abc.abstractmethod
	async def run(self):
		pass

	def stop(self):
		self.task.cancel()

class MethodService(Service):
	"""Base class for method services"""
	def __init__(self):
		super(MethodService, self).__init__()
		self.callQueue = asyncio.Queue()

	async def run(self):
		while True:
			call = await self.callQueue.get()
