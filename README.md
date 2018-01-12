# Psychosis Introduction


## 运行步骤


1. 运行
- python manage.py migrate
- python manage.py runserver 0.0.0.0:8880（本地测试）; python manage.py runserver 0.0.0.0:80 （线上）


2. 浏览器访问
- http://0.0.0.0:8880/ （本地测试）
- http://111.230.111.127 （线上）


## 依赖

- mysql (需要在settings.py中配置数据库，包括数据库名称、用户名和密码。)

- pip install Django==1.8
- pip install mako==1.0.7
- pip install mysqlclient==1.3.12

