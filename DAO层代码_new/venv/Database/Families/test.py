from DAOFactory import DAOFactory
from Families import Families

family_dao = DAOFactory.create_families_dao()
families = Families(None, "科5", "hdh", "2022-9-9", "2023-6-5")
#family_dao.create_families(families) # 测试插入一个新的科
# family_dao.delete_family(2) # 根据id删除某个科
#amily_dao.update_family("科100", "2020-6-3", 3) # 更新科的信息
allfamilies = family_dao.search_family("科") # 模糊查询
for f in allfamilies:
    print(f.family_name)

a=family_dao.count_plants_by_family(); # 统计
for i in a:
    print(i)


