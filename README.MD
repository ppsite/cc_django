![image](https://github.com/pyfs/cc_django/blob/master/images/installing-1.png)
![image](https://github.com/pyfs/cc_django/blob/master/images/installing-2.png)

## 生成 Django 项目的 Cookiecutter 模板

# 项目支持

1. 环境支持: 开发环境，测试环境，生产环境
2. Django 项目最佳实践
3. 自定义用户模型支持
4. 环境变量管理: 从文件和系统环境变量中读取
5. 生产环境配置支持 (uwsgi)
6. 按需加载常见依赖包及相关配置(drf, grappelli, celery, boto3, media)等

# 安装 pyenv

自动创建 python 虚拟环境依赖 pyenv，需在使用前安装 pyenv 和 pyenv-virtualenv

```shell script
# pyenv 支持脚本一键安装
$ curl https://pyenv.run | bash

# pyenv-virtualenv 安装
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

> 官方文档: [pyenv](https://github.com/pyenv/pyenv) | Pyenv插件: [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

# 安装 cookiecutter

MacOS 推荐使用 Home brew 安装，更多方法参考[官方部署文档](https://cookiecutter.readthedocs.io/en/1.7.0/installation.html)

```shell script
brew install cookiecutter
```

# 快速使用

```shell script

cookiecutter https://github.com/pyfs/cc_django

```

# 选项说明

> DRF
 
Django Rest Framework，开发 restful api 工具箱

> GRAPPELLI

Django Admin 后台界面替换方案

> CELERY

异步任务支持

> BOTO3

AWS S3 存储支持，例如: MinIO

> MEDIA

自研应用，提供 ExternalImage 模型，方便将用户上传图片存储到 BOTO3

> TAG

自研应用，提供 ColoredTag 和 KeyValueTag 模型，方便给其他模型打标签