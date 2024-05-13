from flask import Flask, render_template
from py2neo import Graph

app = Flask(__name__)
graph = Graph("bolt://localhost:7687", auth=("neo4j", "gx901205"))

@app.route('/')
def index():
    # 在这里编写查询语句来从 Neo4j 中检索数据
    # 例如：results = graph.run("MATCH (n) RETURN n LIMIT 10").data()
    results = []  # 假设这里是你的查询结果，格式为列表字典

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
