flask启动不了的原因：
I faced the same issue while using PowerShell and that fix worked for me:
instead of using set FLASK_APP = run.py, try $env:FLASK_APP = "run.py"

如果用cmder的话,需要用"set FLASK_APP=hello.py"

Unicode 和 UTF-8 有何区别？
https://www.zhihu.com/question/23374078

装饰器：
http://blog.csdn.net/tb6013245/article/details/45010503

链接：http://www.jianshu.com/p/034a0af509f3
装饰器本质上是一个函数，该函数用来处理其他函数，它可以让其他函数在不需要修改代码的前提下增加额外的功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等应用场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用.概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
