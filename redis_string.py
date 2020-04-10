# from redis import string
#
# if __name__ == '__main__':
#     try:
#         sr = StrictRedis()
#         result = sr.set("name", "iheima")
#         print(result)
#     except Exception as e:
#         print(e)
#


from redis import StrictRedis
if __name__=="__main__":
    try:
        #创建StrictRedis对象，与redis服务器建⽴连接
        sr=StrictRedis()
        #添加键name，值为itheima
        result=sr.set('name','itheima')
        #输出响应结果，如果添加成功则返回True，否则返回False
        print(result)
    except Exception as e:
        print(e)