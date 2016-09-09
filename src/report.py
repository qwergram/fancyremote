import bottle
import json

HISTORY = {}

@bottle.get('/report/<id_>/<report>/')
def update_report(id_, report):
    HISTORY.setdefault(id_, {}).setdefault(report, 0)
    HISTORY[id_][report] += 1
    return "ok"


@bottle.get('/.json')
def show_report():
    return json.dumps(HISTORY, indent=2, sort_keys=True)

@bottle.get('/')

bottle.run(host='localhost', port=5335)