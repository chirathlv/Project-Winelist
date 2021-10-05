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

Winelist Corporation, a subsidiary of a boutique grocery chain based in US, has requested an analysis of its wine customers and sales. This analysis will serve as input into their wine sales maximisation and marketing spend strategy. Data visualisation tools have been used to present the findings and recommendations.

## Data, Technology and Coding Standards <a name="paragraph1"></a>

### Data Sources <a name="subparagraph1"></a>

Winelist Corporation has provided the following data:
[Winelist Corporation](https://www.kaggle.com/c/winwinewine/data)

Additionally, the American Census data has been sourced using API [American Census Data](https://api.census.gov/data/2019)

### Technology Stack <a name="subparagraph2"></a>

The following technologies have been deployed:

- python 3.8.3
- pandas 1.0.5
- numpy 1.18.5
- python-dotenv 0.19.0
- requests 2.24.0
- json 2.0.9
- panel 0.9.7
- plotly 5.3.1
- hvplot 0.7.3
- matplotlib 3.2.2
- jupyter lab 2.1.5
- geopy 2.2.0: https://pypi.org/project/geopy/
- Census API Key: https://api.census.gov/data/key_signup.html
- Map Box API key: https://docs.mapbox.com/help/getting-started/access-tokens/
- Python custom helper code to load latitudes/longitudes (geocdes.py): Included in this Repo

### Coding and Release Standards <a name="subparagraph3"></a>

Following rules have been applied during code development and testing:

1. All variables must reflect their purpose. Underscore to be used as and when required.
2. Each step of the code must contain comments to explain the purpose of the code.
3. A git hub repository called Project1 must be set up with branches for each developer.
4. Each developer must use their own git hub branch to code and unit test developed code.
5. Lead developer must review code prior to merge.
6. Lead developer is responsible for merging all code.
7. Each developer must download the most recent code from main branch before commencing code changes.
8. Each release must provide a brief message on changes made prior to committing the code.

## Data Cleanse and Visualisation <a name="paragraph2"></a>

### Data Cleanse <a name="subparagraph4"></a>

The following data cleanse rules have been applied to the source marketing data set:

1. Identified data set must be formatted correctly prior to use- Date format yyyy/mm/dd, amount must be integer.
2. Calculate age from birth year.
3. Redundant data, if any, must be dropped- drop columns Z_CostContact', 'Z_Revenue', 'Response', 'MntGoldProds'.
4. ‘Absurd’ and 'YOLO' marital status must be changed to the most frequent value for consistency.
5. Rename 2n Cycle to 'Undergraduate'.
6. Duplicates, if any must be dropped.
7. Ensure all columns have appropriate and correct headers.
8. Group records into appropriate sub categories- Age in steps of 10 years, Income in steps of $10k.
9. Ensure records are sorted on the required fields.
10. Validate that entire data set has been correctly loaded.

Additionally, the following data transformation rules have been applied to the American census data downloaded from the American Govt's Census data site.

1. Collect only data for the target customer segment and their location.
2. Identify the state and county correctly.
3. Rename headers with correct labels.
4. Convert numeric values from strings to numbers.

### Analysis- Customer Segmentation <a name="subparagraph5"></a>

**SCP1- Which customer segment provides the maximum sales?**
Data set analysed for age, education, marital status and income values by grouping the data set on the required category.
Analysis:

- Wine sales are significantly higher amongst the educated, particularly graduates.
- Wine sales to "married" and "together" customers are the largest segment of wine customers.
- Customers who buy wines are generally in the income range of $60-$80k.
- It also seems that Winelist does not have customers in the higher income range of $100k and above.

Below is the visual representation of the analysis:
![Total Wine Sales per Income Bracket](https://github.com/chirathlv/Project1/blob/main/Images/Total%20Wine%20Sales%20per%20Income%20Bracket.png)
![Wine Customers based on Age Groups](https://github.com/chirathlv/Project1/blob/main/Images/Wine%20consumption%20based%20on%20age%20groups.png)
![Wine Sales based on Marital Status](https://github.com/chirathlv/Project1/blob/main/Images/Wine%20sales%20based%20on%20marital%20status.png)
![Total Sales based on Education per Marital Status](https://github.com/chirathlv/Project1/blob/main/Images/Wine%20sales%20based%20on%20education%20and%20mstatus.png)
![Wine consumption based on Marital Status and Age Group](https://github.com/chirathlv/Project1/blob/main/Images/Wine%20sales%20based%20on%20marital%20status%20and%20age%20group.png)

**SCP2- Which product in the food basket best aligns with wine consumption?**
This section analyses the customer Food Basket to understand the products associated with wine purchases.

Analysis:
Based on below, customer who buys Wine generally purchases meat. Thsi association maybe used to develop product tie in campaigns.

![Food Basket Comparison](https://github.com/chirathlv/Project1/blob/main/Images/Food%20basket%20comparison.png)

### Analysis- Channel Effectiveness <a name="subparagraph6"></a>

**SCP3- Which channel provides the maximum sales?**
This section analyses stores sales versus web site sales based on the proportion of purchase transactions- at store and at website.

Analysis:

- It can be said that instore sales are higher than sales through company website. Note that the data set is pre Covid 19.

![Website versus Instore sales](https://github.com/chirathlv/Project1/blob/main/Images/Channel%20performance%20stores%20versus%20website.png)

### Analysis- Campaign Effectivenes <a name="subparagraph7"></a>

**SCP4- Do deals lead to an increase in sales? Which promotion campaigns are successful?**
To determine which campaign was the most effective, the successful acceptance of the campaign offer has been mapped. In the absence of specific channel sales data, corresponding customer sales values are used to overlay a sales trend line. Additionally catalog versus deals sales are analysed based on number of successful transactions.

Analysis:

- Campaign 5 was the most effective in successfully concluding with a sale on either channel.
- Catalogs seem to be more effective in bringing in customers to stores

![Effectiveness- Marketing campaigns](https://github.com/chirathlv/Project1/blob/main/Images/Total%20Sales%20generated%20for%20past%20Marketing%20Campaigns.png)

![Comparison- Deals versus Catalogs](https://github.com/chirathlv/Project1/blob/main/Images/Channel%20Performance%20-%20Deals%20vs%20Catalogs.png)

### Key Findings <a name="subparagraph8"></a>

1. Older customers, particularly in the age group of 40-50 years followed by 50-60 years are the largest customer segment.
2. There is direct correlation between education and wine consumption- people who have completed basic education are not wine consumers.
3. Couples, either married or together, are the largest customer segment.
4. There is a direct correlation between income and education which also leads to the conclusion that consumers who have higher incomes are wine consumers.Though in the data set provided, there are no customers with incomes of above $100k. Potentially a missing market segment.
5. Store sales via catalogs are the highest. Note that the data set is pre covid 19. Since catalogs do better, either deals are not capturing interest or the cxustomer is price insensitive.
6. Campaign 5 was the most effective as it had the highest acceptance. It appears that campaign 3 onwards, the sales trend is in the correct direction i.e. upwards.

## Recommendations <a name="paragraph3"></a>

Based on the latest US census data and the identified target customer segment of couples who are educated, it is recommended that Winelist Corporation direct their marketing dollars to the target counties depicted to maximise their sales.

Since campaign 5 appears to be the most effective, the company should use this to increase sales by directing some of gthe deals marketing dollars to this campaign.

**SCP5- Based on customer and sales analysis overlaid with Census data, identify target markets**

![Top Wine States](https://github.com/chirathlv/Project1/blob/main/Images/Top%20wine%20states.png)

![Top Wine Counties](https://github.com/chirathlv/Project1/blob/main/Images/Top%20wine%20counties.png)

## References <a name="paragraph4"></a>

1. [(https://www.kaggle.com/)]
