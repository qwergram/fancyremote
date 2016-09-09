import bottle
import json

HISTORY = {}

@bottle.get('/report/<id_>/<report>/')
def update_report(id_, report):
    HISTORY.setdefault(id_, {"pass": 0, "fail": 0}).setdefault(report, 0)
    HISTORY[id_][report] += 1
    return "ok"


@bottle.get('/.json')
def show_report():
    return json.dumps(HISTORY, indent=2, sort_keys=True)

@bottle.get('/')
def show_pretty_report():
    return """
<!doctype html>
<html>
<head>
<style>
circle {
  fill: #ddd;
  stroke: #0074d9;
  stroke-width: 50;
  stroke-dasharray: 0 158;
  -webkit-transition: stroke-dasharray .3s ease;
  transition: stroke-dasharray .3s ease;
}

svg {
  margin: 0 auto;
  -webkit-transform: rotate(-90deg);
          transform: rotate(-90deg);
  background: #ddd;
  border-radius: 50%;
  display: block;
}

.buttons {
  margin-bottom: 30px;
}

button {
  text-transform: capitalize;
  font-size: 13px;
  cursor: pointer;
  -webkit-appearance: none;
  border: none;
  margin-right: 5px;
  background-color: transparent;
  padding: 5px 10px;
  outline: none;
  border-radius: 2px;
  -webkit-transition: background-color .1s ease, color .2s ease;
  transition: background-color .1s ease, color .2s ease;
}
button:last-of-type {
  margin-right: 0;
}
button.active {
  font-weight: 400;
  background-color: #0074d9;
  color: white;
}

figcaption {
  margin-bottom: 20px;
  font-size: 22px;
  font-weight: bold;
  text-align: center;
}

body {
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
      -ms-flex-pack: center;
          justify-content: center;
  -webkit-box-align: center;
  -webkit-align-items: center;
      -ms-flex-align: center;
          align-items: center;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
  font-family: 'Open Sans', sans-serif;
}

body, html {
  height: 100%;
}
</style>

</head>
</body>
<figure>
  <figcaption>
    Percentage of world population by continent
  </figcaption>
  
  <div class="buttons"></div>
  <svg width="100" height="100" class="chart">
    <circle r="25" cx="50" cy="50" class="pie"/>
  </svg>

</figure>

<script>
var total = 158,
    buttons = document.querySelector('.buttons'),
    pie = document.querySelector('.pie'),
    activeClass = 'active';

var continents = {""" + ",\n".join(["{}: {}".format(key, int((value['pass'] * 100) / (value['pass'] + value['fail']))) for key, value in HISTORY.items()]) + """};

// work out percentage as a result of total
var numberFixer = function(num){
  var result = ((num * total) / 100);
  return result;
}

// create a button for each country
for(property in continents){
  var newEl = document.createElement('button');
  newEl.innerText = property;
  newEl.setAttribute('data-name', property);
  buttons.appendChild(newEl);
}

// when you click a button setPieChart and setActiveClass
  buttons.addEventListener('click', function(e){
    if(e.target != e.currentTarget){
      var el = e.target,
          name = el.getAttribute('data-name');
      setPieChart(name);
      setActiveClass(el);
    }
    e.stopPropagation();
  });

var setPieChart = function(name){
  var number = continents[name],
      fixedNumber = numberFixer(number),
      result = fixedNumber + ' ' + total;
  
  pie.style.strokeDasharray = result;
}

var setActiveClass = function(el) {
  for(var i = 0; i < buttons.children.length; i++) {
    buttons.children[i].classList.remove(activeClass);
    el.classList.add(activeClass);
  }
}

// Set up default settings
//setPieChart('asia');
//setActiveClass(buttons.children[0]);
</script>

</body>
</html>
    
    """

bottle.run(host='localhost', port=5335)