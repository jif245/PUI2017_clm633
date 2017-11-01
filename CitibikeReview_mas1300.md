
Recommendations:

I would recommend adding more scientific notation, as is found in the lab notebook. Ex)

Null Hypothesis:
H_0: Mean[Males] = Mean[Females]
Alternative Hypothesis:
H_a: Mean[Males]> Mean[Females] or Mean[Males] < Mean[Females]
Significance: alpha = 0.05

Perhaps narrowing down to a more specific subset would make the question more interesting.
 
It may be good to add in the time frame you are measuring to not inaccurately generalize over historical and future periods. 

the data has the variables of trip duration and gender, and these two have been extracted into their own dataframe

Nowhere is the scale of ‘trip duration’ given, this must be specified

The plotting does not have X and Y labels and is therefore unclear what it is demonstrating

Suggested Test:

this question compares a categorical value (gender) with a continuous variable (time) to ask if the 2 categories have different means

One suggestion is the unpaired T test, which compares two population means, when the populations do not have any influence on each other.

The two populations you are comparing the means of are males and females
Before committing to a T test you must determine if the populations are approximately normally distributed and have approximately equal variances. 

http://www.lboro.ac.uk/media/wwwlboroacuk/content/mlsc/downloads/1.2_Unpairedttest.pdf

# FBB this should have been placed in HW3 since it is a review of a project in HW3. 
# FBB thorough review, should be helful to the author.
