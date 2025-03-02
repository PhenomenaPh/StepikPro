def corporate_main():
    mails = [input() for _ in range(int(input()))]

    for _ in range(int(input())):
        mail = input()

        emp_mail = f"{mail}@beegeek.bzz"

        i = 1
        while emp_mail in mails:
            emp_mail = f"{mail}{i}@beegeek.bzz"
            i += 1

        mails.append(emp_mail)
        print(emp_mail)


corporate_main()
