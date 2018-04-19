# -*- coding: utf8 -*-

import abc

class Service(abc.ABC):
	"""Base class for services"""

	def __init__(self):
		pass

	@abc.abstractmethod
	async def run(self):
		pass
