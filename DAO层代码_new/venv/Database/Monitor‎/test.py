from DAOFactory import DAOFactory
from Monitor import Monitor

monitor_dao = DAOFactory.create_monitor_dao()
monitor = Monitor(1, "除草剂")
monitor_dao.insert_monitor(monitor)
monitor_dao.delete_monitor(1)
