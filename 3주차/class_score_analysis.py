def read_data(filename):
    data = []
    # TODO
    with open(filename, 'r') as f:
        next(f)
        for line in f.readlines():
            if line in '#':
                next(line)
            values = [int(text) for text in line.split(',')]
            data.append(values)
        return data

def add_weighted_average(data, weight):
    for row in data:
        wavg = weight[0]*row[0]+weight[1]*row[1]
        row.append(wavg)   # TODO
    return data

def analyze_data(data):
    mean = sum(data)/len(data)          
    var = sum([x**2 for x in data])/len(data) - mean**2    
    data.sort()
    median = 0 
    idx = 0
    if len(data) % 2 == 0:
        idx = len(data)//2
        median = (data[idx-1]+data[idx]/2)
    else:
        idx = len(data)//2
        median = data[idx]
        
    return mean, var, median, min(data), max(data)

if __name__ == '__main__':
    data = read_data('data/class_score_en.csv')
    if data and len(data[0]) == 2: # Check 'data' is valid
        add_weighted_average(data, [40/125, 60/100])
        if len(data[0]) == 3:      # Check 'data' is valid
            print('### Individual Score')
            print()
            print('| Midterm | Final | Total |')
            print('| ------- | ----- | ----- |')
            for row in data:
                print(f'| {row[0]} | {row[1]} | {row[2]:.3f} |')
            print()

            print('### Examination Analysis')
            col_n = len(data[0])
            col_name = ['Midterm', 'Final', 'Total']
            colwise_data = [ [row[c] for row in data] for c in range(col_n) ]
            for c, score in enumerate(colwise_data):
                mean, var, median, min_, max_ = analyze_data(score)
                print(f'* {col_name[c]}')
                print(f'  * Mean: **{mean:.3f}**')
                print(f'  * Variance: {var:.3f}')
                print(f'  * Median: **{median:.3f}**')
                print(f'  * Min/Max: ({min_:.3f}, {max_:.3f})')