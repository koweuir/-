class MaintenanceTasks:
    def __init__(self, task_id, task_name, execution_time, execution_location, executor, task_description,
                 target_plant_id, creator, create_time, update_time):
        self.task_id = task_id
        self.task_name = task_name
        self.execution_time = execution_time
        self.execution_location = execution_location
        self.executor = executor
        self.task_description = task_description
        self.target_plant_id = target_plant_id
        self.creator = creator
        self.create_time = create_time
        self.update_time = update_time
