def main():
    path = ("books/frankenstein.txt")
    with open(path) as f:
        file_contents = f.read()
        print(f"--- Begin report of {path} ---")
        count_words(file_contents)
        print("")
        count_letters(file_contents)
        
def count_words(file_contents):
    words = file_contents.split()
    print(f"There are {len(words)} words found in the docmnet")

def count_letters(file_contents):
    wordCount = dict()
    for line in file_contents:
        line = line.lower()
        wds = line.split()
        for wd in wds:
            if wd.isalpha():
                if wd in wordCount:
                    wordCount[wd] = wordCount[wd] + 1
                else:
                    wordCount[wd] = 1
    
    sorted_wordCount = dict(sorted(wordCount.items(), key = lambda item: item[1], reverse = True))

    for key, value in sorted_wordCount.items():
        print(f"The '{key}' character was found {value} times")
        
main()        

