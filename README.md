Project aims are to use Zillow data on single unit/single family properties with transaction dates in 2017 to discover the drivers of errors in Zillow Zestimates. We will first clean up the data then explore it to see what features to use for clustering. Features and clusters were also checked for significance using hypothesis testing with pearsonr test.

Goals:
Make a notebook with models to focus on drivers of logerror.
Use clustering to make new features for models.

Plan - Make new repo, make appropriate SQL query.
Acquire - Acquire(df), put into CSV file
Prepare - Go over data, identifying any missing values, make Wrangle_Zillow that renames columns, handling missing values, change data types. Split data into train, validate and test.
Explore - Visualized relationships of variables, develope hypotheses and ran statistical tests, scales data using MinMax.
Model - Made baseline, modeled train and validate on regession , ran test on final model.
Deliver - Document all code in a reproducible Jupyter notebook.


To Reproducing Findings: 

- Make env.py file that contains the host, username and password for the mySQL database and go into the Zillow table. Store that env file in the same repository. Clone my repository along with the acquire_zillow.py and prepare_zillow.py. Make sure .gitignore is hiding your env.py. You should be able to run Logerror report.


Data Dictionary:
|----------|:-----:|-----:|
|Attribute | Value | Dtype|
|Age | Number of years from original construction until the home sold in 2017. | Float|
|Bathrooms | Number of bathrooms in home | Float|
|Bedrooms | Number of bedrooms | Float|
|Finished Sqft | Calculated total finished living area of the home | Float|
|Cola | Where properties are located | Int|
|Fips | Federal Information Processing Standard Code | Float|
|Dollar_per_sqft | How many dollars per sqft | Float|
|Latitude | Latitude of property | Float|
|Longitude | Longitude of property | Float|
|Home_value | Value of home	| Float|
|Land_tax | The 2017 total tax assessed value of the land | Float|
|Age | Number of years from original construction until the home sold in 2017.	| Float|
|Acres | Square footage of lot converted to acres | Category|
|Has_pool | If the property has a pool |Float|
|County	| What county it is in | Float|
|Logerror | the log(Zestimate) - log(SalePrice)	| Float|


