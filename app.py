from flask import Flask, request, render_template, jsonify
import pandas as pd
import networkx as nx
import numpy as np
from networkx.readwrite import json_graph
import json

#with open('data1.json') as json_file:
#    data = json.load(json_file)

#G = json_graph.node_link_graph(data)

edges = pd.read_csv('edges.csv')
nodes = pd.read_csv('nodes.csv')

G = nx.DiGraph()
for i in nodes['osmid']:
    G.add_node(i)
for i in range(len(edges)):
    G.add_edge(edges.iloc[i]['u'], edges.iloc[i]['v'], weight = edges.iloc[i]['length'])

def get_all_shortest_paths(node_id):
    return nx.single_source_dijkstra(G, id)

def get_shortest_path_to(start, end):
    path = nx.dijkstra_path(G, start, end, 'weight')
    cost = 0
    for i in range(len(path) - 1):
        cost += G[path[i]][path[i+1]]['weight']
    return (path, cost)


app = Flask(__name__)

def do_something(origin, dest):
    o = int(origin)
    d = int(dest)
    print(get_shortest_path_to(o, d)[0])
    return get_shortest_path_to(o, d)[0]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1,text2)
    result = {"output": combine}
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
