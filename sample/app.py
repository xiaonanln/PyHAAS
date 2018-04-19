
import haas
import fib
import dummy
import web

def main():
    # haas.Register(fib.FibService)
    haas.Register(dummy.DummyService1)
    haas.Register(dummy.DummyService2)
    haas.Register(web.WebService)
    haas.SetEtcdAddress( '127.0.0.1', 2379 )
    haas.Run()

if __name__ == '__main__':
    main()
