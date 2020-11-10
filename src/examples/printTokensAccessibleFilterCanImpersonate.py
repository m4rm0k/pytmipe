# -*- coding: UTF-8 -*-
# By Quentin HARDY (quentin.hardy@protonmail.com) - bobsecq

import sys
sys.path.append('../')
from impersonate import Impersonate
from utils import *

configureLogging()
imp = Impersonate()
print("Print limited information about all tokens which can be impersonated:")
imp.printTokensAccessibleFilter(targetPID=None,
                                filter={'canimpersonate':True,},
                                printFull=False,
                                printLinked=False,
                                _useThreadMethod=False)