# Data_Crunching_assignment

## In this assignment I have to perform data crunching on files having 32 milion records of user data.<br>

--> My approach is simple, I am reading 3 of very large files in small chunks of data-frames with `pandas` library.<br>
--> After reading whole file in `chunks` are concatenated in one data-frame and all merge process begins.<br>
--> In merging process I am using left outer join in order to save memory and reducing the redundant data.<br>
--> My merging process is in two steps, first merge user-details with plain passwords and then merging new data-frame with IPs.<br>
--> My next was to create the output `.tsv` file using `to_csv()` method of pandas library.<br>
--> I used <b>left outer join</b> due to which my code ran smoothly and perfect output file generated.
<br>

### Latest update

--> I have made some minor changes to the implementation approach:<br>
--> I am now using the `nrows` argument of the Pandas data frame to load only a specified number of rows, instead of loading the whole 32 million rows in chunks and     then concatenating them.<br>
--> This has significantly reduced the memory usage of the code execution.<br>
--> Another change is that I am now setting the `dtype` (declaring the data type of columns) argument before reading the entire file, instead of dynamically checking for data type. This has been a game changer for memory utilization.<br>
