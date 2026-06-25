import heapq
class priority:
    def __init__(self):
        self.queue = {"cat": [], "dog": []}
        self.offset = 1

    def input(self, lst):
        for each in lst:
            
            name, spec, day, = each
            heapq.heappush(self.queue[spec], (-day, name))

    def printing(self):
        for key, val in self.queue.items():
            print(val)

    def adpot(self, input):
        name, pep, spec = input
        if spec == "dog":
            other = "cat"
        else:
            other = "dog"
        if not self.queue[spec]:
            return self.bring(other)
        return self.bring(spec)

    def bring(self, spec):
        if not self.queue[spec]:
            return None
        day, name = heapq.heappop(self.queue[spec])
        return [name, spec]

    def add(self, input):
        self.offset += 1

        cur = self.offset - 1

        name, spec = input
        heapq.heappush(self.queue[spec], (cur, name))

        


lst = [
    ["Sadie", "dog", 4],
    ["Woof", "cat", 7],
    ["Chirpy", "dog", 2],
    ["Lola", "dog", 1]
]
heap = priority()
heap.input(lst)
heap.printing()
inputs = ["Bob", "Person", "dog"]
print()
print(heap.adpot(inputs))
print()
heap.printing()
heap.add(["floofy", "cat"])
input2 = ["sally", "person","cat"]
print(heap.adpot(input2))
input3 = ["mohammed", "person","cat"]
print(heap.adpot(input3))
input4 = ["rita", "person","cat"]
print(heap.adpot(input4))
print()
heap.printing()
