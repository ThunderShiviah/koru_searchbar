import csv
with open('../data/college_only', 'rb') as csvfile:

    n = 1    
    for row in csvfile:
        print '<option value=/"%d">%s</option>' % (n, row.strip())
        n = n + 1
