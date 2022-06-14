import sys
from kb import KB

kb1 = KB()
with open(sys.argv[1], encoding='utf-8') as file:
    code = file.read().replace(r'\n', '')

kb1.load(code)
kb1.forwardChaining()

#【mynote】python kbReason.py animal_ostrich.kb 會推出鴕鳥但python kbReason.py animal.kb不會，因為加了3個事實:會飛.生蛋.長腿. 