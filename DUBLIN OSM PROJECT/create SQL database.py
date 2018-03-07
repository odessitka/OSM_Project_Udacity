import csv
import sqlite3
db = sqlite3.connect('dublin.db')
cur = db.cursor()

# create table nodes
cur.execute("CREATE TABLE IF NOT EXISTS nodes (\
    id INTEGER PRIMARY KEY NOT NULL,\
    lat REAL,\
    lon REAL,\
    user TEXT,\
    uid INTEGER,\
    version INTEGER,\
    changeset INTEGER,\
    timestamp TEXT);")


# insert data to nodes
db.text_factory = str
with open('nodes.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = []
    for i in dr:
        to_db = (i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp'])
        cur.execute("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
                    to_db)
db.commit()


# create table nodes_tags
cur.execute("CREATE TABLE nodes_tags (\
    id INTEGER,\
    key TEXT,\
    value TEXT,\
    type TEXT,\
    FOREIGN KEY (id) REFERENCES nodes(id));")

# insert data to nodes_tags
with open('nodes_tags.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = []
    for i in dr:
        to_db = (i['id'], i['key'], i['value'], i['type'])
        cur.execute("INSERT INTO nodes_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
db.commit()


# create table ways
cur.execute("CREATE TABLE ways (\
    id INTEGER PRIMARY KEY NOT NULL,\
    user TEXT,\
    uid INTEGER,\
    version TEXT,\
    changeset INTEGER,\
    timestamp TEXT);")

# insert data to ways
with open('ways.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = []
    for i in dr:
        to_db = (i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp'])
        cur.execute("INSERT INTO ways(id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);",
                    to_db)
db.commit()

# create table ways_tags
cur.execute("CREATE TABLE ways_tags (\
    id INTEGER NOT NULL,\
    key TEXT NOT NULL,\
    value TEXT NOT NULL,\
    type TEXT,\
    FOREIGN KEY (id) REFERENCES ways(id));")

# insert data to ways_tags
with open('ways_tags.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = []
    for i in dr:
        to_db = (i['id'], i['key'], i['value'], i['type'])
        cur.execute("INSERT INTO ways_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
db.commit()


# create table ways_nodes
cur.execute("CREATE TABLE ways_nodes (\
    id INTEGER NOT NULL,\
    node_id INTEGER NOT NULL,\
    position INTEGER NOT NULL,\
    FOREIGN KEY (id) REFERENCES ways(id),\
    FOREIGN KEY (node_id) REFERENCES nodes(id));")

# insert data to ways_nodes
with open('ways_nodes.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    to_db = []
    for i in dr:
        to_db = (i['id'], i['node_id'], i['position'])
        cur.execute("INSERT INTO ways_nodes(id, node_id, position) VALUES (?, ?, ?);", to_db)
db.commit()

db.close()