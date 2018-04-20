def hello():
    print('hello', 'haas')

from .haas import Register, Run, SetEtcdAddress
from .Service import Service

__all__ = ['Service', 'Register', 'Run', 'SetEtcdAddress']