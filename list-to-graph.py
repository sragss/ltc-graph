
import json
"""
Builds a dict of parent: [children...]

from 
parent:
-child1
-child2
parent2
-child1
-child2

assumes 1-deep tree, singly linked
"""
def build_graph(lines):
    graph = {}
    parent = ""
    for line in lines:
        line = line.strip()

        if line[0] == "-":
            # Non-root
            graph[parent].append(line[1:])
        
        else:
            # Root
            graph[line] = []
            parent = line
    return graph

"""returns the force-graph json format"""
def build_from_graph(graph):
    json_result = {}
    json_result["nodes"] = []
    json_result["links"] = []

    ROOT_NODE = "LTC.WRK"
    root_json = {}
    root_json["id"] = ROOT_NODE
    root_json["group"] = 0
    json_result["nodes"].append(root_json)

    parent_index = 1
    child_index = 2
    for parent in graph:
        parent_json = {}
        parent_json["id"] = parent
        parent_json["group"] = parent_index
        parent_json["hyper"] = "https://www.google.com"
        json_result["nodes"].append(parent_json)

        root_link = {}
        root_link["source"] = ROOT_NODE
        root_link["target"] = parent
        root_link["value"] = 1
        json_result["links"].append(root_link)
        for child in graph[parent]:
            child_json = {}
            child_json["id"] = child
            child_json["group"] = child_index
            json_result["nodes"].append(child_json)

            link_json = {}
            link_json["source"] = parent
            link_json["target"] = child
            link_json["value"] = 2
            json_result["links"].append(link_json)

        child_index += 1

    return json.dumps(json_result, indent=4)

in_filename = "data/blas.txt"
out_filename = "data/out.json"

with open (in_filename, "r") as in_file:
    data = in_file.readlines()
    graph = build_graph(data)
    result = build_from_graph(graph)
    with open(out_filename, "w") as out_file:
        out_file.write(result)
        out_file.close()
