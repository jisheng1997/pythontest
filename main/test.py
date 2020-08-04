for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ') # 注意'end' 的使用
    print(repr(x * x * x).rjust(4))

# if __name__ == '__main__':
#     print('你要看就给你看好了')
# print('看什么看，不准看')

print('------------------------------')