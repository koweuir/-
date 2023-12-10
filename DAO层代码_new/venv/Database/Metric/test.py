from DAOFactory import DAOFactory
from Metric import Metric

metric_dao = DAOFactory.create_metric_dao()
metric = Metric(1, "除草剂")
metric_dao.insert_monitor(metric)
metric_dao.delete_monitor(1)
