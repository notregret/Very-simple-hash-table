class Table:
    def display_hash_table(self):
        for i in range(len(self.hashtable)):
            print(i, end=': ')

            for j in self.hashtable[i]:
                print(j, end=' ')
            print()

    def __init__(self):
        self.main_number = int(input())
        self.HashTable = [i for i in input().split()]
        self.hashtable = [[] for i in self.HashTable]
        self.insert()

    def Hashing(self, keyvalue):
        return keyvalue % self.main_number

    def insert(self):
        for i in self.HashTable:
            hash_key = self.Hashing(int(i))
            self.hashtable[hash_key].append(i)
        self.display_hash_table()


Table()

