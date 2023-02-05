import os
import random
import collections
import networkx as nx
import math
from PIL import Image, ImageDraw

# constants for graph and image construction
x_size = 256
y_size = 256
nodes_amount = 250
G = nx.Graph()
MAX = 25
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 128, 0)


def main():
    asdf = True
    nodeslist = makemap()
    makeedges()
    makegraph(nodeslist)
    asdf = not asdf

def makeedges():
    for n in G:
        x1 = G.nodes[n]['x']
        y1 = G.nodes[n]['y']
        for n2 in G:
            x2 = G.nodes[n2]['x']
            y2 = G.nodes[n2]['y']
            distance = math.dist([x1, y1], [x2, y2])
            if distance < MAX:
                G.add_edge(n, n2, weight=distance)


def makemap(nodeslist=collections.deque()):
    for x in range(nodes_amount):
        n1 = Node()
        nodeslist.append(n1)
        G.add_node(x, x=n1.xpos, y=n1.ypos)
    return nodeslist


def makegraph(nodes):
    filename = "graph.png"
    image = Image.new(mode="RGB", size=(x_size, y_size), color=black)
    draw = ImageDraw.Draw(image)
    for u, v in G.edges():
        x1 = G.nodes[u]['x']
        y1 = G.nodes[u]['y']
        x2 = G.nodes[v]['x']
        y2 = G.nodes[v]['y']
        draw.line((x1, y1, x2, y2), blue)
    # draw 3 shortest paths on the generated graph
    for i in range(3):
        val = random.randrange(0, len(nodes))
        val2 = val
        while val2 == val:
            val2 = random.randrange(0, len(nodes))
        pathlist = nx.shortest_path(G, source=(val), target=(val2))
        drawpath(pathlist, draw, G)
        print(pathlist)
    image.save(filename)


def drawpath(pathnodeslist, draw, G):
    f = open("output.txt", "a")
    for p in range(len(pathnodeslist) - 1):
        x1 = G.nodes[pathnodeslist[p]]['x']
        y1 = G.nodes[pathnodeslist[p]]['y']
        x2 = G.nodes[pathnodeslist[p + 1]]['x']
        y2 = G.nodes[pathnodeslist[p + 1]]['y']
        ls = [x1, y1, x2, y2]
        draw.line((x1, y1, x2, y2), red, width=1)
        s = " ".join(str(x) for x in ls)
        number = repr(p)
        # f.write("Edge " + number + ": ")
        # f.write(s)
        # f.write("\n")
    for i in pathnodeslist:
        x = G.nodes[i]['x']
        y = G.nodes[i]['y']
        realx = x
        realy = y
        x = x - (x_size/2)
        x = x/10
        y = -(y - (y_size/2))
        y = y/10
        coordinateslist = [x, y]
        string = ", ".join(str(x) for x in coordinateslist)
        # draw.text((realx, realy), string, stroke_fill=blue)
        f.write("(")
        f.write(string)
        f.write(")")
        f.write("\n")


class Node:
    def __init__(self):
        self.xpos = random.randrange(0, x_size)
        self.ypos = random.randrange(0, y_size)


if __name__ == "__main__":
    main()
