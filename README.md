# TableauTransformer
*ETL tooling for preparing tableau seed data*
***

## Description

This library was built with the intentions of enhancing the experience of data wrangling for tableau.
Tableau can be very particular about the data it reads from.
In addition preparing data to fit the shape for different graphs can be time consuming.
TableauTransformer can be used to hurdle over these two barriers.

Github Repo https://github.com/jteixcppib/tableautransformer

## Dependencies

* pip, python 3.6, pandas, numpy

## Getting Started

```
pip install tableautransformer
```

```
import tableautransformer.datawrangling as tbt
```

tbt is a collection of functions, not a collection of methods, so all calls are "tbt.function_name()"

## Function Docs
Here you can find a list of all functions within the library, a description of what they do, and their inputs.

### Basic_Table()

```
basic_table(read_path, read_type='csv', sheet_name=None, columns_to_keep=None, columns_rename=None, 
                filters=None, group_by=None, aggregate_columns=None, pre_agg_math_columns=None, 
                post_agg_math_columns=None, remove_NAN=True, remove_NAN_col='all')
```

##### Description

basic_table is the basis for the tbt library as it refactors ~20 lines of commonly repeated code down to one input heavy function. The function reads in a dataframe, cleans up the data, and performs commonly used table operations.

##### Inputs

> **read_path**: *string*
>> The path to the file you wish to read. The **only mandatory** input.

> **read_type**: *'csv' or 'excel'*
>> Default is *'csv'*, if type is excel then sheet_name must have a value.

> **sheet_name**: *string*
>> The name of the tab you wish to read in.

> **columns_to_keep**: *list of strings*
>> *['colA', 'colB', 'colC']* Default retains all columns, this function runs immediately after reading in the data, any column mentioned in the list will remain in the dataframe, all others are dropped.

> **columns_rename**: *list of strings*
>> *['colA', 'colB', 'colC']* Default does not alter the names. The renaming process occurs after the file is read in and columns_to_keep have been selected. All other column related inputs should use the new name dictated by the rename process if used.

> **filters**: *list of 3-element tuples*
>> *[('col_name', 'operand', 'value')]* The input can be multiple filters, each filter is a 3-element tuple where the first element is the column name, the second is the operand, and the third is the value. The column name and operand must be strings while the value can be numeric (or a string if the operand is '==').

> **group_by**: *list of strings*
>> *['colA', 'colB', 'colC']* groups dataframe by specified columns, aggregate_columns must not be None in order to work.

> **aggregate_columns**: *dicitonary*
>> *{'colA': 'agg_func'}* when group_by is in effect it selects which columns to perform an agg function on, example 'sum' will do np.sum.

> **pre_agg_math_columns**: *dictionary*
>> *{'new_col': 'colA + colB'}* Create a new column labeled as the key (from dictionary) and the scalar value as the value (from dictionary). Creates before group_by function is read. Caveat: columns in the value (from dictionary) must contain no spaces.

> **post_agg_math_columns**: *dictionary*
>> *{'new_col': 'colA + colB'}* Create a new column labeled as the key (from dictionary) and the scalar value as the value (from dictionary). Creates after group_by function is read. Caveat: columns in the value (from dictionary) must contain no spaces.

> **remove_NAN**: *True or False boolean* 
>> Default is *True*, removes any rows where a scalar value in the target column is NaN.

> **remove_NAN_col**: *'all' or list of stirngs*
>> *['colA', 'colB', 'colC']* (default is *'all'*), selects the targets for remove_NAN function.

***

### Bucket()

```
bucket(df, column, bucket_col_name, intervals)
```

##### Description

Creates a new column with values assigned depending on discrete intervals of another columns value.

##### Inputs

> **df**: *DataFrame*
>> The dataframe you want to bucket

> **column**: *string*
>> The column which the values are used to determine what the descrete interval is assigned

> **bucket_col_name**: *string*
>> The name of the new column which contains the discrete intervals

> **intervals**: *dictionary where value is a 2-element numeric tuple*
>> *[{'low': (10,200)}]* this would assign the bucketed discrete value of 'low' to any index's target column inbetween or equal to 20 and 200. **Caveat**: the operand is fixed to *lower_value* **<=** *col_value* **<=** *upper_value*.

***

### Export()

```
export(file_name, tables)
```

##### Description

Exports selected dataframes into an Excel file where each tab is its own dataframe.

##### Inputs

> **file_name**: *string*
>> The path you want to write the file too

> **tables**: *dictionary*
>> The key is the tab name, the value is the df

***

### Find_Dtypes()

```
find_dtypes(df)
```

##### Description

For each column in the DataFrame print the dtypes present inside the series.

##### Inputs

> **df**: *dataframe*
>> The DataFrame you want to loop through

***

### Is_In()

```
is_in(df, target_col, isin_list)
```

##### Description

Filters for only things that are inside the list.

##### Inputs

> **df**: *DataFrame*
>> The dataframe you want to filter

> **target_col**: *string* 
>> The column you want to apply the logic too for the filter.

> **isin_list**: *list*
>> The list that the target_col value must equal at least one element.

***

### Cast()

```
cast(df, target_col, value)
```

##### Description

Assign value to entire column, creates new column if column does not exist. **Caveat** do not use to cast a value which requires math

##### Inputs

> **df**: *DataFrame*
>> The dataframe you want to cast

> **target_col**: *string* 
>> The column you want to apply the logic too for the cast.

> **value**: *any primary type*
>> The scalar value for the entire column.

***

### Date_Format()

```
date_format(df, target_col, date_format)
```

##### Description

Turns a columns value into a specific pandas date_time type

##### Inputs

> **df**: *DataFrame*
>> The dataframe you want to work with

> **target_col**: *string*
>> The column you want to alter

> **date_format**: *strftime Format Code*
>>  the strftime format code which you want to represent your date. see more: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

***

## Authors

Contributors names and contact info

* Josh Teixeira  |  jteixeira@cppib.com

## Version History

* 0.0.31
    * columns_to_keep default is all, fixed columns_rename bug
* 0.0.27
    * export function added
* 0.0.26
    * date_format function fixed
* 0.0.24
    * README basic documentation complete
* 0.0.17
    * README documentation enhanced
* 0.0.16
    * bucket function added
* 0.0.1
    * Initial beta release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details