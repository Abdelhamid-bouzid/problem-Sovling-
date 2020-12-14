import collections

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.__num_list = collections.defaultdict(int)


    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.__num_list[number] += 1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if len(self.__num_list) == 0:
            return False
        else:
            for entries in self.__num_list.keys():
                target = value - entries
                if (target in self.__num_list) and (entries != target or self.__num_list[target] > 1):
                    return True
            return False
