from sys import exit

helpInfo = '''
Usage: fuckCpp.exe file [options]...
Options:
    -h              Display This Help Info
    -l <level>      Set confusion level to <level>, default value is 'low'
    -o <file>       Place the output into <file>, default value is 'confused.cpp'
    --zip -z        Zip the output source file
'''

cppExtensionNames = [
    '.cp', '.cpp', '.h', '.hpp', '.c'
]

keywords = [
    'scanf', 'printf', 'cin', 'cout',
    'putchar', 'puts', 'getchar', 'rand',
    'long long', 'int', 'const', 'char', 
    'true', 'false', 'inline', 'struct',
    'bool', '__gcd', 'memset', 'NULL',
    'private', 'public', 'void', 'while',
    'for', 'auto', 'size_t', 'if', 'return', 
    'else'
]

# 'src' will be given when handling argv
defaultParamData = {
    'level': 'low',
    'output': 'confused.cpp',
    'zipsrc': True
}

paramType = {
    '-h': 'function',
    '-l': 'data',
    '-o': 'data',
    '--zip': 'boolean',
    '-z': 'boolean'
}

paramName = {
    '-h': 'help',
    '-l': 'level',
    '-o': 'output',
    '--zip': 'zipsrc',
    '-z': 'zipsrc'
}

functionMap = {
    'help': (lambda: (print(helpInfo), exit(0)))
}

DEBUG    = True

LOG_FILE = 'runlog_{time:YYYYMMDD}.log' 
