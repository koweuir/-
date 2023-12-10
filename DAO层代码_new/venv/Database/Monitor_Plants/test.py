from DAOFactory import DAOFactory
from Monitor_Plants import Monitor_Plants

monitor_plants_dao = DAOFactory.create_monitor_plants_dao()
monitor_plants = Monitor_Plants(2, 6)
monitor_plants_dao.insert_monitor(monitor_plants)
monitor_plants_dao.delete_monitor(1)
