#------------------------------------------------------------------------------------------
#                                   Генераторы
#------------------------------------------------------------------------------------------ 
# Что такое генератор? Как написать на Python генератор? Преимущества относительно функции?
#------------------------------------------------------------------------------------------ 

#Генераторы в Python — это особый вид функций, которые позволяют работать с последовательностями
# анных итерируемым образом. Генераторы замедляют выполнение и возвращают значения по одному, 
#что позволяет экономить память и ускорять работу с большими наборами данных.
#------------------------------------------------------------------------------------------ 
#                                   Как работают генераторы
#------------------------------------------------------------------------------------------ 
#Генераторы создаются с помощью функции, в теле которой используется оператор yield вместо return. 
# Когда функция с yield вызывается, она не выполняется полностью, а возвращает итератор. Каждый вызов 
# метода next() на этом итераторе продолжает выполнение функции до следующего yield. 
#------------------------------------------------------------------------------------------ 
#                                   Пример генератора:
#------------------------------------------------------------------------------------------ 
def counter(n):
    i = 0
    while i < n:
        yield i
        i += 1

# При вызове counter(5) функция не выполняется сразу. Вместо этого создаётся генератор, который будет 
# возвращать значения от 0 до 4 при каждом обращении через next().
#------------------------------------------------------------------------------------------ 
#                                   Отличия от обычных функций
#------------------------------------------------------------------------------------------ 
# Состояние функции: Обычные функции при вызове сохраняют и возвращают состояние только один раз. Генераторы сохраняют 
# своё состояние между вызовами. 
# Память: Обычные функции возвращают все значения сразу и хранят их в памяти. 
# Генераторы производят значения по одному, что значительно уменьшает потребление памяти для больших последовательностей.
# Ожидание значений: Генераторы позволяют обрабатывать значения "на лету", тогда как обычные функции возвращают сразу 
# всю последовательность.
#------------------------------------------------------------------------------------------ 
#                                   Плюсы генераторов
#------------------------------------------------------------------------------------------ 
# Эффективность по памяти: Генераторы производят элементы по одному и не хранят все элементы в памяти, 
# что позволяет работать с большими наборами данных.
# Легкость в использовании: Генераторы позволяют легко и быстро писать код для работы с итерациями и последовательностями.
# Простой синтаксис: Использование yield делает код чище и понятнее по сравнению с обработкой данных с помощью других структур.
#------------------------------------------------------------------------------------------ 
#                                   Минусы генераторов
#------------------------------------------------------------------------------------------ 
# Ограниченность: Генераторы могут производить значения только один раз. Если вам нужно итерировать данные 
# повторно, необходимо будет создать новый генератор.
# Сложность отладки: Поскольку генераторы поддерживают своё состояние, это может усложнить 
# отладку кода, особенно в сложных случаях.
# Не все функции совместимы: Генераторы не могут использоваться в некоторых контекстах, 
# где ожидаются обычные функции, поскольку они не возвращают все значения сразу.
##------------------------------------------------------------------------------------------ 
#                                   Пример использования
#------------------------------------------------------------------------------------------ 
#Вот простой пример генератора, который генерирует последовательность Фибоначчи:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

#В этом примере мы создаем генератор, который генерирует первые n чисел Фибоначчи. 
# Каждый раз, когда он вызывается, он возвращает следующее число последовательности.
#Генераторы — это мощный инструмент в Python, который позволяет эффективно 
# обрабатывать данные и работать с итерациями. Они могут быть особенно полезны при работе с 
# большими объемами информации или в ситуациях, где важно экономить память.

#------------------------------------------------------------------------------------------ 
#                                   Что такое generator comprehension?
#------------------------------------------------------------------------------------------ 

a = (i for i in range(5))
for i in a:
    print(i)
print(next(a))

#------------------------------------------------------------------------------------------ 
#                                   Генератор с несколькими yield
#------------------------------------------------------------------------------------------ 

def some():
    yield 1
    yield 2
    yield 3

s = some()
print(next(s)) # 1 
print(next(s)) # 2
print(next(s)) # 3

#------------------------------------------------------------------------------------------ 
#                                   yield from
#------------------------------------------------------------------------------------------ 
# если нам нужно из первого генератора вернуть все значения во второй генератор.
def first():
    yield 1
    yield 1
def second():
    yield from first()
    yield 2
    yield 2
obj = second()
for i in obj:
    print(i)        