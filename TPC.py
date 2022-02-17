import math
class TPC:
    _stop = int(input("Num Breakpoint ->  "))
    pair_list = list(range(2, _stop+1))

    def isPrime(self, num):
        primes = []
        for i in range(2, num, 1):
            if num % i == 0:
                primes.append(i)
        if len(primes) == 0:
            return True
        else:
            return False

    def TwinPairs(self):
        new_primes, twin_primes = [], []
        for num in self.pair_list:
            if self.isPrime(num):
                new_primes.append(num)
            else:
                continue

        for i in range(len(new_primes) - 1):
            if (new_primes[i] - new_primes[i+1]) == -2:
                twin_primes.append([new_primes[i], new_primes[i+1]])
            else:
                print(f"GapSize: {math.fabs(new_primes[i] - new_primes[i+1])} -> {new_primes[i]} & {new_primes[i+1]}")

        print(f"Primes List -> {new_primes}")
        for primes in twin_primes:
            print(f"TwinPrimes -> {primes[0]} & {primes[1]}")

myTPC = TPC()
myTPC.TwinPairs()