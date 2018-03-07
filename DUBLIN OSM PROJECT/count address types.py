import operator
import xml.etree.cElementTree as ET

#Now in the tag 'tag' let's see what types of addresses we have inside the 'k' attribute and count them

OSM_FILE = "dublin_ireland.osm"


address_types = {}
for _, tag in ET.iterparse(OSM_FILE):
    if tag.tag == "tag" and tag.attrib['k'].startswith("addr:"):
        k = tag.attrib['k'][5:]
        address_types.setdefault(k, 0)
        address_types[k] += 1


for k,v in sorted(address_types.items(), key=operator.itemgetter(1), reverse=True):
    print(k, ':', v)
