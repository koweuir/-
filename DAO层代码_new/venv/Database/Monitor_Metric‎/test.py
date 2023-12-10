from DAOFactory import DAOFactory
from Monitor_Metric import Monitor_Metric

monitor_metric_dao = DAOFactory.create_monitor_metric_dao()
monitor_metric = Monitor_Metric(1, "除草剂")
monitor_metric_dao.insert_monitor(monitor_metric)
monitor_metric_dao.delete_monitor(1)
