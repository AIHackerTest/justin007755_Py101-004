### 用Git去Clone部分文件

周六的meetup活动里，有一个需求是只clone代码库的部分代码，不是全部。所以研究了一下配置模式，这里应该采用sparse checkout（稀疏克隆）。具体步骤如下：

指定远程仓库
mkdir project_folder
cd project_folder
git init
git remote add -f origin <url>

指定克隆模式: 稀疏克隆模式
git config core.sparsecheckout true

指定克隆的文件夹(或者文件)
echo “libs” >> .git/info/sparse-checkout

拉取远程文件
git pull origin master

![](https://github.com/justin007755/Py101-004/blob/master/Chap3/resource/git_sparse.PNG)

我碰到的一个问题是，当用Cmder来运行上述步骤时，会出现“error: Sparse checkout leaves no entry on working directory”，没太搞清楚原因。换成git cmd以后，没有出现类似问题。
