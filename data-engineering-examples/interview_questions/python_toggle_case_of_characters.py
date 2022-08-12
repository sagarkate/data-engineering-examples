# Problem Statement:    
#   Toggle the case of the alphabets in the given string.
#   Ignore the numeric and special characters.

# Solution#1:
def toggle_case1(input_str: str) -> str:
    result = []
    for char in input_str:
        if 65 <= ord(char) <= 90:
            result.append(chr(ord(char) + 32))
        elif 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)
    
    return ''.join(result)

# Solution#2:
def toggle_case2(input_str: str) -> str:
    result = [
        chr(ord(char) + 32) if 65 <= ord(char) <= 90 
        else chr(ord(char) - 32) if 97 <= ord(char) <= 122
        else char for char in input_str
        ]
    
    return ''.join(result)

def main():
    input_str = 'Abc123Xyz'
    print(f"Input String: {input_str}")
    print(f"Toggle Cased String using Solution#1: {toggle_case1(input_str)}")
    print(f"Toggle Cased String using Solution#2: {toggle_case2(input_str)}")

if __name__ == "__main__":
    main()
