import pandas as pd
import scipy.stats as st
import math
data = pd.read_csv("sample10000.csv")
data.count()
data['payment_type'].value_counts()
0.3543-st.norm.ppf(.995)*math.sqrt(0.3543*(1-0.3543))/math.sqrt(10000)
data['trip_distance'].mean()
data['trip_distance'].std()/100
data['trip_distance'].mean()+st.norm.ppf(.975)*data['trip_distance'].std()/100