import re
#print(re.match('www','www.cherylgood.cn'))
#print(re.match('www','wWW.cherylgood.cn'))
#print(re.match('www','wWW,cherylgood.cn', re.RegexFlag.IGNORECASE))
#print(re.match('www1','www.cherylgood.cn'))
#print(re.match('cn','www.cherylgood.cn'))

#use search
print(re.search('www','www.cherylgood.cn',re.IGNORECASE))
print(re.search('cherylgood','wWW.cherylgood.cn',re.IGNORECASE))
print(re.search('cn','www.cherylgood.cn',re.IGNORECASE))


line = "Hello, I am 安杰小生，我的博客是www.cherylgood.cn"

#还有一点要注意，我们编写正则表达式是，字符串前用了 r，
#这样是表示正则表达式字符串是原始类型的字符串，
#原始字符串时python解析器不会对内部的特殊字符进行转译，减少不必要的麻烦

m = re.match(r'.* am (.*)，我的博客是(.*)', line, re.IGNORECASE)
if m is not None:
    print(m.group())
    print(m.groups())
    # take first () data
    print(m.group(1))
    # take the second data
    print(m.group(2))
else:
    print(' 什么都找不到~~')
