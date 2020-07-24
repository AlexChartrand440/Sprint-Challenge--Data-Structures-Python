class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity;
        self.storage = [None] * capacity;
        self.curr = 0;

    def append(self, item):
        self.storage[self.curr] = item;
        self.curr += 1;
        if self.curr >= self.capacity:
            self.curr = 0;
        # if len(self.storage) < self.capacity:
        #     self.storage.append(item);
        # else:
        #     self.storage[self.curr] = item;
        #     print(str(self.curr) + ' - ' + str(len(self.storage)));
        #     if self.curr > self.capacity:
        #         self.curr = 0;
        #     else:
        #         self.curr += 1;

    def get(self):
        returnStorage = [];
        for item in self.storage:
            if item is not None:
                returnStorage.append(item);
        return returnStorage;