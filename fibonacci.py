def fibbonacci_number(number, memory):
    if number in memory:
        return memory[number]
    if number <= 2:
        return 1
    memory[number] = fibbonacci_number(
        number - 1, memory) + fibbonacci_number(number - 2, memory)
    return fibbonacci_number(number-1, memory) + fibbonacci_number(number-2, memory)


try:
    n = int(input('> '))
    if n <= 0:
        raise ValueError
    memory = {}
    print(fibbonacci_number(n, memory))
except ValueError:
    print('Value must be number bigger than 0')
