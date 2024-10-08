def missing_characters(s):
    # Define the complete set of digits and lowercase English letters
    all_digits = set('0123456789')
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    
    # Extract the digits and letters from the input string
    input_digits = set(filter(str.isdigit, s))
    input_letters = set(filter(str.isalpha, s.lower()))
    
    # Find the missing digits and letters by subtracting the input sets from the full sets
    missing_digits = sorted(all_digits - input_digits)
    missing_letters = sorted(all_letters - input_letters)
    
    # Combine the missing digits and letters into a single string
    result = ''.join(missing_digits) + ''.join(missing_letters)
    
    # Return the result as a string
    return result

# Input processing from stdin
if __name__ == "__main__":
    s = input().strip()  # Read the input string from stdin
    result = missing_characters(s)
    print(result)  # Print the result for the user to see

