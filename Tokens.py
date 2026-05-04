# Marks = 62
# if Marks>=75:
#         print('A')
# elif Marks>=65:
#         print('B')
# elif Marks>=55:
#         print('C')
# else:
#         print('F')

# debit = 300.00
# credit = 450.00

# template = """
# ... Account Report
# ... Credit:  ${credit:.2f}
# ... Debit:  -${debit:.2f}
# ... ________________
# ... Balance: ${balance:.2f}"""

# print (
#             template.format(
#             credit=credit,
#             debit=debit,
#             balance=credit - debit,
#    )
# )


#------------- Exercise-1----------------#

# a=10+20*30
# b=42/30
# c=(94+2)*6-1

# print (a)
# print (b)
# print(c)


# #--------------Excercise-2--------------#

# ex=10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# print(ex)


# #--------------Excercise-3--------------#

# salary = 750 
# raise_percentage = 15 
# print(salary + (salary * raise_percentage / 100))

# #--------------Excercise-4--------------#
# a=4
# b=10
# c=5.0
# d=1
# f=5

# x=(a==c)
# y=(a<b)
# z=(f>=c)
# print(x)
# print(y)
# print(z)

# #--------------Excercise-5--------------#

# # Data
# rows = [
#     {"A": 1,  "B": 2, "C": True,  "D": False},
#     {"A": 10, "B": 3, "C": False, "D": False},
#     {"A": 5,  "B": 1, "C": True,  "D": True},
# ]

# # Evaluate and print results
# print(f"{'A':<5} {'B':<5} {'C':<8} {'D':<8} {'Result'}")
# print("-" * 35)

# for row in rows:
#     A, B, C, D = row["A"], row["B"], row["C"], row["D"]
#     result = A < B and C or D
#     print(f"{A:<5} {B:<5} {str(C):<8} {str(D):<8} {result}")


    #--------------Excercise-5--------------#

first_No = int(input("Enter a number: "))
second_No = int(input("Enter another number: "))

print("Result: ", first_No + second_No) 