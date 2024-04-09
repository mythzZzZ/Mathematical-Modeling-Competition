文件读取

```python
# 读取
df_csv = pd.read_csv('data/my_csv.csv')
df_excel = pd.read_excel('data/my_excel.xlsx')

# 保存
df_csv.to_csv('data/my_csv_saved.csv', index=False)

# 取值
s.values
#取索引
s.index

#形状
s.shape

# 输出数据类型
df.dtypes
```





索引



列索引

```python


df['col_0'].head()

df[['col_0', 'col_1']]

# 输出列数据类型
df.dtypes

# 输出有哪里列
df.columns

```





行索引 loc

```python
# 返回索引名字为 Qiang Sun 的行
df_demo.loc['Qiang Sun']

# 选择  Qiang Sun行 和 School列 
df_demo.loc['Qiang Sun', 'School']

# 选择多行和多列
 df_demo.loc[['Qiang Sun','Quan Zhao'], ['School','Gender']]


    
# 选择 满足条件 df_demo.Weight > 70  的行。
df_demo.loc[df_demo.Weight>70].head()

# 满足条件 df_demo.Grade.isin(['Freshman', 'Senior']) 的行
df_demo.loc[df_demo.Grade.isin(['Freshman', 'Senior'])]

# 根据条件筛选          
 df_demo.loc[condition_1 | condition_2]

# condition可以是一个函数
df_demo.loc[condition]
    

```



![image-20230919214835411](https://zhangwenkang666.oss-cn-beijing.aliyuncs.com/image-20230919214835411.png)

![image-20230919214929452](https://zhangwenkang666.oss-cn-beijing.aliyuncs.com/image-20230919214929452.png)



行索引 iloc

```python
df_demo.iloc[1, 1] # 第二行第二列

df_demo.iloc[[0, 1], [0, 1]] # 前两行前两列

 df_demo.iloc[1: 4, 2:4] # 切片不包含结束端点
    
    
    
# iloc的条件索引 (df_demo.Weight>80).values
df_demo.iloc[(df_demo.Weight>80).values].head()
    
    
    
    
    
    
# query查询
df.query('Weight > Weight.mean()').head()
    
    
df.query('(Grade not in ["Freshman", "Sophomore"]) and''(Gender == "Male")').head()
    
    
    
    
```



![image-20230920091725022](https://zhangwenkang666.oss-cn-beijing.aliyuncs.com/image-20230920091725022.png)





常用基本函数

```python
    # 查看dataframe信息
    df.info()

    df.describe()

    # 求mean
    df_demo = df[['Height', 'Weight']]
     df_demo.mean()


    # max
    df_demo.max()

    # 分位数      
    df_demo.quantile(0.75)


    # 非缺失值个数
    df_demo.count()    
    
    
    # 对序列使用 unique 和 nunique 可以分别得到其唯一值组成的列表和唯一值的个数
    
    # 求唯一值的列表
    df['School'].unique()
    
    # 求唯一值的个数
    df['School'].nunique()
    
    # 求唯一值出现的次数
    df['School'].value_counts()
    
    
    # 多个列组合的唯一值
    df_demo = df[['Gender','Transfer','Name']]
	df_demo.drop_duplicates(['Gender', 'Transfer'])
    
    
    
    # 替换函数
    # Female被替换成0 Male被替换成1
    df['Gender'].replace({'Female':0, 'Male':1}).head()
    
    
    
    # 条件替换
    # where 函数在传入条件为 False 的对应行进行替换，而 mask 在传入条件为 True 的对应行进行替换
    s.where(s<0, 100)
    
    s.mask(s<0, -50)
    
    # 数值替换包含了 round, abs, clip 方法，它们分别表示取整、取绝对值和截断
    
    
    
    
    # 排序函数
    # 默认参数 ascending=True 为升序
    df_demo.sort_values('Height').head()
    
    # ascending=False 为降序
     df_demo.sort_values('Height', ascending=False).head()
    
    
    df_demo.sort_values(['Weight','Height'],ascending=[True,False]).head()
    
    
    
    
    
```



