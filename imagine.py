from PIL import Image, ImageDraw, ImageFont
import os
import networkx as nx
import math
import random

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 128, 0)


def makegraph(G, nodes, x_size, y_size):
    filename = "graph.png"
    image = Image.new(mode="RGB", size=(x_size, y_size), color=black)
    draw = ImageDraw.Draw(image)
    step = int(image.size[0] / 10)

    # for i in range(0, image.size[0], step):
    #     draw.line((0, i, image.size[0], i), black)
    #     draw.line((i, 0, i, image.size[1]), black)
    # for n in nodes:
    #     x1 = n.xpos + 1
    #     x2 = n.xpos - 1
    #     y1 = n.ypos + 1
    #     y2 = n.ypos - 1
    #     draw.ellipse((x2, y2, x1, y1), fill=blue, outline=red, width=2)
    for u, v in G.edges():
        x1 = G.nodes[u]['x']
        y1 = G.nodes[u]['y']
        x2 = G.nodes[v]['x']
        y2 = G.nodes[v]['y']
        draw.line((x1, y1, x2, y2), white)
    for i in range(3):
        val = random.randrange(0, len(nodes))
        val2 = val
        while val2 == val:
            val2 = random.randrange(0, len(nodes))
        pathlist = nx.shortest_path(G, source=(val), target=(val2))
        drawpath(pathlist, draw, G)
        print(pathlist)
        s = " ".join(str(x) for x in pathlist)
        f.write(s)
        f.write("\n")

    # for p in range(len(pathlist)-1):
    #     x1 = G.nodes[pathlist[p]]['x']
    #     y1 = G.nodes[pathlist[p]]['y']
    #     x2 = G.nodes[pathlist[p+1]]['x']
    #     y2 = G.nodes[pathlist[p+1]]['y']
    #     draw.line((x1, y1, x2, y2), red, width=5)
    image.save(filename)
    # os.system(filename)


def drawpath(list, draw, G):
    f = open("output", "w")
    for p in range(len(list) - 1):
        x1 = G.nodes[list[p]]['x']
        y1 = G.nodes[list[p]]['y']
        x2 = G.nodes[list[p + 1]]['x']
        y2 = G.nodes[list[p + 1]]['y']
        ls = [x1, y1, x2, y2]
        draw.line((x1, y1, x2, y2), red, width=5)
        s = " ".join(str(x) for x in ls)
        f.write("toih")
        f.write(s)
        f.write("\n")
