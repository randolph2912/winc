from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

import json
import os
import random

def random_koala_fact():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(module_path, "facts.json"), "r") as data_fp:
        facts = json.load(data_fp)
    return random.choice(facts)

def unique_koala_facts(num):
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(module_path, "facts.json"), "r") as data_fp:
        facts = json.load(data_fp)
    
    unique_facts = set()
    count = 0
    iterations = 0
    while len(unique_facts) < num and iterations < 1000:
        fact = random_koala_fact()
        if fact not in unique_facts:
            unique_facts.add(fact)
            count += 1
        iterations += 1
    return list(unique_facts)

def num_joey_facts():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(module_path, "facts.json"), "r") as data_fp:
        facts = json.load(data_fp)
    
    count = 0
    joey_facts = set()
    for fact in facts:
        if "joey" in fact.lower():
            joey_facts.add(fact)
    return len(joey_facts)

def koala_weight():
    module_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(module_path, "facts.json"), "r") as data_fp:
        facts = json.load(data_fp)

    for fact in facts:
        if "weigh" in fact.lower():
            words = fact.split()
            weight = words[words.index("weigh") + 2]
            try:
                weight_value = int(weight.split("kg")[0])
                return weight_value
            except ValueError:
                continue
    return None

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print("random_koala_fact:", random_koala_fact())
    print("random_koala_fact:", unique_koala_facts(8))
    print("Number of Joey facts:", num_joey_facts())
    print("Koala weight:", koala_weight(), "kg")








