import hlprint
import hlvariables
from colorama import Back, Fore, Style

project = open("tests/ultratest"+'.hhll', 'r')
pyproject = open('popa.py', 'w')
lines = project.readlines()
symvols = 1
print(Fore.LIGHTMAGENTA_EX + 'start\n' + Fore.RESET)
if lines[len(lines)-1] != 'end':
    print(Fore.RED + 'ERROR!')
else:
    for line in lines:
        pyproject.writelines(f'{hlprint.pprint(line)}\n')
        pyproject.writelines(f'{hlprint.pnd(line)}\n')
        pyproject.writelines(f'{hlvariables.var(line)}\n')
    print(Fore.LIGHTMAGENTA_EX + 'file compilate to .py!')