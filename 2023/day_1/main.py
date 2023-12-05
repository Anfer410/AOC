test="""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test2="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def read_input(file="input.txt"):
    with open(file) as f:
        lines = f.readlines()
        content = []
    for line in lines:
        content.append(line.strip())
    
    return(content) 



def transform_words_to_digits(line):
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three","t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7even")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")
    
    return line


def calculate_calibration(task_input, transform=False):
    import timeit
    start = timeit.default_timer()
    calibration=0
    for line in task_input:
        if transform:
            line=transform_words_to_digits(line)
        digits=[]
        for char in line:
            if char.isnumeric():
                digits.append(char)
        
        if len(digits) == 1:
            digits.append(digits[0])
        calibration = calibration + int("".join([digits[0],digits[-1]]))
    stop = timeit.default_timer()
    print(f"Execution time: {stop-start}")
    return calibration



def main():
    task_input=read_input()
    # task_input=test2.splitlines()
    
    print( f"Task 1: {calculate_calibration(task_input)}")
    print( f"Task 2: {calculate_calibration(task_input, True)}")
    

if __name__ == "__main__":
    main()