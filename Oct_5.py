#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@File    : Oct_5.py
@Time    : 2020/8/5 10:38
@Author  : jisheng
"""

#继承
class animal():
    def eat(self):
        print("我饿了，想吃人")

class cat():
    def eat(self):
        print("我只是只猫，我爱吃猫粮")

# cat1 = cat()
# cat1.eat()

#多继承
class bosimao(animal,cat):
    pass

# 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，
# 而在子类使用时未指定，python从左至右搜索
# 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
# bosimao1 = bosimao()
# bosimao1.eat()

# 管理员：管理员是一种特殊的用户。编写一个名为Admin的类，
# 让它继承你为完成练习3或练习5而编写的User类。
# 添加一个名为privileges的属性，用于存储一个由字符串
# （如“can add post”、“can delete post”、“can ban user”等）
# 组成的列表。编写一个名为show_privileges()的方法,
# 它显示管理员的权限，创建一个Admin实例，并调用这个方法。

#父类User
class User():
    def __init__(self,last_name,first_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = self.last_name + self.first_name
        self.login_attempts = 0
        self.greet_user()

    def describe_user(self):
        return "用户的名字是：" + self.last_name + self.first_name

    def greet_user(self):
        print("亲爱的" + self.last_name + self.first_name + "，您好")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        for x in Admin.privileges:
            print(self.name + x)

# admin1 = Admin("zhang",' san ')
# print(admin1.describe_user())
# admin1.show_privileges()

# 冰淇淋小店：冰其淋小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让它继承你为完成练习1或练习4而编写的Restaurant类
# 这两个版本Restaurant类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors的属性,用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一IceCreamStand实例,并调用这个方法。

#父类
class Restaurant:
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

class IceCreamStand(Restaurant):
    favours = ['','']
    def __init__(self,restaurant_name):
        self.restaurant_name = restaurant_name
        # super().__init__()

icecream1 = IceCreamStand('冰其淋小店')

#私有属性和方法
class person():
    __place = "earth"
    #__为私有属性，只有内部可以访问，外部不能访问
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    #私有属性可以通过函数调用来访问
    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    # 私有方法可以通过函数调用来访问
    def __eat(self):
        return self.__name + '想吃饭'

    def want(self):
        return self.__eat()

# zhangsan = person('张三',24)
# print('您好，' + zhangsan.get_name())
# print(zhangsan.want())

#使用面向对象的方式实现加减乘除四则运算。
class cal():
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.arithmetic()

    def arithmetic(self):
        if self.operator == "+":
            res = self.num1 + self.num2
            print('%d加%d等于%d'%(self.num1,self.num2,res))
        elif self.operator == "-":
            res = self.num1 - self.num2
            print('%d减%d等于%d' % (self.num1, self.num2, res))
        elif self.operator == "*":
            res = self.num1 * self.num2
            print('%d乘%d等于%d' % (self.num1, self.num2, res))
        elif self.operator == "/":
            res = self.num1 / self.num2
            print('%d除%d等于%d' % (self.num1, self.num2, res))

# cal1 = cal(4,2,'+')
# cal2 = cal(4,2,'-')
# cal3 = cal(4,2,'*')
# cal4 = cal(4,2,'/')

# 1、创建三个游戏人物，分别是：
# 属性:
#     名字：name,定位：category,血量：Output技能：Skill
# 英雄：
#     铠，战士，血量：1000 技能：极刃风暴
#     王昭君，法师 ，血量：1000 技能：凛冬将至
#     阿轲，刺客，血量：1000 技能：瞬华
# 2、游戏场景，分别：
# 偷红buff，释放技能偷到红buff消耗血量300
# solo战斗，一血，消耗血量500
# 补血，加血200

class heros():
    def __init__(self,name,category,skill,output = 1000):
        self.name = name
        self.category = category
        self.skill = skill
        self.output = output

    def get_info(self):
        return '英雄的名字是：%s，定位是：%s，技能是：%s，血量是：%d'\
            %(self.name,self.category,self.skill,self.output)

    def touhong(self):
        self.output -= 300
        if self.output > 0:
            return '%s释放了%s偷到了红buff，减少了300血，现在血量是：%d'\
                %(self.name,self.skill,self.output)
        else:
            return self.name + '已经死亡'

    def solo(self,enemy):
        self.output -= 500
        enemy.output = -1
        if self.output > 0:
            return '%s击败了%s，拿下了一血，减少了500血，现在血量是：%d' \
                   % (self.name, enemy.name, self.output)
        else:
            return self.name + '已经死亡'

    def cure(self):
        if self.output > 0:
            self.output += 200
            return self.name + '回了一口血，现在血量是：' + str(self.output)
        else:
            return '您已经死亡'

# kai = heros('铠','战士','极刃风暴')
# wangzhaojun = heros('王昭君','法师' ,'凛冬将至')
# print(kai.touhong())
# print(kai.solo(wangzhaojun))
# print(kai.cure())
# print(wangzhaojun.touhong())
# print(wangzhaojun.get_info())




