# File:     priorityQueues.py
# Purpose:  implement our  version of a priority queue
#           each item has data and a priority for example 
#           (5, 'hat') (3, 'flu') (7, 'cat'), (1, 'bat'), (3, 'sat')
#           higher value means higher priority
# Author:   Adelaida A. Medloc4
# Date:     2/18/2025

# Desired interface: enqueue()/put(), dequeue()/get(), 
# clear(), isEmpty(), len(), str()
class priorityQ():
    # constructor
    def __init__(self):
        self.__theList = []
    
    # setters
    # add element to the end of the queue
    # item is a tuple: (priority, data)
    def put(self, item):
        self.__theList.append(item)
    
    # remove & return an elements from queue according to their priority
    def get(self):
        maximum = 0 # assume item at index 0 has highest priority
        for i in range(len(self.__theList)) :
            if self.__theList[i][0] > self.__theList[maximum][0]:
                maximum = i
        
        a = self.__theList.pop(maximum)
        return a
    
    # remove all elements from queue
    def clear(self):
        self.__theList = []
    
    # getters
    # check if queue is empty    
    def isEmpty(self):
        if len(self.__theList) == 0:
            return True
        else:
            return False

    # overloaded operators
    def __str__(self):
        s = ''
        for i in range(0, len(self.__theList)) :
            s = s + str(self.__theList[i][1]) + '\t'
        return s
    
    def __len__(self):
        return( len(self.__theList) )
    
# Testing our queue implementation
if __name__ == '__main__' :
    print('Testing our priority queue implementation')
    print('-----------------------------------------')
    
    # create a display a new priority queue
    tasks = priorityQ()
    print('Here is our empty priority queue:')
    print(tasks)

    # add some items
    tasks.put((1, 'play video games'))
    tasks.put((2, 'sleep'))
    tasks.put((3, 'study for midterm'))
    tasks.put((4, 'attend class'))
    
    # process the queue
    if not tasks.isEmpty() :
        print('Here are our tasks for the day:')
        print(tasks)
        
        print('There are', len(tasks), 'tasks in the queue.\n')
    
        # get item with highest priority from the queue
        topPriority = tasks.get() 
        print('Do this first:', end = ' ')
        print(topPriority[1])
        
        # print the rest of the queue
        print('\nHere are the rests of the tasks for the day:')
        print(tasks)
        