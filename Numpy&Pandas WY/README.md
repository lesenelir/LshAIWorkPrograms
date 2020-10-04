numpy版本 1.16.4

### introduce
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
    np.random.randn()     