#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml.dom import minidom


# 创建xml文件
def create_xml(path):
    doc = minidom.Document()
    root = doc.createElement('tilemap')
    root.setAttribute('tilemapservice','http://tms.osgeo.org/1.0.0" version="1.0.0')
    doc.appendChild(root)
    title = doc.createElement('title')
    root.appendChild(title)
    abstract = doc.createElement('abstract')
    root.appendChild(abstract)
    srs = doc.createElement('srs')
    root.appendChild(srs)
    srs_text =doc.createTextNode('EPSG:4326')
    srs.appendChild(srs_text)
    vsrs = doc.createElement('vsrs')
    root.appendChild(vsrs)
    tilesets = doc.createElement('tilesets')
    root.appendChild(tilesets)
    tilesets.setAttribute('profile','global-geodetic')
    t1 = doc.createTextNode('tileset href="" order="0" units-per-pixel="10.588')
    t2 =doc.createTextNode('tileset href="" order="1" units-per-pixel="5.294')
    t3 =doc.createTextNode('tileset href="" order="2" units-per-pixel="2.647')
    t4 =doc.createTextNode('tileset href="" order="3" units-per-pixel="1.323')
    t5 =doc.createTextNode('tileset href="" order="4" units-per-pixel="0.661')
    t6 =doc.createTextNode('tileset href="" order="5" units-per-pixel="0.331')
    tilesets.appendChild(t1)
    tilesets.appendChild(t2)
    tilesets.appendChild(t3)
    tilesets.appendChild(t4)
    tilesets.appendChild(t5)
    tilesets.appendChild(t6)
    f = open(path,'w')
    doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')
    f.close()
	

# 解析xml文件
def parse_xml(path):
    dom = minidom.parse(path)
    root = dom.documentElement
    tilemap1 = root.getElementsByTagName('tilemap')
    a=tilemap1[0]
    b=a.getAttribute('tilemapservice')
    print(b)
    c=dom.getElementsByTagName('title')
    cc=c[0]
    print(cc.firstChild.data)
	

if __name__ == '__main__':
    create_xml("../created.xml")
    parse_xml("../created.xml")
