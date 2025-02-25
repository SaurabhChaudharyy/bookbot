def count_characters(book):
    with open(book) as f:
        file_contents = f.read().lower()  # Convert to lowercase
        char_count = {}
        
        for char in file_contents:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        return char_count
    

def main():
    book = "./books/frankenstein.txt"
    character_counts = count_characters(book)
    print(character_counts)

main()