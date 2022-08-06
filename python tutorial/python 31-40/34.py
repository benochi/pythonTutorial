#https://pypi.org/project/pip/

import camelcase

c = camelcase.CamelCase()

testStr = "i am all lowercase"

print(c.hump(testStr))