# python3
B=13
Q=256

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input = input()
    
    if "I" in input:
        pattern = input().rstrip()
        text = input().rstrip()
    
    if "F" in input:
        fails = input()
        if "a" in fails:
            print("wrong file name")
            return
    with open("./test/06", "r") as f:
        pattern = f.readline().rstrip()
        text = f.readline().rstrip()
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern,text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    global B, Q
    occur = []
    textlength=len(text)
    patternlength=len(pattern)
    patternhash=get_hash(pattern)
    texthash = get_hash(text[:len(pattern)])
    multiplier = 1

    for i in range(textlength - patternlength + 1):
        if patternhash == texthash:
            if pattern == text[i:i+patternlength]:
                occur.append(i)
        if i < textlength - patternlength:
            texthash=(B* (texthash - ord(text[i]) * multiplier) + ord(text[i + patternlength])) % Q


    # and return an iterable variable
    return occur

def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range (m):
        result = (B * result + ord(pattern[i])) % Q
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

