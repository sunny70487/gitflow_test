from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/graph/fields')
def fetch_graph_fields():
    nodes_fields = [{"field_name": "id", "type": "string"},
                    {"field_name": "title", "type": "string",
                     },
                    {"field_name": "subTitle", "type": "string"},
                    {"field_name": "mainStat", "type": "string"},
                    {"field_name": "secondaryStat", "type": "number"},
                    {"field_name": "arc__failed",
                     "type": "number", "color": "red", "displayName": "Failed"},
                    {"field_name": "arc__passed",
                     "type": "number", "color": "green", "displayName": "Passed"},
                    {"field_name": "detail__role",
                     "type": "string", "displayName": "Role"}]
    edges_fields = [
        {"field_name": "id", "type": "string"},
        {"field_name": "source", "type": "string"},
        {"field_name": "target", "type": "string"},
        {"field_name": "mainStat", "type": "number"},
    ]
    result = {"nodes_fields": nodes_fields,
              "edges_fields": edges_fields}
    return jsonify(result)


@app.route('/api/graph/data')
def fetch_graph_data():

    nodes = [{"id": "1", "title": "Service1", "subTitle": "instance:#2", "detail__role": "load",
              "arc__failed": 0.7, "arc__passed": 0.3, "mainStat": "aaa"},
             {"id": "2", "title": "Service2", "subTitle": "instance:#2", "detail__role": "transform",
              "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "b"},
             {"id": "3", "title": "Service3", "subTitle": "instance:#3", "detail__role": "extract",
              "arc__failed": 0.3, "arc__passed": 0.7, "mainStat": "c"},
             {"id": "4", "title": "Service3", "subTitle": "instance:#1", "detail__role": "transform",
              "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "d"},
             {"id": "5", "title": "Service4", "subTitle": "instance:#5", "detail__role": "transform",
              "arc__failed": 0.5, "arc__passed": 0.5, "mainStat": "e"}]
    edges = [{ "source": "1", "target": "2", "mainStat": 10},
             {"id": "1", "source": "2", "target": "3", "mainStat": 20},
             {"id": "1", "source": "1", "target": "4", "mainStat": 30},
             {"id": "1", "source": "3", "target": "5", "mainStat": 40},
             {"id": "1", "source": "2", "target": "5", "mainStat": 50}]
    result = {"nodes": nodes, "edges": edges}
    return jsonify(result)


@app.route('/api/health')
def check_health():
    return "API is working well!"


app.run(host='0.0.0.0', port=5000,debug=True)