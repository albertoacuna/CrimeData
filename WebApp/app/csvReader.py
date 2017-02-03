import csv


class CSVReader:
    def __init__(self, filename):
        self.dataArray = []

        with open(filename, newline='') as f:
            reader = csv.reader(f)
            iter = 0
            for row in reader:
                if iter != 0:
                    row = {
                        'INC NUM': row[0],
                        'OCCURED_ON': row[1],
                        'OCCURED_TO': row[2],
                        'UCR CRIME CATEGORY': row[3],
                        '100 BLOCK ADDR': row[4],
                        'ZIP': row[5],
                        'PREMISE_TYPE': row[6],
                    }
                    self.dataArray.append(row)
                iter += 1


class Search:
    def __init__(self, obj):
        self.dataArray = obj

    def search_by(self, category, value):
        match = [self.dataArray[i] for i, obj in enumerate(self.dataArray) if obj[category] == value]

        return match

# t = CSVReader('CrimeStats.csv')
# searchObj = Search(t.dataArray)
#
# res = searchObj.search_by('UCR CRIME CATEGORY', 'RAPE')
#
# print(res)
