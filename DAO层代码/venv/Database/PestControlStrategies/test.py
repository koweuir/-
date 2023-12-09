from DAOFactory import DAOFactory
from PestControlStrategies import PestControlStrategies

strategies_dao = DAOFactory.create_pestControlStrategies_dao()
strategies = PestControlStrategies(None, 2, "1", "1", "1", "1", "1")
strategies_dao.create_pestControlStrategies(strategies)
strategies_dao.get_all_pestControlStrategies(1)

