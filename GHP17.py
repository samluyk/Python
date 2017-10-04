# Step 1: Ask for weight in pounds
# Step 2: Record user’s response
weight = input('Enter your weight in pounds: ')
# Step 3: Ask for height in inches
# Step 4: Record user’s input
height = input('Enter your height in inches: ')
# Step 5: Change “string” inputs into a data type float
weight_float = float(weight)
height_float = float(height)
# Step 6: Calculate BMI Imperial (formula: (5734 weight / (height*2.5))
BMI = (5734 * weight_float) / (height_float**2.5)
# Step 7: Display BMI
print("Your BMI is: ", BMI)
# Step 8: Convert weight to kg (formula: pounds * .453592)
weight_kg = weight_float * .453592
# Step 9: Convert height to meters (formula: inches * .0254)
height_meters = height_float * .0254
# Step 10: Calculate BMI Metric (formula: 1.3 * weight / height** 2.5
BMI = 1.3 * weight_kg / height_meters**2.5
# Step 11: Display BMI
print("Your BMI is: ", BMI)
# Step 12: Terminate
