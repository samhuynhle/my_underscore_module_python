class Underscore:
    def map(self, iterable, callback):
        for x in range(len(iterable)):
            iterable[x] = callback(iterable[x])
        return iterable

    def find(self, iterable, callback):
        for x in range(len(iterable)):
            if (callback(iterable[x])) == True:
                return iterable[x]
            
    def filter(self, iterable, callback):
        new_list =[]
        for x in range(0, len(iterable), 1):
            if (callback(iterable[x])) == True:
                new_list.append(iterable[x])
        return new_list

    def reject(self, iterable, callback):
        new_list =[]
        for x in range(0, len(iterable), 1):
            if (callback(iterable[x])) == False:
                new_list.append(iterable[x])
        return new_list

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above

print(_.map([1,2,3], lambda x: x*2)) # should return [2,4,6]
print(_.find([1,2,3,4,5,6], lambda x: x>4)) # should return the first value that is greater than 4
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0)) # should return [2,4,6]
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0)) # should return [1,3,5]