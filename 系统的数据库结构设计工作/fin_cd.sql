USE CD -- ���ݿ�����

-- �����Ʊ�
CREATE TABLE Families (
    family_id INT PRIMARY KEY,
    family_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- ��������
CREATE TABLE Genera (
    genus_id INT PRIMARY KEY,
    family_id INT,
    FOREIGN KEY (family_id) REFERENCES Families(family_id),
    genus_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- �����ֱ�
CREATE TABLE Species (
    species_id INT PRIMARY KEY,
    genus_id INT,
    FOREIGN KEY (genus_id) REFERENCES Genera(genus_id),
    species_name VARCHAR(255),
    region VARCHAR(255),
    env VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- ����ֲ���
CREATE TABLE Plants (
    plant_id INT PRIMARY KEY,
    species_id INT,
    FOREIGN KEY (species_id) REFERENCES Species(species_id),
    disease_name VARCHAR(255),
    alias VARCHAR(255),
    morphology VARCHAR(255),
    cultivation_techniques VARCHAR(255),
    utilization_value VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- ������ͼ��
CREATE TABLE Pictures (
    picture_id INT PRIMARY KEY,
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

-- �������������
CREATE TABLE MaintenanceTasks (
    task_id INT PRIMARY KEY,
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

--�������溦��
CREATE TABLE Pests (
    pest_id INT PRIMARY KEY,
    pest_name VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- �������溦��ֹ���Ա�
CREATE TABLE PestControlStrategies (
    strategy_id INT PRIMARY KEY,
    pest_id INT,
    FOREIGN KEY (pest_id) REFERENCES Pests(pest_id),
    method VARCHAR(255),
    pesticide_name VARCHAR(255),
    pesticide_amount VARCHAR(255),
    effective_period VARCHAR(255),
    other_info VARCHAR(255)
);

-- ��������
CREATE TABLE Monitoring (
    monitoring_id INT PRIMARY KEY,
    monitoring_time DATETIME,
    monitor_person VARCHAR(255),
    monitoring_location VARCHAR(255),
    target_plant_id INT,
    FOREIGN KEY (target_plant_id) REFERENCES Plants(plant_id),
    monitoring_index VARCHAR(255),
    monitoring_device VARCHAR(255),
    creator VARCHAR(255),
    create_time DATETIME,
    update_time DATETIME
);

-- �����쳣����¼��
CREATE TABLE AbnormalMonitoringRecords (
    record_id INT PRIMARY KEY,
    monitoring_id INT,
    FOREIGN KEY (monitoring_id) REFERENCES Monitoring(monitoring_id),
    abnormal_value VARCHAR(255),
    record_time DATETIME,
    remark VARCHAR(255)
);

-- ����Ա����
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(255),
    contact_info VARCHAR(255),
    roleplay VARCHAR(255),
    other_info VARCHAR(255)
);






















