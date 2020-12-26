# TODO(sragsdale):
- Add JSON link in README
- Add hyperlink to python script
- Try different background color
- Clean up HTML so it's easy to add to any site (with example for window-in-window)

# Graphs
Short code sample of the LTC.WRK graph implemented using [vasturiano's force-graph library](https://github.com/vasturiano/3d-force-graph). 

# Styling
The graph can likely be restyled–the version seen here is as default as it gets.

# Running local
Easiest way to test this is to use a simple local server.
```
$ npm install -g live-server
$ live-server
```

# Generating the graph
The graph input consists of a JSON file describing nodes and links.
TODO(sragsdale): link the JSON file.


I got bored writing this by hand so I wrote the python script to generate. The python script takes input from in.txt in the following form:
```
parent1,<parent 1 hyper-link>
-child1,<child 1 hyper-link>
-child2,<child2 hyper-link>
...
parent2<parent 2 hyper-link>
-child3,<child 3 hyper-link>
```
The script assumes a 1 layer tree and is was written very rapidly. If the tree becomes any more complicated, this script will no longer work and the linking will need to be described directly with json (see above).
