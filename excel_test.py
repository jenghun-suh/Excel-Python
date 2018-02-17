import pandas as pd
import numpy as np

from glob import glob


read_fcns = {
    'csv': pd.read_csv,
    'xlsx': pd.read_excel,
}


def get_data(fnames, file_format):

    read_fcn = read_fcns[file_format]

    dfs = []
    for fname in fnames:
        df = read_fcn(fname)
        dfs += [df]

    return dfs


def sample_function(df):
    return np.power(2, df['id']) + df['weight']


def main():
    # get csv file names (you can customize this list)
    csv_fnames = glob('*.csv')
    csv_dfs = get_data(csv_fnames, 'csv')

    out_list = []
    key_of_interest = ['name', 'out']
    for csv_df in csv_dfs:
        print csv_df
        csv_df['out'] = csv_df.apply(sample_function, axis=1)
        print csv_df
        print "sum of out column = {}".format(csv_df['out'].sum())
        print
        out_list += [csv_df[key_of_interest]]
    out_df = pd.concat(out_list)
    print out_df

    # get xlsx file names (you can customize this list)
    xlsx_fnames = glob('*.xlsx')
    xlsx_dfs = get_data(xlsx_fnames, 'xlsx')


if __name__ == "__main__":
    main()
