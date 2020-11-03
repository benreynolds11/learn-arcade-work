import re


def main():
    # This function takes in a line of text and returns
    # a list of words in the line.
    def split_line():
        return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

    my_file = open("dictionary.txt")

    dictionary_list = []
    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)
    my_file.close()

    print("---Linear Search---")
    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        line_number += 1
        word_list = split_line()
        for word in word_list:
            i = 0
            while i < len(dictionary_list) and dictionary_list[i] != word.upper():
                i += 1
                if i == len(dictionary_list):
                    print("Line", str(line_number), "Word:", word)
    story.close()

    print("--- Binary Search ---")
    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        line_number += 1
        word_list = split_line()
        for word in word_list:
            upper_bound = len(dictionary_list) - 1
            lower_bound = 0
            found = False
            while lower_bound <= upper_bound and not found:
                middle = (lower_bound + upper_bound) // 2
                if dictionary_list[middle] < word.upper():
                    lower_bound = middle + 1
                elif dictionary_list[middle] > word.upper():
                    upper_bound = middle - 1
                else:
                    found = True
            if not found:
                print("Line", str(line_number), "Word:", word)
    story.close()


main()