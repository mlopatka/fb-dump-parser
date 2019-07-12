# fb-dump-parser
[WIP] A parser for Facebook's personal informaton dump HTML format.
Part of The [DMI summer school 2019](https://summerschool.uva.nl/content/summer-courses/digital-methods-summer-school/digital-methods-summer-school.html?1562660345370) 

## Current functionality 
* unpacks the zip file provdided when a user requests a downloads of their facebook information.
* traverses the dirrectory organized as per Facebook's data download schema.
* calculates the file size for each top level directory (data category) as a metric of the quantity of information pertaining to a facebook profile.
