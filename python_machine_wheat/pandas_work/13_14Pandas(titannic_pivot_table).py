#titanic_train.csv 
# https://github.com/ogrisel/parallel_ml_tutorial/blob/master/notebooks/titanic_train.csv
#名詞解釋:https://chtseng.wordpress.com/2017/12/24/kaggle-titanic%E5%80%96%E5%AD%98%E9%A0%90%E6%B8%AC-1/
import pandas as  pd
import numpy as np 
titanic_survival = pd.read_csv("titanic_train.csv")
#print(titanic_survival)

# -----------------------------------------#
age = titanic_survival["Age"]
#print(age.loc[0:10]) 
age_is_null = pd.isnull(age) #看是不是缺失值是的話返回True
#print(age_is_null)
age_null_true = age[age_is_null]  #要看缺失值在那些位置
#print(age_null_true)
age_null_count = len(age_null_true) #看缺失值的總數
#print(age_null_count)

# # -----------------------------------------#
# #算看看平均年齡
# mean_age = sum(titanic_survival["Age"]) / len(titanic_survival["Age"])
# print(mean_age)
# #nan無法顯示，因為有NaN空的數值
 
# # -----------------------------------------#
# good_ages = titanic_survival["Age"][age_is_null == False]  #不帶缺失值的值
# correct_mean_age = sum(good_ages) / len(good_ages)
# print(correct_mean_age)

# # -----------------------------------------#
# #也可以使用mean求均值
# correct_mean_age = titanic_survival["Age"].mean()   #不推薦  因為其實可以把缺失值補起來用中位數 或是均值等
# print(correct_mean_age)
# # # -----------------------------------------#
# passenger_classes = [1,2,3]
# fares_by_class ={}
# for this_class in passenger_classes:
#     pclass_rows = titanic_survival[titanic_survival['Pclass'] == this_class]  #只提取等級上的數值
#     pclass_fares = pclass_rows["Fare"]  #提取pclass_rows上的Fare價格
#     fare_for_class = pclass_fares.mean()  #取平均值
#     fares_by_class[this_class]=fare_for_class
# print(fares_by_class)

# # -----------------------------------------#
# #pivot_table:https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html
# #對於不同的艙等的平均存活率
# passenger_survival = titanic_survival.pivot_table(index='Pclass',values="Survived",aggfunc=np.mean)
# print(passenger_survival)


# # -----------------------------------------#
# #對於不同的艙等的平均年紀
# passenger_age = titanic_survival.pivot_table(index='Pclass',values="Age",aggfunc=np.mean)
# print(passenger_age)

# # -----------------------------------------#
# #對於不同港口的船票價格跟存活量的比較
# port_stats = titanic_survival.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=np.sum)
# print(port_stats)

## -----------------------------------------#
# #dropna : https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
# #dropna 丟掉缺失值
# #drop_na_columns = titanic_survival.dropna(axis=1)
# new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age","Sex"])
# print(new_titanic_survival)

# # -----------------------------------------#
#查詢值
row_index_83_age = titanic_survival.loc[83,"Age"]
row_index_1000_pclass = titanic_survival.loc[776,"Pclass"]
print(row_index_83_age)
print(row_index_1000_pclass)




