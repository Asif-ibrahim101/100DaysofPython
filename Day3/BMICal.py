# BMI	Weight Status
# Below 18.5	Underweight
# 18.5 – 24.9	Healthy Weight
# 25.0 – 29.9	Overweight
# 30.0 and Above	Obesity
# BMI = Weight / Height * Height

print("welcome Lets tst your bmi :(");
Underweight = 18.5;
HealthyWeight = 24.9;
Obesity = 30.0;
overweight = 25.0;

Weight = float(input("What is your weight in kg: "));
Height = float(input("what is your height in meters: "));

Height_Cal = Height * Height;
BMI = round(Weight / Height_Cal);

if BMI < Underweight :
    print("your are underweight");
elif BMI == Underweight or BMI <= HealthyWeight:
    print("You are Healthy");
elif  BMI == overweight or BMI <= 29.9:
    print("You are over Weight");
elif BMI >= Obesity: 
    print("You are gonna die");
else:
    print("somethings wrong: (");