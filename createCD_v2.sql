USE test

-- 创建科表
CREATE TABLE Families (
    family_id INT IDENTITY(1,1) PRIMARY KEY,
    family_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建属表
CREATE TABLE Genera (
    genus_id INT IDENTITY(1,1) PRIMARY KEY,
    family_id INT,
    FOREIGN KEY (family_id) REFERENCES Families(family_id),
    genus_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建种表
CREATE TABLE Species (
    species_id INT IDENTITY(1,1) PRIMARY KEY,
    genus_id INT,
    FOREIGN KEY (genus_id) REFERENCES Genera(genus_id),
    species_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建植物表
CREATE TABLE Plants (
    plant_id INT IDENTITY(1,1) PRIMARY KEY,
    species_id INT,
    FOREIGN KEY (species_id) REFERENCES Species(species_id),
    alias VARCHAR(255),
    morphology VARCHAR(255),
	province VARCHAR(50),
	city VARCHAR(50),
	county VARCHAR(50),
	growth_environment VARCHAR(100),
    cultivation_techniques VARCHAR(255),
    utilization_value VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建配图表
CREATE TABLE Pictures (
    picture_id INT IDENTITY(1,1) PRIMARY KEY,
    plant_id INT,
    FOREIGN KEY (plant_id) REFERENCES Plants(plant_id),
	photo VARBINARY(MAX),
    position VARCHAR(255),
    descrip VARCHAR(255),
    photographer VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建养护任务表
CREATE TABLE MaintenanceTasks (
    task_id INT IDENTITY(1,1) PRIMARY KEY,
    task_name VARCHAR(255),
    execution_time DATETIME,
    execution_location VARCHAR(255),
    executor VARCHAR(255),
    task_description VARCHAR(255),
    target_plant_id INT,
    FOREIGN KEY (target_plant_id) REFERENCES Plants(plant_id),
	creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

--创建病虫害表
CREATE TABLE Pests (
    pest_id INT IDENTITY(1,1) PRIMARY KEY,
    pest_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建病虫害防止策略表
CREATE TABLE PestControlStrategies (
    strategy_id INT IDENTITY(1,1) PRIMARY KEY,
    pest_id INT,
    FOREIGN KEY (pest_id) REFERENCES Pests(pest_id),
    method VARCHAR(255),
    pesticide_name VARCHAR(255),
    pesticide_amount VARCHAR(255),
    effective_period VARCHAR(255),
    other_info VARCHAR(255)
);

-- 创建监测表
CREATE TABLE Monitoring (
    monitoring_id INT IDENTITY(1,1) PRIMARY KEY,
    monitoring_time DATETIME,
    monitor_person VARCHAR(255),
    monitoring_location VARCHAR(255),
    target_plant_id INT,
    FOREIGN KEY (target_plant_id) REFERENCES Plants(plant_id),
    monitoring_index INT,
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- 创建异常监测记录表
CREATE TABLE AbnormalMonitoringRecords (
    record_id INT IDENTITY(1,1) PRIMARY KEY,
    monitoring_id INT,
    FOREIGN KEY (monitoring_id) REFERENCES Monitoring(monitoring_id),
    abnormal_value VARCHAR(255),
    record_time DATETIME,
    remark VARCHAR(255)
);

-- 创建员工表
CREATE TABLE Employees (
    employee_id INT IDENTITY(1,1) PRIMARY KEY,
    employee_name VARCHAR(255),
    contact_info VARCHAR(255),
    roleplay VARCHAR(255),
    other_info VARCHAR(255)
);

-- 病虫害-植物对应表
CREATE TABLE Pests_Plants (
    pest_id INT,
	FOREIGN KEY (pest_id) REFERENCES Pests(pest_id),
    plant_id INT,
	FOREIGN KEY (plant_id) REFERENCES Plants(plant_id),
    PRIMARY KEY (pest_id, plant_id)
);

CREATE TABLE Monitor (
    device_id INT IDENTITY(1,1) PRIMARY KEY,
    device_name VARCHAR(100)
);


CREATE TABLE Monitor_Plants (
  monitor_device_id INT,
  plant_id INT,
  PRIMARY KEY (monitor_device_id, plant_id),
  FOREIGN KEY (monitor_device_id) REFERENCES Monitor (device_id),
  FOREIGN KEY (plant_id) REFERENCES Plants (plant_id)
);

CREATE TABLE Metric (
  metric_id INT IDENTITY(1,1) PRIMARY KEY,
  metric_name VARCHAR(255)
);

CREATE TABLE Monitor_Metric (
  monitor_device_id INT,
  metric_id INT,
  PRIMARY KEY (monitor_device_id, metric_id),
  FOREIGN KEY (monitor_device_id) REFERENCES Monitor (device_id),
  FOREIGN KEY (metric_id) REFERENCES Metric (metric_id)
);