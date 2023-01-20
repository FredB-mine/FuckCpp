from sys import exit

__version__ = '1.3.0'

endl = '\n'

helpInfo = '''
Usage: fuckCpp file [options]...
Options:
    -h              Display This Help Info
    -l <level>      Set confusion level to <level>, default value is 'low'
    -o <file>       Place the output into <file>, default value is 'confused.cpp'
    --zip -z        Zip the output source file
    --no-confuse    Ask FuckCpp not to confuse your source
'''

cppExtensionNames = [
    '.cp', '.cpp', '.h', '.hpp', '.c'
]

confuseKeywords = [
    'scanf', 'printf', 'cin', 'cout',
    'putchar', 'puts', 'getchar', 'rand',
    'long long', 'int', 'const', 'char',
    'true', 'false', 'inline', 'struct',
    'bool', '__gcd', 'memset', 'NULL',
    'private', 'public', 'void', 'while',
    'for', 'auto', 'size_t', 'if', 'return',
    'else'
]

spaceTypes = [
    ' ', '\t', '\n', '\r', '\v', '\f'
]

# 'src' will be given when handling argv
defaultParamData = {
    'level': 'low',
    'output': 'confused.cpp',
    'zipsrc': False,
    'noConfuse': False
}

paramType = {
    '-h': 'function',
    '-l': 'data',
    '-o': 'data',
    '--zip': 'boolean',
    '-z': 'boolean',
    '--no-confuse': 'boolean'
}

paramName = {
    '-h': 'help',
    '-l': 'level',
    '-o': 'output',
    '--zip': 'zipsrc',
    '-z': 'zipsrc',
    '--no-confuse': 'noConfuse'
}

functionMap = {
    'help': (lambda: (print(helpInfo), exit(0)))
}

trigraphs = {
    '=': '#',
    '/': '\\',
    '\'': '^',
    '(': '[',
    ')': ']',
    '<': '{',
    '>': '}',
    '!': '|',
    '-': '~'
}

NodeRunTime = {
    'win32': 'node.exe',
    'linux': 'bin/node',
    'darwin': 'bin/node'
}

DEBUG    = True

LOG_FILE = 'runlog_{time:YYYYMMDD}.log' 
