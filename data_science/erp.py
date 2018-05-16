import csv
import matplotlib.pyplot as plt

with open('eeg.csv', 'r') as fh:
    rows = csv.DictReader(fh)
    rows = list(rows)
    yvals = []
    assign = []
    a = []
    test = []
    
    for i in range(0,501): 
        assign.append(str(i))
        
    xvals = []
    for i in range(0,501): #creating a list of lists to store yvals
        xvals.append(a)
    
    for num in range(0,501):
        for row in rows:
            test.append(float(row[assign[num]]))
        xvals[num] = test
        test = []
        yvals.append(sum(xvals[num])/len(xvals[num]))
    
    x_values = []
    for ints in range(0,501):
        x_values.append(ints)
    
    plt.plot(x_values, yvals, color='green')
    plt.axis([0,500,-11,8.2]) 
    plt.show()
