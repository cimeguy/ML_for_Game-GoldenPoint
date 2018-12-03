#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom import minidom

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# 题目九：XML文件的生成和解析
def create_xml(path):
    dom = minidom.Document()  # 创建dom树对象
    root = dom.createElement('tilemap')  # 创建根节点
    root.setAttribute('tilemapservice', 'http://tms.osgeo.org/1.0.0 ')
    root.setAttribute('version', '1.0.0')
    # 设置该节点的属性
    dom.appendChild(root)  # 用dom对象添加根节点

    title = dom.createElement('title')  # 创建元素子节点
    root.appendChild(title)  # 用父节点对象添加元素子节点
    title_text = dom.createTextNode('default')  # 用dom创建文本节点，把文本节点（文字内容）看成子节点
    title.appendChild(title_text)  # 用添加了文本的节点对象（看成文本节点的父节点）添加文本节点

    abstract = dom.createElement('abstract')
    root.appendChild(abstract)

    srs = dom.createElement('srs')
    root.appendChild(srs)
    srs_text = dom.createTextNode('EPSG:4326')
    srs.appendChild(srs_text)

    vsrs = dom.createElement('vsrs')
    root.appendChild(vsrs)

    boundingbox = dom.createElement('boundingbox')
    root.appendChild(boundingbox)
    boundingbox.setAttribute('maxx', '180.0')
    boundingbox.setAttribute('maxy', '90.0')
    boundingbox.setAttribute('minx', '-180.0')
    boundingbox.setAttribute('miny', '-90.0')

    origin = dom.createElement('origin')
    root.appendChild(origin)
    origin.setAttribute('x', '-180.0')
    origin.setAttribute('y', '-90.0')

    tileformat = dom.createElement('tileformat')
    root.appendChild(tileformat)
    tileformat.setAttribute('extension', 'tif')
    tileformat.setAttribute('height', '17')
    tileformat.setAttribute('mime-type', 'image/tiff')
    tileformat.setAttribute('width', '17')

    tilesets = dom.createElement('tilesets')
    root.appendChild(tilesets)
    tilesets.setAttribute('profile', 'global-geodetic')

    tileset = dom.createElement('tileset')
    tilesets.appendChild(tileset)
    tileset.setAttribute('href', '')
    tileset.setAttribute('order', '0')
    tileset.setAttribute('units-per-pixel', '10.588')

    tileset = dom.createElement('tileset')
    tilesets.appendChild(tileset)
    tileset.setAttribute('href', '')
    tileset.setAttribute('order', '1')
    tileset.setAttribute('units-per-pixel', '5.294')

    tileset = dom.createElement('tileset')
    tilesets.appendChild(tileset)
    tileset.setAttribute('href', '')
    tileset.setAttribute('order', '2')
    tileset.setAttribute('units-per-pixel', '2.647')

    tileset = dom.createElement('tileset')
    tilesets.appendChild(tileset)
    tileset.setAttribute('href', '')
    tileset.setAttribute('order', '3')
    tileset.setAttribute('units-per-pixel', '1.323')

    tileset = dom.createElement('tileset')
    tilesets.appendChild(tileset)
    tileset.setAttribute('href', '')
    tileset.setAttribute('order', '4')
    tileset.setAttribute('units-per-pixel', '0.661')

    tileset = dom.createElement('tileset')
    tilesets.appendChild(tileset)
    tileset.setAttribute('href', '')
    tileset.setAttribute('order', '5')
    tileset.setAttribute('units-per-pixel', '0.331')

    with open(path, 'w', encoding='UTF-8') as fh:
        dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')



def parse_xml(path):
    tree = et.parse(path)  # 解析xml文件，返回ElementTree对象
    root = tree.getroot()  # 获取根节点
    a = str(root.attrib['tilemapservice'])  # 打印根节点的某一属性值
    b = root[0].text  # 获取title节点的值
    c = len(root[7])  # 获取tilesets节点的长度
    d = [root[7][0].attrib['order'], root[7][1].attrib['order'], root[7][2].attrib['order'],
         root[7][3].attrib['order'], root[7][4].attrib['order'], root[7][5].attrib['order']]
    e = d.index(max(d))  # 获取tileset节点中最大的order值
    f = [a, b, c, e]

    return f


if __name__ == "__main__":
    create_xml("..\created.xml")
    print(parse_xml("..\created.xml"))