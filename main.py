from utils.compress import *
from utils.confuse import *
from utils.logger import *

# defaultParamData = {
#     'level': 'low',
#     'output': 'confused.cpp',
#     'zipsrc': True
# }

@logger.catch
def execute(conf) -> None: 
    # Firstly: Mess Codes
    pData           = conf.ParamData
    sourceCode      = open(pData['src'], 'r', encoding='u8')
    sourcelines     = sourceCode.readlines()
    Confuser        = confuser(pData['level'])
    confusedCode    = Confuser.genConfused(sourcelines)
    if pData['zipsrc']:
        pass
    outPutFile      = open(pData['output'], 'w', encoding='u8')
    outPutFile.write(confusedCode)
    outPutFile.close()
    return   