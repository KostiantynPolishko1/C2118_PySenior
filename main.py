# import inspect
#
# from lesson4 import Student
#
print('Lesson 6: Try-Except')
#
# print('is function:', inspect.isfunction(Student))
# print('is class: ', inspect.isclass(Student))
#
# #contruction try-except-else-finally
#
# try:
#     print('is method', inspect.ismethod(Student.age))
# except Exception as exception:
#     print(f'error: {exception.__str__()}')
# finally:
#     print('Checking is done')
#
# sigStudent = inspect.signature(Student)
#
# print(sigStudent.parameters)
# for item in sigStudent.parameters.items():
#     print(f'item - {item[1]}')



class ItemSoft:
    price: int
    mark: str

    def __init__(self, price: int, mark: str):
        if type(price) is not int:
            raise TypeError('argument price is not int')
        self.price = price
        self.mark = mark


try:
    keyboard = ItemSoft('1000a', 'logitech')
    print(f'name : {keyboard.mark}, price : {keyboard.price}/{type(keyboard.price)}')
except Exception as error:
    print(f'error msg: {error.__str__()}')
finally:
    print('init of instance is done')
