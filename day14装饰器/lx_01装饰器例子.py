import os


# 新添加的代码
# 最后我们执行的 还是 装饰器后面的代码  新加的代码不作为入口执行
def send_data(run):
    print("""
    1. 执行命令
    2. 发送监控数据
    3. 检测服务状态
    """)

    def run_cmd():
        return run()

    return run_cmd


# 原来的旧代码
@send_data  # 装饰器从下向上装饰  作用： 接入日志,函数处理前的处理
def exec_cmd():
    os.system('dir')


if __name__ == '__main__':
    exec_cmd()
