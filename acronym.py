
# Convert a phrase to its acronym.
# Techies love their TLA (Three Letter Acronyms)!
# Help generate some jargon by writing a program that converts a long name like Portable Network Graphics to its acronym (PNG)


# So create a function that takes in a phrase from a user and returns the phrase acronym
#Inputs: Welcome Back Home 
# expected output: WBH

# We first take in a phrase and split the pharse to seperate it into words
# For each word we will take the letter at index 0 and add it to acroynm string
# return acroynm

def acronym(phrase):
    acronym = ""
    for word in phrase.split():
        acronym = acronym + word[0].upper()
    return acronym


def main():
    phrase = input("Enter a phrase: ")
    print(acronym(phrase))


if __name__ == "__main__":
    main()