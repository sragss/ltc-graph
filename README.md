# TODO(sragsdale):
- Add JSON link in README
- Add hyperlink to python script
- Try different background color
- Clean up HTML so it's easy to add to any site (with example for window-in-window)

# Graphs
Short code sample of the LTC.WRK graph implemented using [vasturiano's force-graph library](https://github.com/vasturiano/3d-force-graph). 

# Generating the graph
The graph input consists of a JSON file describing `nodes` and `links`. This can be manually edited. `data/ltc.json` contains the example graph structure. Note that some nodes have a "hyper" field which is what they'll link to. In the example json all those with the hyper field link to `https://www.yahoo.com`.
TODO(sragsdale): link the JSON file.


## Python generation script `list-to-graph.py`
I got bored writing this graph by hand so I wrote the python script to generate. The python script takes input from in.txt in the following form:
```
parent1,<parent 1 hyper-link>
-child1,<child 1 hyper-link>
-child2,<child2 hyper-link>
...
parent2<parent 2 hyper-link>
-child3,<child 3 hyper-link>
```
The script assumes a 1 layer tree and is was written quick and dirty. If the tree becomes any more complicated, this script will no longer work and the linking will need to be described directly with json (see above).

# Styling
The graph can likely be restyled–the version seen here is as default as it gets.

# Running local
Easiest way to test this is to use a simple local server.
```
$ npm install -g live-server
$ live-server
```
