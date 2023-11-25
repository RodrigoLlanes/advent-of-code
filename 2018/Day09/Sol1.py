
class Marble:
    def __init__(self, v, prev=None, next=None):
        self.value = v
        self.next = next if next is not None else self
        self.prev = prev if prev is not None else self

    def insert_next(self, v):
        self.next = Marble(v, self, self.next)
        self.next.next.prev = self.next
        return self.next

    def pop(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next


if __name__ == "__main__":
    players = 411
    last = 71170

    current_player = 0
    scores = {player: 0 for player in range(players)}
    current = Marble(0)
    for n in range(1, last+1):
        if n % 23 != 0:
            current = current.next.insert_next(n)
        else:
            scores[current_player] += n
            for _ in range(7):
                current = current.prev
            scores[current_player] += current.value
            current = current.pop()

        current_player = (current_player + 1) % players

    print(max(scores.values()))



