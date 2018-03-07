import re
import operator
from collections import defaultdict
import xml.etree.cElementTree as ET

OSM_FILE = "dublin_ireland.osm"

#last word in the string ignoring the case
street_name_re = re.compile(r'\S+\.?$', re.IGNORECASE)
#counting the street types
street_types = defaultdict(int)
#dictionary for examples of using these street types
street_name_examples = defaultdict(list)

for _, tag in ET.iterparse(OSM_FILE):
    if tag.tag == "tag" and tag.attrib['k'] == "addr:street":
        street = tag.attrib['v']
        match = street_name_re.search(street)
        if match:
            name = match.group().lower()
            street_types[name] += 1
            if street_types[name] <= 3:
                street_name_examples[name].append(street)

for k,v in sorted(street_types.items(), key=operator.itemgetter(1), reverse=True):
    print(k, ':', v, ' [', ', '.join(street_name_examples[k]), ']')