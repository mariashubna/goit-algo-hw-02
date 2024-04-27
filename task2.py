from collections import deque

def polindrome(string):
    input_string = string.lower().replace(" ", "")
    d = deque(input_string)

    true_box = 0
    while len(d) > 1:
        if d.popleft() != d.pop():
            return 'Рядок не є паліндромом'
        else:
            true_box += 1

    if len(input_string) % 2 == 0 and true_box == len(input_string) // 2:
        return 'Рядок є паліндромом'
    
    elif len(input_string) % 2 == 1 and true_box == (len(input_string) - 1) // 2:
        return 'Рядок є паліндромом'

print(polindrome('діід в діід'))
