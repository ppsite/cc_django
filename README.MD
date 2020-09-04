生成 Django 项目的 Cookiecutter 模板

> ### 支持

1. 环境支持: 开发环境，测试环境，生产环境
2. Django 项目最佳实践
3. 自定义用户模型支持
4. 环境变量管理: 从文件和系统环境变量中读取
5. 按需加载常见依赖包及相关配置
6. 生产环境配置支持 (uwsgi | nginx)
7. 支持 pyenv 自动创建 virtualenv

> ### 1. 安装 cookiecutter

MacOS 推荐使用 Home brew 安装，更多方法参考[官方部署文档](https://cookiecutter.readthedocs.io/en/1.7.0/installation.html)

```shell script
brew install cookiecutter
```

> ### 2. pyenv && pyenv-virtualenv

自动创建 python 虚拟环境依赖 pyenv，需在使用前安装 pyenv 和 pyenv-virtualenv

```shell script
# pyenv 支持脚本一键安装
$ curl https://pyenv.run | bash

# pyenv-virtualenv 安装
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

官方文档: [pyenv](https://github.com/pyenv/pyenv)
Pyenv插件: [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

> ### 3. 使用该项目创建模板

```shell script

cookiecutter https://github.com/pyFigure/cc_django

```

> ### 4. TODO

1. 按需加载 requirements
2. oauth2 支持
