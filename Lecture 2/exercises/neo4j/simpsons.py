#!/usr/bin/env python3

from unicodedata import name
from neo4j import GraphDatabase

# docker run -p7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/s3cr3t neo4j

HOSTNAME = "localhost"
PORT     = 7687
USERNAME = "neo4j"
PASSWORD = "s3cr3t"

###############################################################################
################################################################## Helpers ####

def pprint (data):
  for ix, record in enumerate(data):
    vs = record.values()
    print(ix, vs)

###############################################################################
############################################################### initialize ####

auth = (USERNAME, PASSWORD)
driver = GraphDatabase.driver("neo4j://%s:%d" % (HOSTNAME, PORT), auth=auth)
session = driver.session()

###############################################################################
########################################################### clear database ####

# https://stackoverflow.com/a/60933970
with driver.session() as session:
  session.run("MATCH (a) -[r] -> () DELETE a, r")
  session.run("MATCH (a) DELETE a")

###############################################################################
##################################################################### Data ####

def create_person(tx, name, gender):
  return tx.run("CREATE (a:Person {name: $name, sex: $gender}) RETURN id(a)", name=name, gender=gender).single().value();

def create_relationship(tx, parent, child):
  return tx.run("MATCH (a:Person), (b:Person) where a.name=$parent AND b.name=$child CREATE (a)-[r:parentOf]->(b) RETURN type(r)", parent=parent, child=child).single().value();

def create_older_than_relationship(tx, person1, person2):
  return tx.run("MATCH (a:Person), (b:Person) where a.name=$person1 AND b.name=$person2 CREATE (a)-[r:olderThan]->(b) RETURN type(r)", person1=person1, person2=person2).single().value();

with driver.session() as session:
  session.write_transaction(create_person, 'Maggie', 'female')
  session.write_transaction(create_person, 'Marge', 'female')
  session.write_transaction(create_person, 'Lisa', 'female')
  session.write_transaction(create_person, 'Homer', 'male')
  session.write_transaction(create_person, 'Bart', 'male')
  
  session.write_transaction(create_relationship, 'Homer', 'Bart')
  session.write_transaction(create_relationship, 'Homer', 'Lisa')
  session.write_transaction(create_relationship, 'Homer', 'Maggie')
  session.write_transaction(create_relationship, 'Marge', 'Bart')
  session.write_transaction(create_relationship, 'Marge', 'Lisa')
  session.write_transaction(create_relationship, 'Marge', 'Maggie')

  session.write_transaction(create_older_than_relationship, 'Lisa', 'Maggie')
  session.write_transaction(create_older_than_relationship, 'Bart', 'Lisa')
  session.write_transaction(create_older_than_relationship, 'Homer', 'Marge')


###############################################################################
################################################################## queries ####

q1 = \
'''
MATCH
  (maggie:Person {name: 'Maggie'}),
  (mother:Person {sex: 'female'}),
  (sister:Person {sex: 'female'}),
  (mother) -[:parentOf]-> (maggie),
  (mother) -[:parentOf]-> (sister),
  (sister) -[:olderThan*]-> (maggie)
RETURN sister.name
'''
print('Maggie has the following older sister(s):')
with driver.session() as session:
  data = session.run(q1)
  pprint(data)
print('')

q2 = \
'''
MATCH
  (father:Person {sex: 'male'}),
  (daughter:Person {sex: 'female'}),
  (father) -[:parentOf]-> (daughter)
RETURN father.name, daughter.name
'''
print('All farther-daugther pairs:')
with driver.session() as session:
  data = session.run(q2)
  pprint(data)
print('')

q3 = \
'''
MATCH
  (person:Person)
RETURN person.name, person.sex
'''
print('List all persons with gender:')
with driver.session() as session:
  data = session.run(q3)
  pprint(data)
print('')

q4 = \
'''
MATCH
  (parent:Person),
  (child:Person),
  (parent) -[:parentOf]-> (child)
WHERE parent.sex = child.sex
RETURN parent.name, child.name
'''
print('List all parent-child pairs of same gender:')
with driver.session() as session:
  data = session.run(q4)
  pprint(data)
print('')

q5 = \
'''
MATCH
  (marge:Person {name: 'Marge'}),
  (homer:Person {name: 'Homer'}),
  (homer) -[rel_ref]-> (marge),
  (src:Person),
  (dst:Person),
  (src) -[rel_candidate]-> (dst)
WHERE
  src <> dst AND
  type(rel_candidate)=type(rel_ref)
RETURN src.name, dst.name
'''
print('List all pairs of humans who share a relationship with marge and homer:')
with driver.session() as session:
  data = session.run(q5)
  pprint(data)
print('')

###############################################################################
################################################################# finalize ####

driver.close()

