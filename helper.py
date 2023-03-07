def objectToFloat(dataframe, column_name):
    dataframe[column_name] = dataframe[column_name].str.replace(".", "")
    dataframe[column_name] = dataframe[column_name].str.replace(",", ".")
    return dataframe[column_name]