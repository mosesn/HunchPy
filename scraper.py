import re

matcher = re.compile(r'self\.(\S+)')
fp = open('text.txt')


for line in fp.readlines():
    tmp = matcher.search(line)
    if tmp:
       x = tmp.group(1)
       print '    def get_' + x + '(self):'
       print '        return self.'+x
       print ''
