from datetime import datetime
from dateutil.relativedelta import relativedelta


def dateConverter(input, output):
    file = input
    solution = open(output, "w")
    max = datetime.strptime('2049-01-01', '%Y-%m-%d')
    min = datetime.strptime('1950-01-01', '%Y-%m-%d')
    count = 0
    with open('gistfile1.txt', 'r') as file:
        for line in file:
            for format in ['%Y-%m-%d',
                           '%m/%d/%y',
                           '%m#%y#%d',
                           '%d*%m*%Y',
                           '%b %d, %y',
                           '%b %d, %Y']:
                try:
                    date = datetime.strptime(line.strip('\n'),format)
                    if date > max:
                        date = date - relativedelta(years=100)
                        converted = date.strftime('%Y-%m-%d')+'\n'
                    elif date < min:
                        date = date + relativedelta(years=100)
                        converted = date.strftime('%Y-%m-%d')+'\n'
                        print 'never happens'
                    else:
                        converted = date.strftime('%Y-%m-%d')+'\n'
                    print converted
                    count +=1
                    solution.write(converted)

                except:
                    pass

        print count
        solution.close()

dateConverter ('gistfile1.txt', 'output.txt')
