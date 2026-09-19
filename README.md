## Using the math library to Calculate the Given Information to Create a Circular Garden.

### This is a program that will calculate the area, circumference, square root of the area, rounded down area, and rounded up area of the circular garden or circle.

**How to Run**
1. Open the program on your device.
2. It will first ask you the radius of the circle in meters. Input the radius in meters.
3. Then, it will calculate the Area, Circumference, Square_Root, Rounded_Down_Area, and Rounded_Up_Area.
4. After that, it will input all of those calculations in the order it was said in a manner that can be understood properly.

***Input Needed***

Radius

**Sample Output**

Please enter the radius of the circle in meters: 7
The area of the circular garden is: 153.94 square meters.
The circumference of the circular garden is: 43.98 meters.
The square root of the area is: 12.41
The rounded circumference is: 153 square meters.
The rounded circumference is: 154 square meters.

**Author**

Maria Ysabel R. Cabarrubias

8 - Adelfa


## Computational Thinking
# Problem Identification 

The problem is to calculate the circular garden based on the radius.

# Problem Decomposition 

To make the program easier, I will divide it into the input, processing, and output stages.

The input stage will contain the radius given by the user.

The processing stage will contain every calculation that is needed which are area, circumference, square root, the rounded down values, and the rounded up values of the circular garden.

# Pattern Recognition 

I had noticed that most functions needed a math library, so I will include that in my program. 

# Data Representation 

I will represent my data using the float data type and use words like square meters and meters to create the correct unit for the values.

# Algorithm Development
import math
Assign Variable Radius from User's Float Input

Assign Variable Area that Calculates math.pi times radius to the power of 2.

Assign Variable Circumference that Calculates 2 times math.pi times Radius.

Assign Variable Square_Root that Calculates Square root of the Area.

Assign Variable Rounded_Down_Area that rounds down Area to the value less than OR equal to it.

Assign Variable Rounded_Up_Area that rounds down Area to the value greater than OR equal to it.

Output The area of the circular garden is and Area in two decimal places with Square meters.

Output The circumference of the circular garden is and Circumference in two decimal places with meters.

Output The square root of the circular garden is and Square_Root in two decimal places.

Output the Rounded Circumference is and Rounded_Down_Area.

Output the Rounded Circumference is and Rounded_Up_Area.
