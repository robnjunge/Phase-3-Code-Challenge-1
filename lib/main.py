def is_balanced(expression):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False



def remove_duplicates(sequence):
    seen = set()
    result = []

    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Test case
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

import string

def word_frequency(sentence):
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

