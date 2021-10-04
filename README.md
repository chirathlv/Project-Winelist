# Table of Contents
1. [Introduction- Project Win(e)list](#Introduction)
2. [Data, Technology and Coding Standards](#Paragraph1)
   1. [Data Sources](#SubParagraph1)
   2. [Technology Stack](#Subparagraph2) 
   3. [Coding and Release Standards](#Subparagraph3)
3. [Data Cleanse and Visualisation](#Paragraph2)
   1. [Data Cleanse](#SubParagraph4)
   2. [Analysis- Customer Segmentation](#SubParagraph5)
   3. [Analysis- Channel Effectiveness](#Subparagraph6) 
   4. [Analysis- Campaign Effectivenes](#Subparagraph7)
   5. [Key Findings](#Subparagraph8)   
4. [Recommendations](#Paragraph3)
5. [References](#Paragraph4)

<div style="page-break-after: always;"></div>

## Introduction- Project Win(e)list <a name="Introduction"></a>

Winelist Corporation, a subsidiary of a boutique grocery chain based in US, has requested an analysis of its wine customers and sales. This analysis will serve as input into their wine sales maximisation and marketing strategy. Data visualisation tools have been used to present the findings and recommendations.

## Data, Technology and Coding Standards <a name="paragraph1"></a>
### Data Sources <a name="subparagraph1"></a>

Winelist Corporation has provided the following data:
[Winelist Corporation](https://www.kaggle.com/c/winwinewine/data)

Additionally, the American Census data has been sourced using API [American Census Data]()

### Technology Stack <a name="subparagraph2"></a>

The following technologies have been used in developing this solution:
- Python libraries and code
- Pandas libraries including Census and Geo librar ???
- hvPlot
- Plotly Express
- MapBox/API
- Panel
- Census API 
- Panel

### Coding and Release Standards <a name="subparagraph3"></a>

Following rules must be applied during code development and testing:
1. All variables must reflect their purpose. Underscore to be used as and when required. Avoid using long variable names. 
2. Each step of the code must contain comments to explain the purpose of the code and methodolgy.
3. A git hub repository called Project1 will be set up with branches for each developer.
4. Each developer must use their own git hub branch to code and unit test developed code.
5. Lead developer must review code prior to merge.
6. Lead developer is responsible for merging all code.
7. Each developer must download the most recent code from main branch before commencing code changes.
8. Each release must provide a brief message on changes made prior to committing the code.


## Data Cleanse and Visualisation <a name="paragraph3"></a>
### Data Cleanse <a name="subparagraph4"></a>

The following data cleanse rules will be applied to the source marketing data set:
1. Identified data set must be formatted correctly prior to use- Date format dd/mm/yyyy, amount must be integer.
2. Calculate age from birth year and not greater than 100 years.3. 
3. Redundant data, if any, must be dropped- drop columns Z_CostContact', 'Z_Revenue', 'Response', 'MntGoldProds'.
4. ‘Absurd’ and 'YOLO' marital status must be changed to the most frequent value for consistency.
5. Rename 2n Cycle to 'Undergraduate'.
6. Duplicates, if any must be dropped.
7. Ensure all columns have appropriate and correct headers.
8. Group records into appropriate sub categories- Age in steps of 10 years, Income in steps of $10k
9. Ensure records are sorted on the required fields.
10. Validate that entire data set has been correctly loaded.

Additionally the following data cleanse rules will be applied to tyhe Census data:
- Extract only the fields that are required.
- Extract only the top 5% population data that meets target customer criteria values/ ranges.
- Extract required data set by state/ county.
- Extract the longitude and latitude information for the identified counties.
- Drop all other information.
- Check for duplicates.

### Analysis- Customer Segmentation <a name="subparagraph5"></a>
__SCP1- Which customer segment provides the maximum sales?__
Data set analysed for age, education, marital status and income values by grouping the data set on the required category. 
Analysis: 
- Wine sales are significantly higher amongst the educated, particularly graduates.
- Wine sales to "married" and "together" customers are the largest segment of wine customers.
- Customers who buy wines are generally in the income range of $60-$80k
- It also seems that Winelist does not have customers in the higher income range of $100k and above

Below is the visual representation of the analysis:
![REQ1- Total Wine Sales per Income Bracket](https://github.com/chirathlv/Project1/blob/Renu/Images/Total%20Wine%20Sales%20per%20Income%20Bracket.png)
![REQ1- Wine consumption based on Age Groups ](https://github.com/chirathlv/Project1/blob/Renu/Images/Wine%20consumption%20based%20on%20Age%20Groups.png)
![REQ1- Wine consumption based on Marital Stats ](https://github.com/chirathlv/Project1/blob/Renu/Images/Wine%20consumption%20based%20on%20Marital%20Stats.png)
![REQ1- Total Sales based on Education per Marital Stat ](.https://github.com/chirathlv/Project1/blob/Renu/Images/Total%20Sales%20based%20on%20Education%20per%20Marital%20Stat.PNG)
![REQ1- Wine consumption based on Marital Status and Age Group ](https://github.com/chirathlv/Project1/blob/Renu/Images/Wine%20consumption%20based%20on%20Marital%20Status%20and%20Age%20Group.png)

__SCP2- Which product in the food basket best aligns with wine consumption?__
This section analyses the customer Food Basket to understand the products associated with wine purchases.

Analysis: 
Based on below, customer who buys Wine generally purchases meat.



### Analysis- Channel Effectiveness <a name="subparagraph6"></a>
__SCP3- Which channel provides the maximum sales?__
This section analyses stores sales versus web site sales based on the proportion of purchase transactions- at store and at website. 

Analysis: 
- It can be said that instore sales are higher than sales through company website





### Analysis- Campaign Effectivenes <a name="subparagraph7"></a>
__SCP4- Do deals lead to an increase in sales? Which promotion campaigns are successful?__
To determine which campaign was the most effective, the successful acceptance of the campaign offer has been mapped. In the absence of specific channel sales data, corresponding customer sales values are used to overlay a sales trend line. Additionally catalog versus deals sales are analysed based on number of successful transactions

Analysis: 
- Campaign 5 was the most effective in successfully concluding with a sale on either channel.
- Catalogs seem to be more effective in bringing in customers to stores 


### Key Findings <a name="subparagraph8"></a>
1. Older customers, particularly in the age group of 40-50 years followed by 50-60 years are the largest customer segment.
2. There is direct correlation between education and wine consumption- people who have completed basic education are not wine consumers.
3. Couples, either married or together, are the largest customer segment.
4. There is a direct correlation between income and education which also leads to the conclusion that consumers who have higher incomes are wine consumers.
5. Store sales via catalogs are the highest.
6. Observed that there are no customers whose income exceeds $100k
7. Average sales per customer is $304
8. Campaign 5 was the most effective as it had the highest acceptance.


## Recommendations <a name="paragraph4"></a>

Based on the latest US census data and the identified target customer segment of couples who are educated, it is recommended that Winelist Corporation direct their marketing dollars to the below regions to maximise their sales. Based on the findings, 

__SCP5- Based on customer and sales analysis overlaid with Census data, identify target markets__


## References <a name="paragraph5"></a>

1. [(https://www.kaggle.com/)]
