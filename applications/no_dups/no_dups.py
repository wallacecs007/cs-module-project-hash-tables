def no_dups(s):
    # Your code here
    dict = {}
    array = s.split(' ')

    newArray = []

    for word in array:
        if not word in dict.keys():
            dict[word] = word
            newArray.append(word)

    return(" ".join(newArray))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
