def data_report(dataframe):
    
    # create numerical data report using built in describe() method
    data_report = dataframe.describe().T
    
    # add a percent missing column
    data_report['% missing'] = dataframe.apply(lambda x: x.isna().mean())
    
    # add a cardinality column
    data_report['cardinality'] = dataframe.apply(lambda x: x.nunique())
    
    # add a skew column
    data_report['skew'] = dataframe.apply(lambda x: x.skew())

    # add a kurtosis column 
    # data_report['kurtosis'] = dataframe.apply(lambda x: x.kurtosis())
    
    # rearrange the columns 
    cols = ['count','% missing','cardinality','mean','std','min','25%','50%','75%','max','skew'
    data_report = data_report[cols]
    
    return data_report