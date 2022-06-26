# Metadata

Daniel

## Motivation

Sensors er noget der taget data fra din virkelige verden og indsætter det i den digitale. Actuators gør det modsatte. Dvs. at hvis har en sensor, så kan vi læse fra den og hvis vi har en actuator, så kan vi skrive til den.

Ontologies er defineret som
- Formal Naming and Definition
- Types, Properties, and Interrelationship of Entities
- Entities Existing in a Particular Domain

## RDF
The Resource Description Framework (RDF) kan bruges til at definere ontologies. En ontologies er en triple store. Her bruger han The Simpsons som eksempel på dette, hvor man har nodes med edges mellem dem. Disse nodes definere en state og en edge definere en egenskab de har. Generel definition er
- Triples er delt op i subject, predicate og object
- En triple store er en model
- Namespaces
- Subclasses og subproperties

Et eksempel er at Marge et er subject. "Parent of" er predicate og object kunne være Bart. Et predicate kunne være "is a" hvor object her ville være Female. Female kan være en subclass of Human.

Det hele her handler om, at jeg flere triples man har jo mere information har man.

### Tools
Turtle - The Terse RDF Triple Language (.ttl)
OWL: The Web <-> Ontology Language
    - Et sæt af extensions til RDF
    - Closed world assumption (Hvad man ikke kan bevise til at være sandt må være falsk)
Brick er en ontology til at lave Metadata
    - Har koncepter som typing, flows, physical encapsulation og control.
SparQL Query bruger pattern matching.

### Ontology Construction

Man bruger RDF til at definere modellen og schema.

Her kan man definere
- Types
- Relationships (Minder om types, men peger på en literal)
- Relationship Restrictions (At en model kun må indeholde specifikke relations)
- Type Equivalence (Bruges til at brigde to ontologies i en model, hvor man kan teste om f.eks. noget i et namespace er det samme som noget i et andet namespace)
- Restrictions between type and relationship (man kan begrænse hvor mange triples der kan følge et pattern. Dette er kendt som restriction on cardinality. F.eks. hvor mange at disse relations kan være ingoing og hvor mange kan være outgoing)
- Literals (datatypes)

### Validation of Model

En validator tester hvorvidt modellen passer på dens schema.
En reasoner kan anvende regler.
 
## Neo4J

Neo4J er en graph. Denne graph består af nodes og edges. Nodes består af
- Et sæt af labels
- En key-value store der indeholder named properties
- Et map fra relationhip type til et æt af outgoing relationships
- Et map fra relationship type til et sæt af incoming relationships

Relationships er edges og består af
- En single type
- En key-value store der indeholder named properties
- En source node
- En destination node

Når vi queuer noget, så går vi igennem et index. 