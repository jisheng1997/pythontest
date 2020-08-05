#!/usr/bin/python3

import functools
from numpy import mean


list1 = [1,2,3,4,5,6,7]
# def square(x):
#     return x**2

#求list1里数的平方并返回一个list
res1 = list(map(lambda x:x**2,list1))
# print(res1)

res2 = list(map(lambda x,y:x+y,[1,2,3],[4,5,6]))
# print(res2)

res3 = list(filter(lambda x:x % 3==0,list1))
# print(res3)

#求1-100的和
res4 = functools.reduce(lambda x,y:x+y,range(1,101))
#求5的阶乘
res5 = functools.reduce(lambda x,y:x*y,range(1,6))
# print(res4,res5)

# 第一步：格式化用户的英文名，要求首字母大小，其它字母小写
# 第二步：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个集合
# 第三步：过滤后，性别为男的用户
# 第四步：取每个元素的中的年龄[list]
# 第五步：求性别为男的用户的平均年龄

names = ['jeo','susan','herry','balck']
ages = [11,22,33,44]
sex = ['man','woman','man','man']

# 第一步：格式化用户的英文名，要求首字母大小，其它字母小写
step1 = list(map(lambda x:x.capitalize(),names))
# 第二步：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个集合
step2 = list(map(lambda x,y,z:[x,y,z],step1,ages,sex))
# 第三步：过滤后，性别为男的用户
step3 = list(filter(lambda x:x[2] == 'man',step2))
# 第四步：取每个元素的中的年龄[list]
# step4 = [i[1] for i in step3]
step4 = list(map(lambda x:x[1],step3))
# 第五步：求性别为男的用户的平均年龄
# step5 = mean(step4)
step5 = (functools.reduce(lambda x,y: x+y,step4))/len(step4)
# print(step5)

# 1.使用高阶函数求： 5！+4！+3！+2！+1！
# def fac(num):
#     result = 1
#     for n in range(1,num + 1):
#         result *= n
#     return result

res6 = list(map(lambda num:functools.reduce(lambda x,y:x*y,range(1,num+1)),[1,2,3,4,5]))
# print(sum(res6))

# 定义类
class person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("初始化成功")

    def sleep(self):
        print(self.name + '该睡觉了')

# lin = person('阿绫',24,'man')
# lin.sleep()

# 1.餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type(烹饪)。
# 创建一个名为 describe_restaurant()方法和一个名为open_restaurant ()方法,
# 其中前者打印前述两项信息，而后者打印一条消息,指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
# 2.三家餐馆：根据你为完成练习1而编写的类创建三个实例，
# 并对每个实例调用方法 describe_restaurant()。

class Restaurant:
    """
    class name：餐馆
    time：2020.08.03
    """
    count = 0
    number_served = 0
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        Restaurant.count += 1

    def describe_restaurant(self):
        print("餐馆的名字是：" + self.restaurant_name)
        print("烹饪类型是：" + self.cuisine_type)

    def open_restaurant (self):
        return "餐馆正在营业"

    def set_number_served(self,x):
        Restaurant.number_served = x

    def get_number_served(self):
        return '正在就餐的人数是：' + str(Restaurant.number_served)

    def increment_number_served(self,increment):
        Restaurant.number_served += increment

# restaurant1 = Restaurant("精品川菜馆","川菜")
# print(restaurant1.__doc__)
# print(restaurant1.restaurant_name,restaurant1.cuisine_type)
# restaurant1.describe_restaurant()
# print(restaurant1.open_restaurant())
# restaurant2 = Restaurant("老牌坊鲁菜名店","鲁菜")
# restaurant2.describe_restaurant()
# restaurant3 = Restaurant("粤味轩餐厅","粤菜")
# restaurant3.describe_restaurant()

# if __name__ == '__main__':
#     print('看什么看，不准看')

#如何查看实例化的次数？
# print(restaurant3.count)

# 3.就餐人数：在为完成练习1而编写的程序中,添加一个名为number_served的属性,
# 并将其默认值设置为0。打印有多少人在这家餐馆就餐过,然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法,它让你能够设置平日就餐人数。
# 调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法,它让你能够将就餐人数递增.
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

# restaurant1.set_number_served(30)
# restaurant1.increment_number_served(10)
# print(restaurant1.get_number_served())

# 1.用户：创建一个名为User的类，其中包含属性first_name和last_name,
# 还有用户简介通常会存储的其他几个属性。在类User中定义一个名为describe_user()的方法，
# 它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法.
# 2.尝试登录次数：在为完成练习3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法,它将属性 login_attempts的值加 1。
# 再编写一个名为reset_login_attempts()方法,它将属性login_attempts的值重置为0。
# 根据User类创建一个实例,再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值,确认它被正确地递增；
# 然后，调用方法reset_login_attempts()
# 并再次打印属性login_attempts的值，确认它被重置为0。
#如何对于每个实例对象有不同的数值？

class User():
    #这是一个类变量
    login_attempts = 0
    # 对象被实例化后会先找实例变量，没有实例变量，才会找类变量。
    def __init__(self,last_name,first_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.last_name + self.first_name
        # 这是一个实例变量
        self.login_attempts = 0

    def describe_user(self):
        return "用户的名字是：" + self.last_name + self.first_name

    def greet_user(self):
        return "亲爱的" + self.last_name + self.first_name + "，您好"

    def increment_login_attempts(self):
        # 如果不创建实例变量，这条语句将会自动创建，
        # 但在没有实例变量之前，会指向类变量
        # print(self.login_attempts) 这里输出类变量的值
        self.login_attempts += 1
        # print(self.login_attempts) 这里输出实例变量的值
        User.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

#实例化对象张三
user1 = User('张','三')
print(user1.describe_user())
print(user1.greet_user())
#进行五次用户请求
for i in range(1,6):
    user1.increment_login_attempts()
#实例化对象李四
user2 = User('李','四')
#进行两次用户请求
for i in range(1,3):
    user2.increment_login_attempts()
#查询不同实例化对象的用户请求次数，实例变量对于不同实例的值不同，类变量被全部实例共享
print(user1.name + '用户请求的次数为：' + str(user1.login_attempts))#
print(user2.name + '用户请求的次数为：' + str(user2.login_attempts))
print('总请求次数（类变量）：' + str(User.login_attempts))
#调用reset函数将用户请求次数归零
user1.reset_login_attempts()
print(user1.name + '用户请求的次数为：' + str(user1.login_attempts))












