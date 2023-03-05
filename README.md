# Gross Domestic Product and Software Developers

This project provides and endpoint that receives a country's ISO code and returns its gross domestic product as well as the youngest age that developers started coding for that country.
Source:
- European Gross Domestic Product for 2021*
- Stackoverflow 2021 survey's responses*

_*Since 2022's GDP was incomplete, 2021 information was used_

## Installation
`pip install -r requirements.txt`

## Load db
`./manage.py load_db`

## Run tests
`./manage.py test`

## Run server
`./manage.py runserver`

## Endpoint example
`GET http://localhost:8000/processors/gdp_youngest_age/BE/`

----
## Project
This project was developed using Django and Django Rest Framework for
convenience when building the API and the DB tables. 

It uses a **sqlite** database for its simplicity. 

The command _load_db_ is provided to import all the information to the database.

When importing all the data, the library **pycountry** is used to get the countries' ISO code.

For convenience when querying the age when developers started to code, I parsed the string
coming from the survey to min-max ranges in the database.

----
## Part 1
In order to get the most frequent first coding age of each european country and their corresponding amount of developers
I used the following query:

`SELECT "country_name", "min_age_first_code", "max_age_first_code", max("dcount")
FROM (SELECT rs.country_name, rs.min_age_first_code, rs.max_age_first_code, count("min_age_first_code") AS "dcount"
      FROM readers_stackoverflowresponse rs
      JOIN readers_grossdomesticproduct rg ON rs.country_name = rg.country_name
      GROUP BY rs.country_name, rs.min_age_first_code)
GROUP BY "country_name";`

This returns:

| country\_name | min\_age\_first\_code | max\_age\_first\_code | max\("dcount"\) |
| :--- | :--- | :--- | :--- |
| albania | 11 | 17 | 28 |
| austria | 11 | 17 | 545 |
| belgium | 11 | 17 | 446 |
| bulgaria | 11 | 17 | 239 |
| croatia | 11 | 17 | 156 |
| cyprus | 11 | 17 | 39 |
| denmark | 11 | 17 | 374 |
| estonia | 11 | 17 | 81 |
| finland | 11 | 17 | 288 |
| france | 11 | 17 | 1597 |
| greece | 11 | 17 | 309 |
| hungary | 11 | 17 | 273 |
| iceland | 11 | 17 | 25 |
| ireland | 11 | 17 | 187 |
| italy | 11 | 17 | 1003 |
| latvia | 11 | 17 | 72 |
| lithuania | 11 | 17 | 148 |
| luxembourg | 11 | 17 | 29 |
| malta | 11 | 17 | 24 |
| montenegro | 11 | 17 | 11 |
| netherlands | 11 | 17 | 1043 |
| norway | 11 | 17 | 338 |
| poland | 11 | 17 | 1136 |
| portugal | 11 | 17 | 298 |
| romania | 11 | 17 | 461 |
| serbia | 11 | 17 | 182 |
| slovakia | 11 | 17 | 163 |
| slovenia | 11 | 17 | 151 |
| spain | 11 | 17 | 773 |
| sweden | 11 | 17 | 711 |
| switzerland | 11 | 17 | 618 |

We can see that for all european countries, the most frequent starting age for developers is between
11 and 17 years old. Since the age is not variable, we cannot define a determined relationship
between this age and the GDP of the country.

## Part 2
In order to increase the scalability of this endpoint, we could:
- Use a cache to access the data quicker and don't affect the performance, since this information is loaded once a year, 
and it won't change with the passage of time.
- If the amount of survey responses increased, an index could be used to enhance the speed of the query.

## Part 3
Since sqlite has no pivot query, I used two queries to show the data.

In order to show the three most popular programming languages, I used this subquery:

`SELECT "name"
FROM readers_programminglanguageresponse
GROUP BY "name"
ORDER BY count("name") DESC
LIMIT 3;`

This returns Javascript, HTML/CSS, Python.

To build the query that gives us information about how many developers use these programming
languages in each country, I used the following query:

