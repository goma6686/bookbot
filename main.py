def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        list_of_dict = sort_dict_by_value(char_count)
        converted_dict = convert(list_of_dict)

        print_report(word_count, converted_dict)

def print_report(words, dict_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print("\n")

    for dict in dict_list:
        for key, value in dict.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

#converts dict to list of dicts
def convert(dictionary):
    return [{key: value} for key, value in dictionary.items()]

#returns word count
def count_words(full_text):
    words = full_text.split()
    return len(words)

#returns the number of times each character appears in the string
def count_characters(full_text):
    full_text = full_text.lower()
    char_count = {"a" : 0}

    for character in full_text:
        #checks if character is from alphabet
        if character.isalpha():
            if character in char_count.keys():
                char_count[character] += 1
            else:
                char_count[character] = 1

    return char_count

main()