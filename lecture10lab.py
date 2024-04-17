"""
EXERCISE 1

Open the file diamonds.csv, and explore it using .describe()

Then, use groupby() to create an object df_color which groups by color.
"""

"""
EXERCISE 2

The color is graded from D to Z, though it caps out at J in our data.
D is colorless and diamonds get progressively darker as we go towards J.
Colorless diamonds are the most desirable of diamonds and should be the most
expensive: https://www.lumeradiamonds.com/diamond-education/diamond-color

Using the method mean() check whether D-color diamonds are in fact
more expensive than other categories. Do you seen any trend? Is it in
the right direction?

Hint: Groupby objects can "call" columns e.g. 

    df_color["depth"].describe()

will give you summary statistics for the column named depth across 
groups. Try it out and see.
    
At this point you have to figure out the exact command to get a short
list of prices and your output should looks something like this:

color
D    3169.95
E    3076.75
F    3724.89
G    3999.14
H    4486.67
I    5091.87
J    5323.82
Name: price, dtype: float64

In other words - darker diamonds appear to be *more* expensive! In
contrast to our expectation that colorless diamonds should be more
expensive
"""

"""
EXERCISE 3

Here's a theory for why that's happening: our results are being
confounded by weight. Darker diamonds would usually sell for less
but in our dataset, they are also larger, which pushes up the price

To check whether this theory is plausible, check how the average 
weight (in carats) varies across groups. If it appears that darker
colors are also more larger, that lends support to this theory
"""

"""
EXERCISE 4

Short: check if the effect is softened when we "control" for size

Long: 1. Look up the average weight of diamonds in the dataset

2. Create an indicator variable called "small" that has the value 1 
if the diamond is smaller than the average weight and 0 otherwise

3. Create a groupby object using both color AND this indicator
variable

4. Check the mean price by group in this variable 
"""