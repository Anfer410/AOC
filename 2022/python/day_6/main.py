import time

test_inputs = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb",
"bvwbjplbgvbhsrlpgdmjqwftvncz",
"nppdvjthqldpwncqszvftbrmjlhg",
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]


def read_input():
    with open('input.txt') as f:
        file = f.read()
    
    return file


# Brutforce...
def part_1(signal):
    start = time.perf_counter()
    for i in range(len(signal) - 4):
        if signal[i] not in [signal[i+1], signal[i+2], signal[i+3]] and\
           signal[i+1] not in [signal[i], signal[i+2], signal[i+3]] and\
           signal[i+2] not in [signal[i], signal[i+1], signal[i+3]] and\
           signal[i+3] not in [signal[i], signal[i+1], signal[i+2]]:
            print(f'marker {signal[i]} after {i + 4}')
            break
    
    end = time.perf_counter()
    print(f'Task took: {end - start} seconds')
    
    return i + 4
  

# Proper algorithm
def find_start_of_message_marker(signal, size):
    start = time.perf_counter()
    found = False
    
    for i in range(len(signal)-size):
        buffer = []
        
        # check characters
        for j in range(i,i+size):
            if len(buffer) < size and not found :
                if signal[j] not in buffer:
                    buffer.append(signal[j])
                    if len(buffer) == size:
                        print(f'Handshake till {j}, message start at: {j+1}')
                        found = True
                        break 
                else: 
                    # print(f'Duplicate found in range {i}-{j}')
                    break 
            elif not found:
                # print(f'Not found in {i}-{j} range')
                break
    
    end = time.perf_counter()
    print(f'Task took: {end - start} seconds')


def main():
    # signal = test_inputs[0]
    
    signal = read_input()

    # Part 1 - old
    # part_1(signal)

    # Part 1
    find_start_of_message_marker(signal, 4)
    # Part 2
    find_start_of_message_marker(signal, 14)


if __name__ == '__main__':
    main()