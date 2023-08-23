def palindrome(n):
    num1 = str(n)

    num_range = len(num1)

    x = num_range - 1

    reverse_num = ""

    while x < num_range:
        if x == -1:
            break

        reverse_num = reverse_num + num1[x]
        x = x - 1

    if num1 == reverse_num:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")

no1 = 121
no2 = 125

print("original number ", no1)
palindrome(no1)

print("original number ", no2)
palindrome(no2)
