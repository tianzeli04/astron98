count = 0
for i in range(100):
    if (i % 4 == 0) or (i % 5 == 0) or (i % 6 == 0):
        count += 1
print(count)

#I learned about the principle of inclusion and exclusion in math 74 and my professor named it "teenage PIE" because it's slightly more sophisticated than "baby PIE". 

#python TeenagePIE.py