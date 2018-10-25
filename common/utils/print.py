from termcolor import colored, cprint


def warn(string, flag="[!]"):
    cprint(flag + string, 'yellow')


def error(string, flag="[-]"):
    cprint(flag + string, 'red')


def info(string, flag="[+]"):
    cprint(flag + string, 'green')


def result_print(string):
    print(string)


def start_mark(string, flag='*'):
    print(flag * 76)
    print(flag + ' ' * 31 + string + ' ' * 31 + flag)
    print(flag * 76)


def end_mark(flag='*'):
    print(flag * 76)
    print(flag + ' ' * 35 + 'END' + ' ' * 36 + flag)
    print(flag * 76)


if __name__ == '__main__':
    warn('warn')
    error('error')
    info('info')
