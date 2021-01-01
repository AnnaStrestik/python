# file = open ('data.txt', encoding= 'utf-8')
# content = file.read()
# file.close()
# data = content.strip().split(':')
# result = sum(int(c) for c in data)
# print (result)

pocet = 3

# varianta A
# print('Celkovy pocet zayanamu: ' + pocet)
# TypeError: must be str, not int
# 4A

# varianta B
seznam = [1, 2, 3, 4]
# print (seznam[len(seznam)])
# IndexError: list index out of range
# 2B

# varianta C
# if pocet > 0:
# print ('Kladny pocet zaznamu')
# IndentationError: expected an indented block
# 1C

# varianta D
# [c for c in seznam if c => 2]
# SyntaxError: invalid syntax
# 3D

# varianta E
print (pocet / (len(seznam) - 4))
