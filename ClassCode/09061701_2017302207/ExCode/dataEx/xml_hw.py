#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from xml.dom import minidom

try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

# 题目九：XML文件的生成和解析
def create_xml(path):
    document = minidom.Document()
    tilemap = document.createElement('tilemap')
    document.appendChild(tilemap)
    tilemap.setAttribute('tilemapservice', "http://tms.osgeo.org/1.0.0 ")

    tile = document.createElement('tile')
    tilemap.appendChild(tile)
    abstract = document.createElement('abstract')
    tilemap.appendChild(abstract)
    srs = document.createElement('srs')
    tilemap.appendChild(srs)
    vsrs = document.createElement('vsrs')
    tilemap.appendChild(vsrs)
    boundingbox = document.createElement('boundingbox')
    boundingbox.setAttribute('maxx', "180.0")
    boundingbox.setAttribute('maxy', "90.0")
    boundingbox.setAttribute('minx', "-180.0")
    boundingbox.setAttribute('miny', "-90.0")
    tilemap.appendChild(boundingbox)
    origin = document.createElement('origin')
    origin.setAttribute('x', "-180.0")
    origin.setAttribute('y', "-90.0")
    tilemap.appendChild(origin)
    tileformat = document.createElement('tileformat')
    tileformat.setAttribute('extension', "tif")
    tileformat.setAttribute('height', "17")
    tileformat.setAttribute('mime-type', "image/tiff")
    tileformat.setAttribute('width', "17")
    tilemap.appendChild(tileformat)
    tilesets = document.createElement('tilesets')
    tilesets.setAttribute('profile', "global-geodetic")
    tilemap.appendChild(tilesets)
    list_tileset = ["10.588", "5.294", "2.647", "1.323", "0.661", "0.331"]
    for ordernum in range(6):
        tileset = document.createElement('tileset')
        tilesets.appendChild(tileset)
        tileset.setAttribute('href', "")
        tileset.setAttribute('order', str(ordernum))
        tileset.setAttribute('units-per-pixel', list_tileset[ordernum])
    EPSG = document.createTextNode('EPSG:4326')
    srs.appendChild(EPSG)

    default = document.createTextNode('default')
    tile.appendChild(default)
    with open(path, 'w') as fout:
        document.writexml(fout, addindent=' ', newl='\n')

    return None


def parse_xml(path):
    prase_dict = {}
    tree = et.ElementTree(file=path)
    root = tree.getroot()
    prase_dict["tilemap service"] = ''.join(root.attrib.values())
    for child in root:
        if child.tag == 'tile':
            prase_dict["title"] = child.text
    tileset_count = 0
    for child1 in root:
        if child1.tag == 'tilesets':
            for grandchild in child1:
                if grandchild.tag == 'tileset':
                    tileset_count += 1
    prase_dict["tileset count"] = tileset_count
    list_order = []
    for child2 in root:
        if child2.tag == 'tilesets':
            for grandchild2 in child2:
                if grandchild2.tag == 'tileset':
                    for art in grandchild2.attrib.keys():
                        if art == 'order':
                            list_order.append(grandchild2.attrib[art])
    max = int(list_order[0])
    for min in range(len(list_order)):
        if max >= int(list_order[min]):
            continue
        else:
            max = int(list_order[min])
    prase_dict["tileset max"] = max
    return prase_dict



if __name__ == "__main__":
    pass