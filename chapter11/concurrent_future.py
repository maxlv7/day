from concurrent.futures import ThreadPoolExecutor,wait,as_completed
from functools import partial
# futures是什么？

# 一个保存了未来结果的容器,类似于js的promise(个人理解)
import time

start = time.time()

def get_html(times):
    time.sleep(times)
    print("get %d page success!"%times)
    return times

executor = ThreadPoolExecutor(max_workers=3)

# 提交一个任务并立即执行
# executor.submit(get_html,(1))

#得到这个任务的返回值
# future = executor.submit(get_html,(3))
# print(future.result())


#要获取已经成功的task的返回
urls = [2,4,3]
# all_tasks = [executor.submit(get_html,(url)) for url in urls]
# wait(all_tasks)
# print(all_tasks)
# for future in as_completed(all_tasks):
#     data = future.result()
#     print('get %d page'%data)
#
# for f in all_tasks:
#     print(f.result())

for data in executor.map(get_html,urls):
    print("get %d page"%data)

end = time.time()-start
print(end)