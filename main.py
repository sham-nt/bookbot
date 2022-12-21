# Global variables:
book_path = "books/frankenstein.txt"


# functions:
def get_book_txt(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
    
def count_words(str):
    words = str.split()
    return len(words)
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
    
def char_report(text):
    dict = get_chars_dict(text)
    char_list = list(dict)
    alpha_list = []
    for char in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {dict[char]} times")
    
    
     

# main function 
def main():
    book_text = get_book_txt(book_path)
    number_of_words = count_words(book_text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} found in the document")
    char_report(book_text)
    print("--- End report ---")

        
if __name__ == "__main__":
    main()