#!/usr/bin/env python
# -*- coding: utf-8-*-

from lxml.html import fromstring, tostring
from lxml import etree


with open('./rebuild.sh') as f:
    lines = f.readlines()[2:]

t = [x.strip('# \n') for x in lines[-12::2]]
dic = [(x.split('|')[0].decode('utf-8'), x.split('|')[1]) for x in t]
dic = dic[::-1]

with open('./html/index.html') as f:
    root = fromstring(f.read())

ul = root.xpath('//ul[@id="toc"]')[0]
lis = ul.xpath('./li')

# 移除li
for li in lis:
    li.getparent().remove(li)
# 生成新的li
for name, date in dic:
    li = etree.Element('li')
    a = etree.Element('a', href='./' + name + '.html')
    a.text = name
    span = etree.Element('span')
    span.set("class", 'time')
    span.text = date
    a.append(span)
    li.append(a)
    ul.append(li)

with open('./html/index.html', 'wb') as f:
    f.write(tostring(root, encoding='unicode').encode('utf-8'))
