import queue

class AUAStudent:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print ('New score:'), description
        return
    def cmp(self, other):
        return (self.priority, other.priority)

def main():
    q = queue.PriorityQueue()

    q.put(AUAStudent(81, 'Mid-level score'))
    q.put(AUAStudent(120, 'Low-level score'))
    q.put(AUAStudent(60, 'Important score'))

    while not q.empty():
        next_score = q.get()
        print('Processing score:'), next_score.description

main()