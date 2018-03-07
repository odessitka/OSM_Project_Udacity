import pprint
import xml.etree.cElementTree as ET

# Let's see what types of tags we have in OSM_FILE and count their numbers

OSM_FILE = "dublin_ireland.osm"


def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags


pprint.pprint(count_tags(OSM_FILE))
