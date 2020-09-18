# 吃或商城

## **Version 1.0🐡：**

🐳基于后端框架Django和前端框架amazeui的前后段不分离开发。

🐉2020年4月2日---5月25日（已完成）


💃开发使用到的技术栈：Django+amzeui+layui+jquery+redis+celery+websocket+whoosh+mysql


🕺部署服务器用到的技术栈：nginx+uwsgi+channels


🤸一些第三方的服务：阿里云云服务器（学生机） + OSS + OCR身份识别 + 阿里云短信服务


🐠服务管理工具：supervisor

---

## **Version 2.0🐙：**

🐋重构Version1.0，基于后端框架Django+接口框架Django-Restful-Framework框架（正在开发，目前已开发80%的功能），前端欲打算使用Vue框架（才刚动工）,实现前后段分离式开发。


🐲2020年6月5日-----目前（正在开发中）


💃开发使用到的技术栈：Django+DRF+Vue+Jquery+Redis+Celery+Rabbitmq+Elasticsearch+Websocket+Mysql+Fastdfs+JWT


🕺部署服务器用到的技术栈：nginx+uwsgi+channels


🤸一些第三方的服务：阿里云云服务器（学生机） + OSS + OCR身份识别 + 阿里云短信服务


🐠服务管理工具：supervisor

---
#### **🥳主要修改🥳：**

1. 传统前后端不分离===>基于restful风格接口开发  👀

2. whoosh搜索后端====>elasticsearch搜索后端👀

3. django自带的模板语言====>前端使用vue前端框架👀

4. 由原来的redis作为消息队列====>增加消息队列rabbitmq👀

5. django默认的Storage本地存储=====>分布式fastdfs存储

6. django默认的传统session认证=====>JWT算法认证

---
## **🥶目前已完成的功能🥶：**

目前已开发43个API

---
## **🤤接口文档🤤：**

