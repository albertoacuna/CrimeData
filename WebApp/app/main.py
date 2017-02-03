from flask import Flask, jsonify

from csvReader import CSVReader, Search

print(__name__)
app = Flask(__name__)
parsedData = CSVReader('static/CrimeStats.csv')
search = Search(parsedData.dataArray)
# parser = reqparse.RequestParser()
# parser.add_argument('speedGreaterThan', type=int, help='Speed of vehicle greater than')
# parser.add_argument('route_id', type=str, help='Speed of vehicle')


@app.route('/crimeData/')
@app.route('/crimeData/<category>/<value>/')
def getCrimeData(category=None, value=None, methods=['GET']):
    # response = url_request.urlopen('https://transitdata.phoenix.gov/api/vehiclepositions?format=json')
    # string = response.read().decode('utf-8')
    # parsedData = json.loads(string)

    # timeStamp = parsedData['header']['timestamp']
    # parsedTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S')

    result = search.search_by(category, value)

    return jsonify({ 'result': result})