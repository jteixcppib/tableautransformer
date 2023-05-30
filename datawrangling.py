# This module has more granulated functions which aid in the manipulation of data
from datetime import date
import pandas as pd
import numpy as np
from pyparsing import col

def basic_table(read_path, read_type='csv', sheet_name=None, columns_to_keep='all', columns_rename=None, 
                filters=None, group_by=None, aggregate_columns=None, pre_agg_math_columns=None, 
                post_agg_math_columns=None, remove_NAN=True, remove_NAN_col='all'):
    
    # reading in basics
    if read_type == 'csv':
        df_basic_table = pd.read_csv(read_path)
    elif read_type == 'excel':
        df_basic_table = pd.read_excel(read_path, sheet_name=sheet_name)
    else:
        print('read_type must be either "csv" or "excel"')
    
    # columns
    if columns_to_keep != 'all':
        df_basic_table = df_basic_table[columns_to_keep]
    if columns_rename is not None:
        df_basic_table.columns = columns_rename

    # remove nan
    if remove_NAN:
        if remove_NAN_col == 'all':
            df_basic_table = df_basic_table[df_basic_table.notna()]
        else:
            for col in remove_NAN_col:
                df_basic_table = df_basic_table[df_basic_table[col].notna()]

    if pre_agg_math_columns is not None:
        for new_column_name, math_expression in pre_agg_math_columns.items():
            df_basic_table[new_column_name] = df_basic_table.eval(math_expression)
    
    if filters is not None: ## need to add in a isin filter ability within this functionality or create a new argument for it
        for column, operator, value in filters:
            if operator == "==":
                df_basic_table = df_basic_table[df_basic_table[column] == value]
            elif operator == "!=":
                df_basic_table = df_basic_table[df_basic_table[column] != value]
            elif operator == ">":
                df_basic_table = df_basic_table[df_basic_table[column] > value]
            elif operator == ">=":
                df_basic_table = df_basic_table[df_basic_table[column] >= value]
            elif operator == "<":
                df_basic_table = df_basic_table[df_basic_table[column] < value]
            elif operator == "<=":
                df_basic_table = df_basic_table[df_basic_table[column] <= value]
    if group_by and aggregate_columns is not None:
        df_basic_table = df_basic_table.groupby(group_by).aggregate(aggregate_columns).reset_index()

    if post_agg_math_columns is not None:
        for new_column_name, math_expression in post_agg_math_columns.items():
            df_basic_table[new_column_name] = df_basic_table.eval(math_expression)
    return df_basic_table

def find_dtypes(df):
    for col in df.columns:
        datatypes = set(df[col].dtype for i in df[col])
        print(f'{col}: {list(datatypes)}')

def find_dups(df, name):
    duplicated = df.duplicated(subset=df.columns)
    print('-----------------------------------------------')
    print(f"Your duplicated inside {name} are:")
    print(df[duplicated])
    print('-----------------------------------------------')

def force_string(df):
    for col in df.columns:
        df[col] = df[col].astype(str)
        df[col] = df[col].replace(0,'')

def force_object(df):
    for col in df.columns:
        df[col] = df[col].astype(object)

def is_in(df, target_col, isin_list):
    df = df[df[target_col].isin(isin_list)]
    return df

def cast(df, target_col, value):
    df[target_col] = value
    return df

def export(file_name, tables):
    with pd.ExcelWriter(file_name) as writer:
        for key in tables.keys():
            tab_name = key
            tab_df = tables[key]
            tab_df.to_excel(writer, sheet_name=tab_name, index=False)
    return print(f"Data written too {file_name}")

def create_row(): # might not be needed, if so it will be a create row with filter and col_ops
    pass

def bucket(df, column, bucket_col_name, intervals): # need to add in operand for both lower and upper bounds
    interval_values = []
    for value in df[column]:
        interval = 'other'
        for interval_name, interval_range in intervals.items():
            if interval_range[0] <= value <= interval_range[1]:
                interval = interval_name
                break
        interval_values.append(interval)

    df[bucket_col_name] = interval_values
    return df

def date_format(df, target_col, date_format):
    df[target_col] = pd.to_datetime(df[target_col])
    df[target_col] = df[target_col].dt.strftime(date_format)
    return df

