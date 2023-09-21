import pandas as pd


def join_files(df1, df2, how, key):
    different_cols = df2.columns.difference(df1.columns).tolist()
    different_cols.append(key)
    df2 = df2[different_cols]
    return df1.merge(df2, how=how, on=key)


fc = pd.read_csv('8/10_05_23__11_53__Cabin FC__139-FTS.csv')
batt = pd.read_csv('8/10_05_23__11_53__Cabin Batt__139-FTS.csv')
pilot = pd.read_csv('8/10_05_23__11_53__Pilot__139-FTS.csv')


all_flight = join_files(batt, fc,how='outer', key=':Time')
all_flight = join_files(all_flight, pilot, how='outer', key=':Time')
all_flight = all_flight.fillna(0)

print(all_flight.info())

all_flight.to_csv('Flight_8.csv', index=False)
