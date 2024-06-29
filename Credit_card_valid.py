#
# def creditCard(c):
#     if c[0] not in ['4', '5', '6']:
#         valid = False
#
#     a = c.split(sep=4)
#
#     if len(a) == 1:
#         for i in a:
#             if len(i) != 16:
#                 valid = False
#
#     if len(a) == 4:
#         for i in a:
#             if len(i) != 4:
#                 valid= False
#
#     if len(a) != 1 and len(a) != 4:
#         valid=False
#     s = c.replace("-", "")
#
#
#     for i in range(len(s)-3):
#        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3]:
#            valid= False

def creditCard(n):
    c = 0
    list = []
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '-']
    b = [4, 5, 6]
    print(len(n))
    for i in n:
        if (len(i) != 16):
            print("Invalid")
    for i in len(n):
            if (n[i] == n[i + 1]):
                c += 1
            else:
                list.append(c)
                c = 1
            if (n[i] not in a):
                print("Invalid")
            if (n[0] not in b):
                print("Invalid")

    for i in range(len(n) - 3):
        if n[i] == n[i + 1] and n[i] == n[i + 2] and n[i] == n[i + 3]:
            print("Invalid")

c =['4123456789123456','5123-4567-8912-3456','1234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
creditCard(c)