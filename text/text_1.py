

import re

p = re.compile('-')
c=p.sub('', '2022-03-01')

print(c)