### 一. 用户个人信息相关API
  
  ---
  #### 1. 绑定手机号（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/email-or-phone-binding-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "phone": "13787833295",
  "code": "200",
  "is_existed": false,
  "way": "phone"
}
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  |phone|code|is_existed|way|
  -:|:-:|:-:|:-
  |str|str|bool|str|
  
  ---
  #### 2. 修改个人用户名（PATCH）
  
  **Url http://127.0.0.1:8000/consumer/information-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "username": "司yz"
  }
  ```
  
  **请求数据类型**
  |username|
  -:|:-
  |str|
  
  **响应Json数据格式:**
  ```json
  {
  "code": 4,
  "msg": "修改信息成功",
  "status": "success",
  "data": ""
}
```

 ---
  #### 3. 获取用户个人基本信息（GET）
  
  **Url http://127.0.0.1:8000/consumer/information-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  {
  "username": "syz247179876",
  "phone": "13787833295",
  "first_name": "张三",
  "head_image": "group1/M00/00/00/wKgAaV86kJ-ARxCAAA543lGjCZc7153661",
  "birthday": "1999-05-20",
  "sex": "男",
  "rank": "先锋会员",
  "safety": 60,
  "last_login": null
}
  ```
  
  **响应数据类型**
  |username|phone|first_name|head_image|birthday|sex|rank|safety|last_login|
  -:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-
  |str|str|str|str|str|str|str|int|str|
  
  ---
  #### 4. 修改用户密码（PATCH）
  
  **Url：http://127.0.0.1:8000/consumer/password-changes-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "new_password": "123456",
  "old_password": "654321",
  "code": "52351"
}
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
|new_password|old_password|code|
  -:|:-:|:-
  |str|str|str|
  
  
  ---
  #### 5. 实名认证（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/verification-name-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "face": file,
  "back": file
}
  ```
  
  **响应Json数据格式:**
  ```json
  {
  "code": 15,
  "msg": "身份认证成功",
  "status": "success",
  "data": ""
}
  ```
  
  **请求数据类型**
  |face|back|
  -:|:-
  |file|file|
  
  
   ---
  #### 6. 修改头像（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/shop-head-image-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "head_image": file
  }
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  |head_image|
  -:|:-
  |file|
  
  ---
  ### 二  用户收货地址相关API
  
  ---
  #### 7. 添加收获地址（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/address-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "recipients": "曾靖文",
  "region": "湖南工业大学泰山录三食堂2",
  "address_tags": "2",
  "phone": "13787833290"
}
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  |recipients|region|address_tags|phone|
  -:|:-:|:-:|:-
  |str|str|str|str|
  
  
  
  ---
  #### 8. 查询收获地址（GET）
  
  **Url：
  http://127.0.0.1:8000/consumer/address-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  
  待填
  
  
  
  ---
  #### 9. 修改地址信息（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/address-chsc-api/2/**
  
  
  **请求Json数据格式：**
  ```json
 {
  "recipients": "司司",
  "region": "度假村",
  "address_tags": "1",
  "phone": "13787833295",
  "default_address": true
}
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  |recipients|region|address_tags|phone|default_address|
  -:|:-:|:-:|:-:|:-
  |str|str|str|str|bool|
  
  **响应数据类型**
  待填
  
  
  
  ---
  #### 10. 删除收获地址信息（PUT）
  
  **Url：  http://127.0.0.1:8000/consumer/address-chsc-api/6/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **响应数据类型**
  待填
  
  ---
  ### 三  用户注册登陆API
  
  ---
  #### 11. 用户注册（POST）
  
  **Url：http://127.0.0.1:8000/consumer/register-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
 {
  "password": "1234567",
  "phone": "13787833295",
  "code": "PJHAV5",
  "way": "phone"
}
  ```
  
  **响应Json数据格式:**
  ```json
 待填
  ```
  
  **请求数据类型**
  |password|phone|code|way|
  -:|:-:|:-:|:-
  |str|str|str|str|
  
  
  
  
  ---
  #### 12. 用户登录（PUT）
  
  **Url：  http://127.0.0.1:8000/consumer/login-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "username": "13787833290",
  "password": "1234567",
  "previous_page": "?next=/chsc-syz-247179876-docs/",
  "is_remember": true,
  "way": "2"
}
  ```
  
  **响应Json数据格式:**
  ```json
   {
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImNoY2gyNDcxNzk4NzZAcXEuY29tIiwiZXhwIjoxNTk3NzUxNTE0LCJlbWFpbCI6IjI0NzE3OTg3NkBxcS5jb20iLCJvcmlnX2lhdCI6MTU5NzY2NTExNH0.x2YToUZ1VssJ9PGVLhlcNJVnFxSCsBi-E9N4NATf31g",
  "previous_page": "/chsc-syz-247179876-docs/"
}
  ```
  
  **请求数据类型**
  |username|password|previous_page|is_remember|way|
  -:|:-:|:-:|:-:|:-
  |str|str|str|bool|str|
  
  **响应数据类型**
  
  |token|previous_page|
  -:|:-
  |str|str|
  
  ---
  ### **足迹相关API** 
  
  ---
  #### 13. 删除单个足迹（DELETE）
  
  **Url：http://127.0.0.1:8000/consumer/foot-chsc-api/1/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **响应数据类型**
  
  
  
  
  
  ---
  #### 14. 删除全部足迹（DELTE）
  
  **Url：http://127.0.0.1:8000/consumer/foot-chsc-api/destroy_all/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  
  
  
  ---
  #### 15. 添加足迹（POST）
  
  **Url：http://127.0.0.1:8000/consumer/foot-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
  "pk":231231
}
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
  |pk|
  -:|:-
  |int|
  
  
  ---
  #### 16. 查看用户足迹（GET）
  
  **Url：http://127.0.0.1:8000/consumer/foot-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**

  ---
  ### **收藏模块API**
  

  #### 17. 添加收藏（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/favorites-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  {
    "commodity_pk":26537
}
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **请求数据类型**
   |pk|
   -:|:-
   |int|
  
  
  
  
  ---
  #### 18. 删除全部收藏商品（DEL）
  
  **Url：http://127.0.0.1:8000/consumer/favorites-chsc-api/destroy_all/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **响应数据类型**
  
  

  
  ---
  #### 19. 删除单个收藏商品（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/favorites-chsc-api/132/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **响应数据类型**
  
  
  
  ---
  #### 20. 查看收藏的商品（PUT）
  
  **Url：http://127.0.0.1:8000/consumer/favorites-chsc-api/**
  
  
  **请求Json数据格式：**
  ```json
  无
  ```
  
  **响应Json数据格式:**
  ```json
  待填
  ```
  
  **响应数据类型**


---
## **🥰个人技术博客🥰**

  👉👉👉  [博客地址](https://syzzjw.cn)
  
  qq:247179876(技术交流使用）
