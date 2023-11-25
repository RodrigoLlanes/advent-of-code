inp = [int(line.rstrip()) for line in open("input.txt")]

card_public_key = inp[0]
door_public_key = inp[1]

card_loop_size = None

door_encryption_key = 1

n = 1
i = 1
while card_loop_size is None:
    n *= 7
    n %= 20201227

    if n == card_public_key:
        card_loop_size = i

    i += 1


for _ in range(card_loop_size):
    door_encryption_key *= door_public_key
    door_encryption_key %= 20201227

print(door_encryption_key)