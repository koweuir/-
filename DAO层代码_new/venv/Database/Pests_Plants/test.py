from DAOFactory import DAOFactory
from Pests_Plants import Pests_Plants

pests_dao = DAOFactory.create_pests_plants_dao()
pests_plants = Pests_Plants(1, 2)
pests_dao.insert(pests_plants)  # 测试插入一个新的pest

