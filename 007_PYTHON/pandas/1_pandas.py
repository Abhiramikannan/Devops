#used lot in ML
#manipulation lang
#set-ExecutionPolicy Unrestricted
#to avoid conflict we are using virtual envt
#.\pandas\Scripts\activate=activate virtual envt,pip list(show packages)
#deactivate
#start virtual envt:python -m venv pandas
#DataFrame: works like a table 
# (similar to an SQL table, Excel spreadsheet, or dictionary of Series objects). 
import pandas as pd
data={ 'name':['abhi','vilas','akash'],'subject':['python','java','sql'],'marks':[60,70,80]}
date_list = ['2025-02-01', '2025-02-02', '2025-02-03', '2025-02-04']
# Convert to a DatetimeIndex (Pandas handles conversion)
# dates = pd.to_datetime(date_list)
# # Creating a DataFrame with datetime index
# datass = {'temperature': [22, 23, 21, 19]}
# df = pd.DataFrame(datass, index=dates)
# df=pd.DataFrame(datass)
df = pd.DataFrame(data)
print(df)

for index,row in df.iterrows():
    #print(f'{index} {row}')
      #to see only names
      print(f'{index}')
      print(f'{row['name']}')
   
