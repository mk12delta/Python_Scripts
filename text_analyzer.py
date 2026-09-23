#CSCI2850 - Text File Analysis

NETID = "acarmine"

def read_words(filename):
    words = []
    with open(filename, "r") as infile:
        for line in infile:
            words.extend(line.split())
    return words

def count_frequencies(words):
    freq = {}
    for word in words:
        key = word.lower()
        freq[key] = freq.get(key, 0) + 1
    return freq

def find_long_short(words):
    longest = words[0]
    shortest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word
    return longest, shortest

def average_len(words):
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

def most_common_start(words):
    letters = {}
    for word in words:
        first = word.lower()[0]
        if first.isalpha():
            letters[first] = letters.get(first, 0) + 1
    best = ""
    for letter in letters:
        if best == "" or letters[letter] > letters[best]:
            best = letter
    return best

def main():
    words = read_words("data.txt")
    freq = count_frequencies(words)
    longest, shortest = find_long_short(words)

    with open(NETID + ".txt", "w") as outfile:
        outfile.write("Longest Word: " + longest +"\n")
        outfile.write("Shortest Word: " + shortest +"\n")
        outfile.write("Average Word Length: " + str(average_len(words)) + "\n")
        outfile.write("Most Common Starting Letter: " + most_common_start(words)+"\n")
        outfile.write("Word Frequencies:\n")
        for word in sorted(freq):
            outfile.write(word + ": " + str(freq[word]) + "\n")

if __name__ == "__main__":
    main()
