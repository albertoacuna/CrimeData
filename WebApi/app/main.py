from flask import Flask, jsonify, request

from csvReader import CSVReader, Search

app = Flask(__name__)
parsedData = CSVReader('static/CrimeStats.csv').dataArray
sortedArray = sorted(parsedData, key=lambda x: x['INC NUM'])

search = Search()
# parser = reqparse.RequestParser()
# parser.add_argument('speedGreaterThan', type=int, help='Speed of vehicle greater than')
# parser.add_argument('route_id', type=str, help='Speed of vehicle')


@app.route('/crimeData/')
def get_crime_data(methods=['GET']):
    result = sortedArray

    #Filters
    category = request.args.get('category')
    value = request.args.get('value')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    page_size = int(request.args.get('page_size'))
    page_number = int(request.args.get('page_number'))

    if category is not None and value is not None:
        result = search.search_by(result, category, value)
    if start_time is not None and end_time is not None:
        result = search.search_by_date_range(result, start_time, end_time)

    if page_size is  None and page_number is  None:
        page_size = 10
        page_number = 1

    array_start = (page_number - 1) * page_size
    array_end = page_number * page_size

    return jsonify({'total_records': len(result), 'result': result[array_start:array_end]})
