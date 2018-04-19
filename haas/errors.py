

class RegisterError(RuntimeError):
    def __init__(self, className):
        RuntimeError.__init__(self, 'Service %s is registered multiple times' % className)


