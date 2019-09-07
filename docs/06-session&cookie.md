# Django 登录过程
+ 查询用户
+ login 逻辑
    + 先将用户的基本信息组成 json，然后加密生成加密的 session 字符串
    + 随机生成一串长的字符，叫做 sessionid
    + 将 sessionid 和 session 值绑在一起一起保存在数据库
    + 将 sessionid 写入到 cookie 中
    + 返回请求给浏览器
+ 浏览器
    + 拿到文本发现在 cookie 中写入了一个 sessionid
    + 将 cookie 中所有的值写入到本地存储文件中
    + 后续针对该网站的所有请求都会带上 cookie
+ django 判断用户是否登录
    + 拦截器拦截所有的请求
    + 在拦截器中发现了在 cookie 中的 sessionid 后，通过该 sessionid 查询到 session, 从 session 中解析出用户的 id，通过 id 查找到用户
    + 给每一个 request 都设置一个属性 user
    