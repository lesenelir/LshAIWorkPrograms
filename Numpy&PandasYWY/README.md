numpy版本 1.16.4
pands版本 0.25.0

### numpy intro
    NumPy包的核心是 ndarray 对象，它封装了python原生的同数据类型的 n 维数组。

### ndarray知识
    ndarray.shape 返回元祖。数组维度，表示每个维度中数组的大小。对于有 n 行和 m 列的矩阵，shape 将是 (n,m)
    ndarray.ndim 数组维度的数量。shape里面有几个数字，ndim就是多少
    ndarray.size = shape()里的元素乘积
    
    Notes：
        数组维度是指需要几个数字才能唯一确定这个元素，则这个数组就是几维
        一维：a[i]
        二维：b[i][j]
        三维：c[i][j][k]
   
### ndarray创建
    np.arange(num).reshape(乘积为num)
    np.random.randn()  满足正太分布
    np.random.randint(num1, num2, size=(,..))  
    
###  ndarray合并
    给已有数据添加行，比如，增添一些样本数据 np.concatenate([array1, array2])
    给已有数据添加列，比如，增添一些特征 np.concatenate([array1, array2], axis=1)
    Notes：
        添加行保证列数一致
        添加列保证行数一致
        axis=0 按照行向
        axis=1 按照列向
        
__________________________________________________________________________________________

### pandas intro
    pandas有容易使用的数据结构和数据分析工具
    Pandas 的主要数据结构是 Series（一维数据）与 DataFrame（二维数据）
    Series:
        一维数据，代表一行或者一列。由一组数据（不同数据类型）以及一组与之相关的数据标签（索引）组成
    DataFrame:
        二维数据，整个表格，多行多列。df.index & df.columns
        DataFrame可以看作由Series组成的字典
        
    
### pandas读取数据
    pandas读取表格类型数据：
        csv tsv txt : pd.read_csv
        excel : pd.read_excel
        mysql : pd.read_sql

### pandas 查询数据
    df.loc 根据行列的标签值查询【推荐】
        使用单个label值查询数据
        使用值列表批量查询
        使用数值区间进行范围查询
        使用条件表达式查询
        使用函数查询
    df.iloc 根据行列的数字位置查询
    df.where
    df.query
    
    Notes：
        注意降维 dataframe > series > data
        
### pandas 添加合并concat  
    concat：使用某种合并方式join，沿着某个轴向axis，把多个pandas对象（dataframe或series合并成一个）
    pandas.concat(objs, asix=0, join='outer', ignore_index=False)
    objs：列表，可以是Series 也可以是DataFrame
    asix：0代表按行合并，1代表按列合并
    join：合并时对齐方式，默认是outer join 也可以是 inner join
    ignore_index：是否忽略原来的数据索引
    
    Notes:
        特例：append方法
            DataFrame.append(other, ignore_index=False)
            append只有按行合并，没有按列合并，相当于concat的简写
                
    