# PUI2016 HW 4.

## Assignemnt 1: review
No collaborators.

## Assignment 2: Literature choices of statistical tests

|Statistical Analyses | IV(s) | IV Type(s) | DV(s) | DV Type(s)| Control Var | Control Var Type | Question to be Answered | H0 | alpha | Link |
|-----------------------|-------|------------|-------|-----------|-------------|------------------|-------------------------|----|-------|--------|
|Logistic Regression | Gender, Smoking| Categorical | Current Rhinitis | Dichotomous | Not Applicatble to Logistic Regression | N.A. | Do gender and smoking have an impact on rhinitis infection? | there is no correlation between current rhinitis, gender, and smoking | 0.05 | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0094731#pone-0094731-t006|
|Path Analysis|1: Maternal death|Categorical: 0 or 1 (yes or no, mother died)|2: Annual Income, Expenditure per capita|Both Continuous|Control for mother's age, baseline income, baseline expenditure (source: fig. 4)|Age: ordinal. Baselines: continuous.|Does maternal death increase poverty? (source: conclusion)|Maternal death has no or positive increase on income and expenditure over a 12-month timespan.|10%, 5%, and 1% examined (see fig. 5), but nothing set in advance|[link](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134756)|
| ANOVA  | 1,State(meditation or rest) 2,Valence(negative, neutral, or positive) 3,Group(novices or experts)     | categorical | clusters extracted from ROIs | continuous | NA | NA | whether the brain activities levels are different signficantly across the State, Valence and Group | the brain activities level (the clusters volumes) are the same with varying State, Valence, and Group | alpha = 0.05| http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0001897|


## FBB Logistic regression: I think the regression is never for IV geneder and smoking alone, but always for all other relevant variables with adjustment for gender and current smoking (I think separately for one and the other)

## FBB good altogether

Collaborators [with who did what]:
- Christian (clm633) [Path Analysis]
- Te Du (td928) [ANOVA]
- Ian Xiao (ixx200) [Logistic Regression]

## Assignment 3: 
I collaborated with Prince Abunku to discuss the chi-squared tests. He showed me the scipy chisquared test function, which I tried as an alternative.

## Assignment 4:
I worked with Prince Abunku, Jack Lundquist, Sarah Schoengold, mostly discussing specific interpretations of the corrleation tests (which still confuses me). 

Note: I also shared out the snippet for the spatial join in part 4 to get borough information to the group at large, so I'm not sure who used that. 
