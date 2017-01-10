import heapq


def PQsort(ilist):
    queue = PriorityQueue()
    for i in ilist:
        queue.push(i, i)

    res =[]
    while not queue.isEmpty():
        res.append(queue.pop())

    return res



class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        tup = (priority, item)
        heapq.heappush(self.heap, tup)
        self.count += 1

    def pop(self):
        res = heapq.heappop(self.heap)
        self.count -= 1
        return res[1]

    def isEmpty(self):
        return self.count == 0

    def update(self, item, priority):
        found = False

        for i in self.heap:
            if item == i[1]:
                #found the item
                if priority < i[0]:
                    #the new item has better priority
                    tup = (priority, item)
                    #we need short circuit evaluation for the next one
                    self.heap = [j for j in self.heap if not (j[1] == item and priority < j[0])]
                    heapq.heapify(self.heap)
                    heapq.heappush(self.heap, tup)
                    found = True
                    break   #break only if found instance of item has lower priority

        if not found:
            self.push(item, priority)
