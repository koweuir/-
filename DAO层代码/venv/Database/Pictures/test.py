from DAOFactory import DAOFactory
from Pictures import Pictures

pictures_dao = DAOFactory.create_pictures_dao()
pictures = Pictures(None, "2", "4", "4", "4", "4", "2022-9-9", "2023-6-5")
pictures_dao.create_pictures(pictures)  # 测试插入一个新的图片

all_pictures = pictures_dao.get_all_picturesById("1")  # 查询
for s in all_pictures:
    print(s.species_name)
