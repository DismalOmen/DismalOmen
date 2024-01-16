class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Not a negative number!")
        self._capacity = capacity
        self._size =  0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Sorry, too many cookies!")
        elif self.size > self.capacity:
            raise ValueError("Sorry, that size won't work!")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Sorry, too few cookies!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():

    jar = Jar()
    jar.deposit(6)
    jar.withdraw(5)
    print(jar)

if __name__ == "__main__":
    main()