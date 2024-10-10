API 使用文档


概述
本API提供了学生和项目的信息管理功能，包括学生注册、登录、项目的创建、读取、更新和删除等操作。


基本信息
API基础URL: http://127.0.0.1:8000/api/
内容类型: json


启动方式
进入项目根目录，执行命令：python manage.py runserver


接口列表
1. 学生注册
方法: POST
路径: /students/
示例: student.json
{
    "account": 1,
    "name": "张三",
    "signature": "这是个签",
    "memo": "这是备忘录",
    "project_count": 5,
    "password": "123456"
}

2. 学生登录
方法: POST
路径: /login/
示例: login.json
{
    "account": 1,
    "password": "123456"
}

3. 获取学生信息
方法: GET
路径: /students/{account}/
示例: /students/1/


4. 创建项目
方法: POST
路径: /projects/
示例: project.json
{
    "project_id": 1,
    "name": "科学研究项目",
    "initiator": "张三",
    "supervisor": "李教授",
    "summary": "项目的概要",
    "content": "项目的内容",
    "current_members": 5,
    "total_members": 10
}

5. 获取项目信息
方法: GET
路径: /projects/{project_id}/
示例: /projects/1/

6. 更新项目
方法: PATCH
路径: /projects/{project_id}/
示例: /projects/1/
示例: project_update.json
{
    "participants": "小王, 小李, 小赵",
    "total_members": 12
}

7. 删除项目
方法: DELETE
路径: /projects/{project_id}/
示例: /projects/1/

8. 搜索
方法: GET
路径: /projects/
参数:
name__icontains: 名称
initiator__icontains: 发起者
supervisor__icontains: 指导者
participants__icontains: 参与者
示例: /projects/?name__icontains=科学&supervisor__icontains=李


curl使用示例
部分功能如下
1. 学生注册
curl -X POST -H "Content-Type: application/json" -d @student.json http://127.0.0.1:8000/api/students/

2. 学生登录
curl -X POST -H "Content-Type: application/json" -d @login.json http://127.0.0.1:8000/api/login/

3. 获取学生信息
curl -X GET http://127.0.0.1:8000/api/students/

4. 创建项目
curl -X POST -H "Content-Type: application/json" -d @project.json http://127.0.0.1:8000/api/projects/

5. 获取项目信息
curl -X GET http://127.0.0.1:8000/api/projects/

6. 更新项目
curl -X PATCH -H "Content-Type: application/json" -d @project_update.json http://127.0.0.1:8000/api/projects/1/

7. 删除项目
curl -X DELETE http://127.0.0.1:8000/api/projects/1/

8. 搜索
curl -X GET http://127.0.0.1:8000/api/projects/?name__icontains=项目&supervisor__icontains=李