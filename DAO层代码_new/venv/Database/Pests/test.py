from DAOFactory import DAOFactory
from Pests import Pests

pests_dao = DAOFactory.create_pests_dao()
pests = Pests(None, "89764", "ctc", "2022-9-9", "2023-6-5")
pests_dao.insert_pests(pests)  # 测试插入一个新的pest
pests_dao.delete_pest(2)  # 根据id删除某个pest

pests = Pests(1, "542", "ytr", None, None)
pests_dao.update_pests(pests)  # 更新pest的信息
