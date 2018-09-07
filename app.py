from flask import Flask, render_template
from string import Template
import requests, json 

app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello World The ID ${id_num} is ${pokemon_name} ! </h1>   
	""")

@app.route('/', methods=['GET'])
def main():
    return """<h1>Hello world!</h1>"""

@app.route('/pokemon/<input>/')
def some_id_page(input):
	api_url = 'http://pokeapi.co/api/v2/pokemon/' + str(input) + '/' 
	r = requests.get(api_url)
	jforms = json.loads(r.text)
	
	if input.isdigit(): 
		some_name = jforms['name']
		return(HTML_TEMPLATE.substitute(id_num= input, pokemon_name=some_name))
	else:
		some_id = jforms['id']
		return(HTML_TEMPLATE.substitute(id_num= some_id, pokemon_name= input))


if __name__ == '__main__':
    app.run()
