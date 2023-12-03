class Monitoring:
    def __init__(self, monitoring_id, monitoring_time, monitor_person, monitoring_location, target_plant_id, monitoring_index, monitoring_device, creator, create_time, update_time):
        self.monitoring_id = monitoring_id
        self.monitoring_time = monitoring_time
        self.monitor_person = monitor_person
        self.monitoring_location = monitoring_location
        self.target_plant_id = target_plant_id
        self.monitoring_index = monitoring_index
        self.monitoring_device = monitoring_device
        self.creator = creator
        self.create_time = create_time
        self.update_time = update_time
