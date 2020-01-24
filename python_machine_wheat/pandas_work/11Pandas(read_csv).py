#food_info.csv:
#https://github.com/ustutz/Dataquest/blob/master/Data_Analyst/Step_2_Intermediate_Python_and_Pandas/2_Data_Analysis_with_Pandas_Intermediate/3_Introduction_to_Pandas/food_info.csv

#安裝python -m pip install --upgrade pandas
import pandas

#------------------------------------#
food_info = pandas.read_csv("food_info.csv")  #傳入數據
#print(type(food_info)) #pandas.core.frame.DataFrame 核心結構就是dataframe
#print(food_info.dtypes)  #包含幾種類型結構
#print(help(pandas.read_csv))
print(food_info.head())    #把剛剛讀出來的數據顯示出來  food_info.head(3) 則為頭幾行前三個數據
#print(food_info.tail(4))    #尾四行
#print(food_info.columns)    #每個列的指標
#print(food_info.shape)   #(8790, 48) 8000多個樣本 每個有48個列
#-----------------------------------------#


















