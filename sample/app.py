
import haas
import fib

def main():
    haas.Register(fib.FibService)
    haas.Run()

if __name__ == '__main__':
    main()
