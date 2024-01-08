from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
{
  'id' : 1,
  'title' : 'Neckless',
  'location' : 'Dubai, Gold Souk',
  'Price' : 'DHs. 4,500'
},
  {
    'id' : 2,
    'title' : 'Chain',
    'location' : 'Dubai, Gold Souk',
    'Price' : 'DHs. 2,000'
  },

{
  'id' : 3,
  'title' : 'Ring',
  'location' : 'Dubai, Gold Souk',
  'Price' : 'DHs. 650'
},
{
  'id' : 4,
  'title' : 'Nosering',
  'location' : 'Dubai, Gold Souk',
  'Price' : 'DHs. 110'
}
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Al Naeem')

@app.route("jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)