from DAOFactory import DAOFactory
from Species import Species

species_dao = DAOFactory.create_species_dao()
species = Species(None, "2", "木贼麻黄", "beijing", "beijing", "ctc", "2022-9-9", "2023-6-5")
species_dao.insert_species(species)  # 测试插入一个新的种
species_dao.delete_species_by_name(2)  # 根据id删除某个种

species = Species(1, None, None, "shanghai", "shanghai", None, None, None)
species_dao.update_species(species)  # 更新种的信息
