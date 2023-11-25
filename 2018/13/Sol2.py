from heapq import heappush, heappop
import heapq


def load_data():
    graph = {}
    carts = []
    data = open('input.txt', 'r').readlines()
    for y, line in enumerate(data):
        for x, tile in enumerate(line):
            if tile in ['>', '<', 'v', '^']:
                carts.append([tile, x, y, 0])

            if tile in ['-', '>', '<']:
                graph[x, y, '>'] = (0, (x+1, y))
                graph[x, y, '<'] = (0, (x-1, y))
            elif tile in ['|', 'v', '^']:
                graph[x, y, '^'] = (0, (x, y-1))
                graph[x, y, 'v'] = (0, (x, y+1))
            elif tile == '\\':
                graph[x, y, '^'] = (1, (x-1, y, '<'))
                graph[x, y, '>'] = (1, (x, y+1, 'v'))
                graph[x, y, 'v'] = (1, (x+1, y, '>'))
                graph[x, y, '<'] = (1, (x, y-1, '^'))
            elif tile == '/':
                graph[x, y, '^'] = (1, (x+1, y, '>'))
                graph[x, y, '>'] = (1, (x, y-1, '^'))
                graph[x, y, 'v'] = (1, (x-1, y, '<'))
                graph[x, y, '<'] = (1, (x, y+1, 'v'))
            elif tile == '+':
                options = [(x+1, y, '>'), (x, y-1, '^'), (x-1, y, '<'), (x, y+1, 'v')]
                graph[x, y, '^'] = (2, options[2::-1])
                graph[x, y, '>'] = (2, options[1::-1] + options[-1:])
                graph[x, y, 'v'] = (2, options[:1] + options[-1:1:-1])
                graph[x, y, '<'] = (2, options[-1:0:-1])
    return graph, carts


def main():
    graph, unordered_carts = load_data()
    carts = {}
    for tile, x, y, d in unordered_carts:
        carts[x, y] = (tile, d)
    
    step = 0
    while True:
        positions = sorted((x + y * 1e5, x, y) for x, y in carts.keys())
        step += 1
        deleted = set()
        for _, x, y in positions:
            if (x, y) in deleted:
                continue
            tile, d = carts[x, y]
            match graph[x, y, tile]:
                case (0, (nx, ny)):
                    if (nx, ny) in carts:
                        deleted.add((nx, ny))
                        del carts[x, y]
                        del carts[nx, ny]
                    else:
                        del carts[x, y]
                        carts[nx, ny] = (tile, d)
                case (1, (nx, ny, ntile)):
                    if (nx, ny) in carts:
                        deleted.add((nx, ny))
                        del carts[x, y]
                        del carts[nx, ny]
                    else:
                        del carts[x, y]
                        carts[nx, ny] = (ntile, d)
                case (2, paths):
                    nx, ny, ntile = paths[d]
                    d += 1
                    d %= 3
                    if (nx, ny) in carts:
                        deleted.add((nx, ny))
                        del carts[x, y]
                        del carts[nx, ny]
                    else:
                        del carts[x, y]
                        carts[nx, ny] = (ntile, d)
                case _:
                    print('ERROR')

        items = list(carts.keys())
        if len(items) == 1:
            return items[0]



if __name__ == '__main__':
    x, y = main()
    print(f'{x},{y}')

