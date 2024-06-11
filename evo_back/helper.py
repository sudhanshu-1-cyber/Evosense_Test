import re

def extract_yt_term(command):
    # Define a regular expression pattern to capture request for youtube
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    #Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    #if match is found , return the extracted request; otherwise, return none
    return match.group(1) if match else None

def extr_yt_term(command):
    # Define a regular expression pattern to capture request for youtube
    pattern = r'play\s+(.*?)\s+from\s+youtube'
    #Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    #if match is found , return the extracted request; otherwise, return none
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    #Split the input string into words
    words = input_string.split()
    #Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    #Join the remaining words back into the string
    result_string = ' '.join(filtered_words)
    
    return result_string