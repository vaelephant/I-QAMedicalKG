import os
from py2neo import Graph

# 获取当前脚本所在目录的上层目录，用于构建数据文件路径
cur_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(cur_dir, 'D:/code/QAMedicalKG/data/medical2.json')  # 获取json文件路径

# 连接本地 Neo4j 数据库
graph = Graph("bolt://localhost:7687", auth=("net4j", "txys666666"))

# 确认连接
if graph:
    print("成功连接到数据库！")
else:
    print("无法连接到数据库！")
