import re

def find_mirror_words(text):
    pattern = re.compile(r'[@#]([A-Za-z]{3,})[^A-Za-z]+([A-Za-z]{3,})[@#]')
    matches = pattern.findall(text)

    valid_pairs = []
    mirrored_pairs = []

    for match in matches:
        word_one, word_two = match
        if word_one == word_two[::-1]:
            mirrored_pairs.add(match)
        elif word_one.lower() == word_two[::-1].lower():
            valid_pairs.append(match)

    return valid_pairs, mirrored_pairs

def main():
    text = input().strip()

    valid_pairs, mirrored_pairs = find_mirror_words(text)

    if not valid_pairs:
        print("No word pairs found!")
    else:
        print(f"{len(valid_pairs)} word pairs found!")

    if not mirrored_pairs:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        print(' <=> '.join(' <=> '.join(pair) for pair in sorted(mirrored_pairs, key=lambda x: x[0])))

if __name__ == "__main__":
    main()
