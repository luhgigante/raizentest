# raizentest

Goal
This xls file has some pivot tables like this one:

Pivot Table

The developed pipeline is meant to extract and structure the underlying data of two of these tables:

Sales of oil derivative fuels by UF and product
Sales of diesel by UF and type
The totals of the extracted data must be equal to the totals of the pivot tables.

Schema
Data should be stored in the following format:

Column	Type
year_month	date
uf	string
product	string
unit	string
volume	double
created_at	timestamp
Remember to define a convenient partitioning or indexing schema.

.

This code reads excel xml to acess the pivot caches

In Test Raizen.ipynb shows 2 ways to extract values for each data schema:

1) read xml files
2) create objects using root
3) append objects in a list
4) make a validation in the first columns
5) append values in a list
6) create dataframe 
7) result in 2 csv outputs (for each table as required)
