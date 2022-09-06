suicidesperyear = [22, 56, 99, 112, 234, 162, 178, 215, 66, 253, 142, 87, 98, 213, 53, 33, 117, 136, 172, 298]

homicidesperyear = [15, 23, 54, 66, 87, 21, 112, 154, 167, 132, 64, 77, 143, 178, 200, 266, 149, 176, 89, 92]

legalinterventionperyear = [0, 0, 0, 2, 1, 4, 0, 6, 2, 1, 2, 3, 4, 0, 0, 2, 1, 3, 0, 4]

naturalperyear = [86, 23, 54, 99, 34, 12, 98, 54, 27, 65, 22, 74, 73, 66, 93, 32, 19, 33, 28, 21]

undeterminedperyear = [12, 88, 22, 16, 98, 44, 32, 100, 67, 43, 26, 43, 87, 84, 99, 105, 200, 103, 77, 51]


import statistics
statistics.pvariance(suicidesperyear)
statistics.stdev(suicidesperyear)

statistics.pvariance(homicidesperyear)
statistics.stdev(homicidesperyear)

statistics.pvariance(legalinterventionperyear)
statistics.stdev(legalinterventionperyear)

statistics.pvariance(naturalperyear)
statistics.stdev(naturalperyear)

statistics.pvariance(undeterminedperyear)
statistics.stdev(undeterminedperyear)

print('variance', statistics.pvariance(suicidesperyear))
print('standard deviation', statistics.stdev(suicidesperyear))
print('variance', statistics.pvariance(homicidesperyear))
print('standard deviation', statistics.stdev(homicidesperyear))
print('variance', statistics.pvariance(legalinterventionperyear))
print('standard deviation', statistics.stdev(legalinterventionperyear))
print('variance', statistics.pvariance(naturalperyear))
print('standard deviation', statistics.stdev(naturalperyear))
print('variance', statistics.pvariance(undeterminedperyear))
print('standard deviation', statistics.stdev(undeterminedperyear))

#missybernskoetter


