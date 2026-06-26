# ticket fare
child = int(input("Enter number of children: "))
adult = int(input("Enter number of adults: "))
old = int(input("Enter number of old people: "))
child_fare = child = 450
adult_fare = adult = 600
old_fare = old = 400
total_fare = (child * child_fare) + (adult * adult_fare) + (old * old_fare)
print("Total fare is:", total_fare)