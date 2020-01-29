import pandas

food_info = pandas.read_csv("food_info.csv")  #傳入數據
## -----------------------------------------#
## dataframe的類型
## object - for string values
## int - for integer values
## float - for float values
## datetime - for time values
## bool - for boolean values
## print(food_info.dtypes)  

# print(food_info.loc[0])  #提取第一個數據
# print(food_info.loc[3:6])  #提取屬據3~6
#提取列名的數據
# ndb_col = food_info["NDB_No"]
# print(ndb_col)
##or
# col_name = "NDB_No"
# ndb_col = food_info[col_name]
# print(ndb_col)

# #定義兩個列提取
# col_name = ["Zinc_(mg)","Copper_(mg)"]
# zinc_copper =food_info[col_name]
# print(zinc_copper)
# #-----------------------------------------#
##找尋以g為結尾的
# col_names = food_info.columns.tolist()   #當前列名變成list
# # print(col_names)
# gram_columns =[]

# for c in col_names:
#     if c.endswith("(g)"):   #Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
#         gram_columns.append(c)
# gram_df = food_info[gram_columns]
# print(gram_df.head(3))  #顯示頭開始3個數值

# #-----------------------------------------#
# #對數據做處理mg轉為g的作法
# print(food_info["Iron_(mg)"])
# div_1000 = food_info["Iron_(mg)"] / 1000
# print(div_1000)

# # #-----------------------------------------#
# #對應位置，每列新增一個列
# water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"] #維度一樣對應位置互乘
# iron_grams = food_info["Iron_(mg)"] / 1000
# print(food_info.shape)
# food_info["Iron_(g)"] = iron_grams
# print(food_info.shape)
# # #-----------------------------------------#
# #最大值 與特徵標準化
# #https://ithelp.ithome.com.tw/articles/10197357
# max_calories = food_info["Energ_Kcal"].max()  #902
# # print(max_calories)
# normalized_calories = food_info["Energ_Kcal"] / max_calories  #除與最大值
# normalized_protein = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()   #特徵標準化
# normalized_fat = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
# food_info["Normalized_Protein"] = normalized_protein
# food_info["Normalized_Fat"] = normalized_fat
# print(food_info["Normalized_Fat"])

# #-----------------------------------------#
# #排序
# #升序
# food_info.sort_values(["Sodium_(mg)"],inplace=True)  ##按任一軸從小到大的值排序 # 如果為True，則就地執行操作False就多一個列
# print(food_info["Sodium_(mg)"])  #NaN是缺失值
# #降序
# food_info.sort_values(["Sodium_(mg)"],inplace=True,ascending=False) #ascending上升的相反就是下降由大到小
# print(food_info["Sodium_(mg)"]) 


#-----------------------------------------#








