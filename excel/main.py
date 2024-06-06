import pandas as pd
#pandas 会帮助我们创建一个数据表格，可以对数据表格进行相关操作，然后将数据表格同步到excel中


# 1 手动的创建一个pandas的数据表格

table = pd.DataFrame(columns=['name','salary','job_title'])

#2 给数据表格插入数据
table.loc[0] = ['Jay',40000,'singer']
table.loc[1] = ['Tom',40000,'sale']

print(table)

#3将数据表格转换成excel
table.to_excel('text.xlsx',sheet_name='haha')





pd.read_excel('movie_list.xlsx')

