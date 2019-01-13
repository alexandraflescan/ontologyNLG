import random
import pprint
import copy

from Utils import *

g = rdflib.Graph()

g.parse('harryPotter_ont.owl')

prefixes = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX base: <http://www.semanticweb.org/alexandra/ontologies/2018/5/untitled-ontology-27#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>"""

def get_properties():
    properties = g.query(prefixes + """
SELECT  ?objectProperty WHERE {
  ?objectProperty rdf:type owl:ObjectProperty 
} LIMIT 70
""")

    return to_list(properties)
print (get_properties())

def get_subclasses(ontologyClass):
    subclasses = g.query(prefixes + """
SELECT DISTINCT ?subClass WHERE {
  ?subClass rdfs:subClassOf* base:""" + ontologyClass + " }")
    return to_list(subclasses)


# print(get_subclasses('Pizza'))

def get_domain(property):
    domain_triples = g.query(prefixes + """
    SELECT DISTINCT ?domain  
    WHERE { base:""" + property + """ rdfs:domain ?domain.   
    }
       """)
    print (to_list(domain_triples))
    return to_list(domain_triples)


# print(get_domain('hasTopping'))


def get_range(properties):
    range_triples = g.query(prefixes + """
    SELECT DISTINCT ?range  
    WHERE { base:""" + properties + """ rdfs:range ?range.   
    }
       """)
    return to_list(range_triples)


def get_sentence_words():
    output_sentence = {}
    pro = get_properties()
    for p in pro:
        domain = get_domain(p)
        if len(domain) != 1:
            continue
        subdom = get_subclasses(domain[0])
        range = get_range(p)
        if len(range) != 1:
            continue
        subrange = get_subclasses(range[0])
        output_sentence[p] = {'domain': subdom, 'range': subrange}
    return output_sentence

def normalize_camelcase( text):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', text)
    return " ".join([m.group(0) for m in matches]).lower()
def normalize_camelcase_transform_property( text):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', text)
    return [m.group(0) for m in matches]

def get_domain_range():
    sent_word = get_sentence_words()
    domain_range = {}
    property = random.sample(sent_word.keys(), 1)[0]
    domains = random.sample(sent_word[property]['domain'], 3)
    ranges = random.sample(sent_word[property]['range'], 3)
    properties = normalize_camelcase_transform_property(property)



    domain_range['property'] = properties[0].lower()
    domain_range['range'] = [normalize_camelcase(r) for r in ranges]
    domain_range['domain'] = [normalize_camelcase(d) for d in domains]

    domain_range['generic'] = properties[-1] if len(properties) >= 2 else 'thing'
    return domain_range


domain_range = get_domain_range()
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(get_properties() + sent_word['hasTopping']['domain'])
# pp.pprint(get_properties() + sent_word['hasTopping']['range'])


