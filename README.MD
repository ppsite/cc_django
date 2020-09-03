基于 CookieCutter 制作的 Django 项目基础开发框架

> ### 支持

Python==3.7.5

Django==2.2.14

Celery==4.3


> ### 为什么要做 cc_django 模板？

对于 python 开发者，web 全栈开发过程中，经常要创建 django 项目；而项目初始化阶段，通常会有如下几个操作

1. 根据架构安装相关 python 依赖包，并进行相应配置
2. 添加自定义代码包 (常用代码片段等)
3. 生产环境发布用到的配置 (uwsgi.ini | nginx.conf)

而上述这些操作在依赖包较多时，非常繁琐，而且经常会漏掉配置，往往需要花费几个小时之久；


> ### 1. 安装 cookiecutter

MacOS 推荐使用 Home brew 安装，更多方法参考[官方部署文档](https://cookiecutter.readthedocs.io/en/1.7.0/installation.html)

```shell script
brew install cookiecutter
```

> ### 2. 使用该项目创建模板

```shell script
cookiecutter https://github.com/pyFigure/cc_django
```

> ### 3. TODO

1. 按需加载 requirements
2. oauth2 支持
