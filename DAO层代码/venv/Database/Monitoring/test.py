from DAOFactory import DAOFactory
from Monitoring import Monitoring

monitoring_dao = DAOFactory.create_monitoring_dao()
monitorings = Monitoring(None, "2", "1", "1", 1, "1", "1", "1", "1", "1")
monitoring_dao.create_monitoring(monitorings)
monitoring_dao.delete_monitoring(1)
