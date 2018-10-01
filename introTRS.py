#Rosalind Introduction to Random Strings
#http://rosalind.info/problems/prob/ Soroush

import math
string = "TGTCTCGACATGGTCTAGTATGGACAGGTCTTGGTATCTACGAGTCGAGTGATCGCAAACAGTGGTTATGGATCTTACCAATTAACCTTCGGATTAAGCG"
prob = "0.104 0.169 0.189 0.282 0.339 0.434 0.473 0.503 0.582 0.631 0.730 0.759 0.821 0.891"
prob = prob.split(" ")
final = 1

for z in prob:
    for x in string:
        if (x == "A") or (x == "T"):
            final = final* (1-float(z))/2
        elif (x == "G") or (x == "C"):
            final = final * float(z) /2
    print "%.3f" % round((math.log10(final)), 3),
    final = 1
