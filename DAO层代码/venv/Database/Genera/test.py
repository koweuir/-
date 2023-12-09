from DAOFactory import DAOFactory
from Genera import Genera

genus_dao = DAOFactory.create_genera_dao()
genus = Genera(None, "5", "属3", "hdh", "2022-9-9", "2023-6-5")
#genus_dao.create_genus(genus) # 新建一个属
#genus_dao.delete_genus(1) # 根据id删除属
#genus_dao.update_genus("属100", "2020-6-3", 2) # 更新
allfamilies = genus_dao.search_genera("属") # 模糊查询
for f in allfamilies:
    print(f.genus_name)
