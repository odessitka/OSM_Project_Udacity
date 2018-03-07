import pprint
import re
from collections import defaultdict
import xml.etree.cElementTree as ET

OSM_FILE = "dublin_ireland.osm"

#Mapping the typos and the abbreviations of the street types

expected_street_types= ['Road', 'Park', 'Avenue', 'Drive', 'Street', 'Grove', 'Crescent', 'Court', 'Lawn', 'Green',
                        'Close', 'Terrace', 'Rise', 'Place', 'Way', 'Gardens', 'Heights', 'View', 'Walk', 'Wood',
                        'Lane', 'Lawns', 'Estate', 'Square', 'Vale', 'Hill', 'Woods', 'Manor', 'Row', 'Quay', 'Parade',
                        'Glen', 'Mews', 'Meadows', 'Hills', 'Boulevard', 'Brae', 'Mount', 'Valley', 'Brook', 'Well',
                        'Plaza', 'Alley', 'Crossing', 'Rest', 'Field', 'Bridge', 'Dales', 'Bypass', 'Cove', 'Haven',
                        'Cross', 'Yard', 'End', 'Corner', 'Point', 'Lower', 'Upper', 'North', 'West', 'East', 'Middle',
                        'Great', 'Little']


mapping = {'Ave': 'Avenue',
           'St.': 'Street',
           'Rd.': 'Road',
           'Roafd': 'Road',
           'St': 'Street',
           'Rd': 'Road',
           'Avevnue': 'Avenue',
           'Nouth': 'North'}


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected_street_types:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r", encoding='utf-8')
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types


def update_name(name, mapping):
    m = street_type_re.search(name)
    if m:
        try:
            better_street_type = mapping[m.group()]
        except:
            better_street_type = m.group()
    return street_type_re.sub(better_street_type, name)


street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
st_types = audit(OSM_FILE)
pprint.pprint(dict(st_types))

for st_type, ways in st_types.items():
    for name in ways:
        better_name = update_name(name, mapping)
        print(name, "=>", better_name)