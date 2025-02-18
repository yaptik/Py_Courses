# # Home Work 5.1.
# def is_year_leap(year):
#     '''Determinate, are year is leap?'''
#
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, '--> ', end='')
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print('ok!')
#     else:
#         print('Fail')

# # Home Work 5.4
# def Fibonacci(number):
#     if number <= 0:
#         return None
#     if number == 1:
#         return 1
#
#     Fibo1 = Fibo2 = 1
#     for i in range(2, number):
#         Fibo1, Fibo2 = Fibo2, Fibo1 + Fibo2
# 
#     return Fibo2
#
# for i in range(-1, 25):
#     print(Fibonacci(i))
#
