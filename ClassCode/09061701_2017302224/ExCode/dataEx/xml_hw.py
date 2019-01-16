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
    from xml.dom import minidom
    try:
        f = open(path, "w")
        try:
            doc = minidom.Document()

            tilemap = doc.createElement("tilemap")
            tilemap.setAttribute("tilemapservice", "http://tms.osgeo.org/1.0.0")
            tilemap.setAttribute("version", "1.0.0")
            doc.appendChild(tilemap)

            title = doc.createElement("title")
            tilemap.appendChild(title)
            titletext = doc.createTextNode("default")
            title.appendChild(titletext)

            author = doc.createElement("abstract")
            tilemap.appendChild(author)

            srs = doc.createElement("srs")
            tilemap.appendChild(srs)
            srctext = doc.createTextNode("EPSG:4326")
            srs.appendChild(srctext)

            vsrs = doc.createElement("vsrs")
            tilemap.appendChild(vsrs)

            boundingbox = doc.createElement("boundingbox")
            boundingbox.setAttribute("maxx", "180.0")
            boundingbox.setAttribute("maxy", "90.0")
            boundingbox.setAttribute("minx", "-180.0")
            boundingbox.setAttribute("miny", "-90.0")
            tilemap.appendChild(boundingbox)

            oringin = doc.createElement("oringin")
            oringin.setAttribute("x","-180.0")
            oringin.setAttribute("y","-90.0")
            tilemap.appendChild(oringin)

            tileformat = doc.createElement("tileformat")
            tileformat.setAttribute("extension","tif")
            tileformat.setAttribute("height", "17")
            tileformat.setAttribute("mime-type", "image/tiff")
            tileformat.setAttribute("width", "17")
            tilemap.appendChild(tileformat)

            tilesets = doc.createElement("tilesets")
            tilesets.setAttribute("profile", "global-geodetic")
            tilemap.appendChild(tilesets)

            tileset = doc.createElement("tileset")
            tileset.setAttribute("href", "")
            tileset.setAttribute("order", "0")
            tileset.setAttribute("units-per-pixel", "10.588")
            tilesets.appendChild(tileset)

            tileset = doc.createElement("tileset")
            tileset.setAttribute("href", "")
            tileset.setAttribute("order", "1")
            tileset.setAttribute("units-per-pixel", "5.294")
            tilesets.appendChild(tileset)

            tileset = doc.createElement("tileset")
            tileset.setAttribute("href", "")
            tileset.setAttribute("order", "2")
            tileset.setAttribute("units-per-pixel", "2.647")
            tilesets.appendChild(tileset)

            tileset = doc.createElement("tileset")
            tileset.setAttribute("href", "")
            tileset.setAttribute("order", "3")
            tileset.setAttribute("units-per-pixel", "1.323")
            tilesets.appendChild(tileset)

            tileset = doc.createElement("tileset")
            tileset.setAttribute("href", "")
            tileset.setAttribute("order", "4")
            tileset.setAttribute("units-per-pixel", "0.661")
            tilesets.appendChild(tileset)

            tileset = doc.createElement("tileset")
            tileset.setAttribute("href", "")
            tileset.setAttribute("order", "5")
            tileset.setAttribute("units-per-pixel", "0.331")
            tilesets.appendChild(tileset)

            doc.writexml(f, "\t", "\t", "\n")
        except:
            print("open file failed")
        finally:
            f.close()
    except:
        print("open file failed")


def parse_xml(path):
    tree = et.parse("%s"%path)
    root = tree.getroot()
    setorder = 0
    dic = {}
    dic['tilemap service'] = root.attrib['tilemapservice']+' '
    for child in root:
        for title in root.findall('title'):
            att = title.text
            dic['title'] = att
        for tilesets in root.findall('tilesets'):
            tilesetcount = 0
            for tileset in tilesets.findall('tileset'):
                if 'tileset' in str(tileset):
                    if tileset.get('order'):
                        order = tileset.get('order')
                        if int(order) > setorder:
                            setorder = int(order)
                            dic['tileset max'] = setorder
                tilesetcount += 1
                dic['tileset count'] = tilesetcount
    return dic


if __name__ == "__main__":
    pass