`SELECT rs.country_name,
SUM(CASE
  WHEN rp.name like "%Javascript%" THEN 1 ELSE 0 END) AS "Javascript",
SUM(CASE
  WHEN rp.name like "%HTML/CSS%" THEN 1 ELSE 0 END) AS "HTML/CSS",
SUM(CASE
  WHEN rp.name like "%Python%" THEN 1 ELSE 0 END) AS "Python"
FROM readers_stackoverflowresponse rs
JOIN readers_programminglanguageresponse rp on rs.id = rp.survey_response_id
GROUP BY country_name;`

This returns:

| country\_name | Javascript | HTML/CSS | Python |
| :--- | :--- | :--- | :--- |
| afghanistan | 31 | 27 | 19 |
| albania | 50 | 43 | 30 |
| algeria | 29 | 26 | 19 |
| andorra | 7 | 5 | 3 |
| angola | 14 | 14 | 5 |
| argentina | 415 | 339 | 246 |
| armenia | 57 | 33 | 33 |
| australia | 1107 | 925 | 830 |
| austria | 498 | 438 | 377 |
| azerbaijan | 38 | 33 | 33 |
| bahamas | 3 | 1 | 5 |
| bahrain | 22 | 19 | 14 |
| bangladesh | 503 | 439 | 322 |
| barbados | 8 | 7 | 4 |
| belarus | 95 | 66 | 46 |
| belgium | 467 | 400 | 333 |
| belize | 2 | 3 | 3 |
| benin | 10 | 9 | 4 |
| bhutan | 4 | 3 | 3 |
| bosnia and herzegovina | 106 | 94 | 47 |
| botswana | 4 | 3 | 2 |
| brazil | 1531 | 1218 | 950 |
| brunei darussalam | 1 | 1 | 1 |
| bulgaria | 260 | 210 | 117 |
| burkina faso | 3 | 3 | 3 |
| burundi | 5 | 5 | 4 |
| cambodia | 17 | 16 | 10 |
| cameroon | 27 | 30 | 16 |
| canada | 1978 | 1686 | 1590 |
| central african republic | 2 | 2 | 1 |
| chad | 2 | 2 | 1 |
| chile | 151 | 119 | 123 |
| china | 424 | 327 | 490 |
| colombia | 278 | 242 | 176 |
| costa rica | 59 | 47 | 30 |
| croatia | 156 | 141 | 109 |
| cuba | 26 | 26 | 22 |
| cyprus | 36 | 27 | 26 |
| côte d'ivoire | 15 | 13 | 6 |
| denmark | 366 | 317 | 273 |
| djibouti | 2 | 2 | 1 |
| dominica | 1 | 1 | 1 |
| dominican republic | 84 | 71 | 29 |
| ecuador | 81 | 60 | 49 |
| egypt | 322 | 306 | 218 |
| el salvador | 26 | 20 | 10 |
| estonia | 76 | 71 | 61 |
| ethiopia | 46 | 43 | 30 |
| fiji | 1 | 2 | 1 |
| finland | 351 | 273 | 247 |
| france | 1802 | 1592 | 1422 |
| gambia | 1 | 1 | 0 |
| georgia | 100 | 82 | 59 |
| germany | 3387 | 3027 | 2711 |
| ghana | 62 | 59 | 38 |
| greece | 360 | 330 | 295 |
| guatemala | 52 | 42 | 26 |
| guinea | 2 | 2 | 1 |
| guyana | 5 | 4 | 4 |
| haiti | 4 | 3 | 3 |
| honduras | 19 | 18 | 10 |
| hungary | 298 | 270 | 209 |
| iceland | 27 | 17 | 27 |
| india | 6448 | 5833 | 5223 |
| indonesia | 452 | 385 | 256 |
| iraq | 47 | 49 | 27 |
| ireland | 234 | 203 | 193 |
| isle of man | 5 | 5 | 3 |
| israel | 521 | 390 | 514 |
| italy | 1095 | 959 | 734 |
| jamaica | 16 | 17 | 10 |
| japan | 267 | 210 | 209 |
| jordan | 43 | 34 | 22 |
| kazakhstan | 39 | 41 | 30 |
| kenya | 181 | 171 | 132 |
| kuwait | 18 | 18 | 12 |
| kyrgyzstan | 12 | 8 | 4 |
| lao people's democratic republic | 4 | 3 | 1 |
| latvia | 71 | 58 | 38 |
| lebanon | 79 | 78 | 48 |
| lesotho | 2 | 3 | 0 |
| liberia | 2 | 2 | 2 |
| liechtenstein | 0 | 0 | 1 |
| lithuania | 140 | 120 | 59 |
| luxembourg | 38 | 30 | 26 |
| madagascar | 14 | 13 | 7 |
| malawi | 9 | 8 | 4 |
| malaysia | 220 | 202 | 148 |
| maldives | 12 | 10 | 9 |
| mali | 1 | 1 | 0 |
| malta | 29 | 22 | 17 |
| mauritania | 4 | 4 | 2 |
| mauritius | 24 | 21 | 17 |
| mexico | 531 | 456 | 285 |
| monaco | 1 | 1 | 0 |
| mongolia | 17 | 11 | 10 |
| montenegro | 13 | 13 | 4 |
| morocco | 153 | 160 | 95 |
| mozambique | 9 | 8 | 3 |
| myanmar | 35 | 29 | 15 |
| namibia | 10 | 9 | 9 |
| nepal | 245 | 208 | 178 |
| netherlands | 1182 | 1020 | 831 |
| new zealand | 361 | 299 | 230 |
| nicaragua | 12 | 10 | 4 |
| niger | 2 | 2 | 1 |
| nigeria | 316 | 292 | 172 |
| norway | 367 | 313 | 257 |
| oman | 14 | 11 | 11 |
| pakistan | 572 | 543 | 323 |
| panama | 25 | 21 | 11 |
| papua new guinea | 0 | 0 | 0 |
| paraguay | 34 | 24 | 17 |
| peru | 105 | 92 | 72 |
| philippines | 280 | 247 | 155 |
| poland | 1078 | 901 | 812 |
| portugal | 363 | 301 | 219 |
| qatar | 18 | 24 | 20 |
| romania | 426 | 351 | 263 |
| russian federation | 787 | 623 | 664 |
| rwanda | 25 | 23 | 14 |
| saint kitts and nevis | 1 | 0 | 0 |
| saint lucia | 1 | 1 | 2 |
| saint vincent and the grenadines | 0 | 0 | 0 |
| san marino | 2 | 1 | 0 |
| saudi arabia | 95 | 87 | 63 |
| senegal | 26 | 24 | 16 |
| serbia | 208 | 184 | 109 |
| sierra leone | 1 | 1 | 2 |
| singapore | 226 | 177 | 203 |
| slovakia | 160 | 145 | 119 |
| slovenia | 165 | 135 | 122 |
| somalia | 4 | 4 | 3 |
| south africa | 387 | 353 | 247 |
| spain | 958 | 809 | 675 |
| sri lanka | 301 | 269 | 189 |
| sudan | 16 | 19 | 12 |
| suriname | 3 | 3 | 2 |
| sweden | 729 | 597 | 523 |
| switzerland | 580 | 530 | 469 |
| syrian arab republic | 37 | 36 | 15 |
| tajikistan | 5 | 7 | 2 |
| thailand | 116 | 106 | 86 |
| togo | 7 | 7 | 3 |
| trinidad and tobago | 13 | 14 | 8 |
| tunisia | 120 | 113 | 79 |
| turkey | 681 | 570 | 462 |
| turkmenistan | 8 | 9 | 4 |
| tuvalu | 1 | 1 | 1 |
| uganda | 49 | 41 | 33 |
| ukraine | 450 | 337 | 271 |
| united arab emirates | 124 | 120 | 80 |
| uruguay | 109 | 88 | 56 |
| uzbekistan | 33 | 29 | 31 |
| viet nam | 244 | 198 | 172 |
| yemen | 8 | 11 | 6 |
| zambia | 16 | 17 | 12 |
| zimbabwe | 22 | 20 | 17 |
