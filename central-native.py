# """Module 2 Project to determine central tendencies."""

values = [47, 95, 88, 73, 88, 84]

# Calculate the count of the values
total = 0 
value_counter = 0
values = [47, 95, 88, 73, 88, 84]

for value in values:
    total += value
    value_counter += 1
    
print(f'The count is {value_counter}')
    
# Calculate the sum of the values
total = 0
for number in [47, 95, 88, 73, 88, 84]:
    total = total + number

total

# Calculate the mean of the values
total = 0 
value_counter = 0
values = [47, 95, 88, 73, 88, 84]

for value in values:
    total += value
    value_counter += 1
    
mean = total/value_counter
print(f'The mean is {mean}')

# Calculate the median of the values
values = [47, 95, 88, 73, 88, 84]

values1 = sorted(values)

if len(values1) % 2 == 0:
   first_median = values1[len(values1) // 2]
   second_median = values1[len(values1) // 2 - 1]
   median = (first_median + second_median) / 2
else:
   median = values1[len(values1) // 2]
print(values1)
print("Median of above list is: " + str(median))

# Calculate the mode of the values
values = [47, 95, 88, 73, 88, 84]

mode = max(values, key = values.count)
print(f'The mode is {mode}')