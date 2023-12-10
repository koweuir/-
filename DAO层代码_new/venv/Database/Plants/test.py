from DAOFactory import DAOFactory
from Plants import Plants

plants_dao = DAOFactory.create_plants_dao()
plant = Plants(None, "2", "1", "1", "1", "1", "1", "1", "2022-9-9", "2023-6-5")
plants_dao.insert_plants(plant)  # 测试插入一个新的植物
plants_dao.delete_plant_by_id(2)  # 根据id删除某个植物

plant = Plants(1, "3", "3", "3", "3", "3", "1", "1", "2022-9-9", "2023-6-5")
plants_dao.update_plant(plant)  # 更新植物的信息
all_plants = plants_dao.search_subordinate_plants("2", "2", "2")  # 模糊查询
for p in all_plants:
    print(p.disease_name)
