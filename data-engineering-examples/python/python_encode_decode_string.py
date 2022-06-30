import base64

def to_base64_string(message: str) -> str:
    '''
    Convert text to base64 encoded string
    1.  Fetch ASCII decimal value of each character in the input message.
    2.  Convert each decimal value to its 8-bit binary value and join them together.
        e.g. message text is 'pi'.
        ASCII decimal values of p and i are 112 and 105, respectively.
        8-bit Binary values of 112 and 105 are 01110000 and 01101001, respcetively.
        resultant binary value of string 'pi' is 0111000001101001.
    3.  Break the resultant binary value into groups of 6-bits 
        since we need to convert it to base64 (2^6).
        If the total resultant binary value bits are not in multiples of 6, we can append 0 at the end.
        For above example, the resultant binary bits are 16.
        So, we are short of 2 bits to form a 6-bit group at the end. 
        We will append 2 zeros in the last group.
        So, we will have 3 6-bit groups i.e. 011100, 000110 and 100100.
    4.  Once, we groups of 6-bit values. We will convert those into their respective decimal values.
        011100: its decimal value is 28.
        000110: its decimal value is 6.
        100100: its decimal value is 36.
    5.  Now, using base64 encoding table, fetch respective base64 character for above decimal values.
        28: c
        6: G
        36: k
    6.  Final base64 string would be b'cGk='.
        If you notice additional '=' character at the end, 
        it is due to the fact that base64 strings are represented in the multiples of 4 characters.
        Since our input string ended up having only 3 characters, 
        base64 appended one '=' character at the end.
        If the input string had been 'P', the output would have been 'UA==', 
        since 'P' is equivalent to only 2 base64 characters, 
        it added two '=' at the end to make it 4-character long.
    '''
    # message = "Python is fun"
    message_bytes = message.encode('ascii') # b'Python is fun'
    base64_bytes = base64.b64encode(message_bytes) # b'UHl0aG9uIGlzIGZ1bg=='
    base64_message = base64_bytes.decode('ascii') # 'UHl0aG9uIGlzIGZ1bg=='
    return base64_message

def from_base64_string(base64_message: str) -> str:
    '''
    It is the reverse process of converting normal text to base 64 
    as specified above in to_base64_string() function.
    '''
    # base64_message = 'UHl0aG9uIGlzIGZ1bg=='
    base64_bytes = base64_message.encode('ascii') # b'UHl0aG9uIGlzIGZ1bg=='
    message_bytes = base64.b64decode(base64_bytes) # b'Python is fun'
    message = message_bytes.decode('ascii') # 'Python is fun'
    return message

def simplified_to_base64_string(message):
    return base64.b64encode(message.encode('utf-8')).decode('utf-8')

def simplified_from_base64_string(base64_message):
    return base64.b64decode(base64_message.encode('utf-8')).decode('utf-8')

def main():    
    message = "Python is fun"
    base64_message = to_base64_string(message=message)
    print(base64_message) # 'UHl0aG9uIGlzIGZ1bg=='

    message = from_base64_string(base64_message=base64_message) # 'Python is fun'
    print(message) # 'Python is fun'

    print(f"{simplified_to_base64_string('pi')}")
    print(f"{simplified_from_base64_string(simplified_to_base64_string('pi'))}")

if __name__ == "__main__":
    main()
