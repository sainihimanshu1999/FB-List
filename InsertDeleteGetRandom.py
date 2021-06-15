import random
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:
            self.nums.append(val)
            self.dic[val] = len(self.nums)-1
            return True
        return False
            
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            index,last = self.dic[val],self.nums[-1]
            self.nums[index],self.dic[last]=last,index
            self.nums.pop(),self.dic.pop(val,0)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0,len(self.nums)-1)]
        