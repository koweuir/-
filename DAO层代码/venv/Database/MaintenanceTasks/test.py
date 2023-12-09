from datetime import datetime

from DAOFactory import DAOFactory
from MaintenanceTasks import MaintenanceTasks


def get_current_date():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date


task_dao = DAOFactory.create_maintenanceTasks_dao()
task = MaintenanceTasks(None, "养护任务2", "2023-12-5", "北林", "hdh", "一个艰难的养护任务", 6, "hdh", "2032-2-8",
                        "2024-5-6")
# task_dao.create_maintenanceTasks(task) # 新增一个养护任务
# task_dao.delete_task(2) # 根据id删除一个养护任务
# task_dao.update_task("任务3", get_current_date(), "北京", "lisa", "easy", 6, get_current_date(), 2) # 更新
alltasks = task_dao.search_tasks("北")  # 模糊查询
for f in alltasks:
    print(f)

relativePlants = task_dao.search_plant_monitoring_maintenance(1)  # 查找植物对应的检测指标以及养护任务等信息
for p in relativePlants:
    print(p)
