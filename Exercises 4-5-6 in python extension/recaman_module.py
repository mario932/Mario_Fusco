def generate_recaman_sequence(n):
    mylist = [0]
    a0 = 0

    for i in range(1, n):
        if ((a0 - i > 0) and not (a0 - i in mylist)):
            mylist.append(a0 := a0 - i)
        else:
            mylist.append(a0 := a0 + i)
    return mylist

def main():
    n = int(input('Insert the number of elements in the sequence: '))
    result = generate_recaman_sequence(n)
    print(result)

if __name__ == "__main__":
    main()