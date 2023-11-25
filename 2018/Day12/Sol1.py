
def load_data():
    data = open('input.txt', 'r').readlines()
    state = data[0][len('initial state: '):].strip()
    transf = {}
    for line in data[2:]:
        k, v = line.strip().split(' => ')
        transf[k] = v
    return state, transf


def main():
    state, transf = load_data()
    
    state = f'...{state}...'
    min_index = -3
    max_index = len(state) - 1 - 3

    for _ in range(20):
        if state[3] == '#':
            state = '.' + state
            min_index -= 1
        if state[-4] == '#':
            state += '.'
            max_index += 1
        
        new_state = '..'
        for i in range(2, len(state) - 2):
            key = state[i-2:i+3]
            new_state += transf[key]
        new_state += '..'
        state = new_state
    print(sum(v for i, v in enumerate(range(min_index, max_index+1)) if state[i] == '#'))


if __name__ == '__main__':
    main()
