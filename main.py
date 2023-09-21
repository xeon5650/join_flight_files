import pandas as pd


def join_files(df1, df2, how, key):
    different_fc_and_batt = df2.columns.difference(df1.columns).tolist()
    different_fc_and_batt.append(key)
    df2 = df2[different_fc_and_batt]
    return df1.merge(df2, how=how, on=key)


fc = pd.read_csv('8/10_05_23__11_53__Cabin FC__139-FTS.csv')
batt = pd.read_csv('8/10_05_23__11_53__Cabin Batt__139-FTS.csv')
pilot = pd.read_csv('8/10_05_23__11_53__Pilot__139-FTS.csv')


all_flight = join_files(batt, fc,how='outer', key=':Time')
all_flight = join_files(all_flight, pilot, how='outer', key=':Time')
all_flight = all_flight.fillna(0)
print(all_flight.info())

batt.to_csv('Flight_9.csv', index=False)
