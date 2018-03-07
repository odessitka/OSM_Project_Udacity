import re
from collections import defaultdict
import xml.etree.cElementTree as ET

OSM_FILE = "dublin_ireland.osm"

### Checking the addresses with addictive street types as Lower, West, Great
list_of_street_types = ['Lower', 'Upper', 'North', 'West', 'East', 'Middle', 'Great', 'Little']

street_name_re = re.compile(r'\S+\.?$', re.IGNORECASE)
#dictionary with unique street names for every street type we audit
street_types_examples = defaultdict(set)


for _, tag in ET.iterparse(OSM_FILE):
    if tag.tag == "tag" and tag.attrib['k'] == "addr:street":
        street = tag.attrib['v']
        match = street_name_re.search(street)
        if match:
            name = match.group()
            if name in list_of_street_types:
                street_types_examples[name].add(street)


for t in list_of_street_types:
    print(t)
    print(street_types_examples[t])