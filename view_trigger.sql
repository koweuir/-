USE test
--园林植物基本信息管理业务

--视图1：详细植物信息
--展示植物的详细信息，包括病⾍害信息和栽培技术。
GO
CREATE VIEW View_PlantDetails AS
SELECT
p.plant_id,
p.species_id,
p.alias,
p.morphology,
p.province,
p.city,
p.county,
p.growth_environment,
p.cultivation_techniques,
p.utilization_value
FROM
Plants p;
GO
--视图2：植物配图信息
--展示植物的配图信息，包括拍摄地点和拍摄⼈。
GO
CREATE VIEW View_PlantPictures AS
SELECT
p.plant_id,
p.alias,
pic.picture_id,
pic.position,
pic.descrip,
pic.photographer
FROM
Plants p
JOIN
Pictures pic ON p.plant_id = pic.plant_id;
GO
--视图3：植物病⾍害信息
--展示植物的病⾍害信息。
GO
CREATE VIEW View_PlantPestControl AS
SELECT p.plant_id, p.alias, pe.pest_id, pe.pest_name, s.strategy_id, s.method, s.pesticide_name, s.pesticide_amount
FROM Plants p
JOIN Pests_Plants pp ON p.plant_id = pp.plant_id
JOIN Pests pe ON pp.pest_id = pe.pest_id
JOIN PestControlStrategies s ON pe.pest_id = s.pest_id;
GO



--园林植物分类管理

--视图1：植物科⽬信息
--展示植物的科⽬信息。
GO
CREATE VIEW View_FamilyDetails AS
SELECT
f.family_id,
f.family_name
FROM
Families f;
GO
--视图2：植物属⽬信息
--展示植物的属⽬信息。
GO
CREATE VIEW View_GeneraDetails AS
SELECT
g.family_id,
g.genus_id,
g.genus_name
FROM
Genera g;
GO
--视图3：植物种⽬信息
--展示植物的种⽬信息。
GO
CREATE VIEW View_SpeciesDetails AS
SELECT
s.genus_id,
s.species_id,
s.species_name
FROM
Species s;
GO



--园林植物养护管理

--视图1：养护任务信息
--展示所有养护记录。
GO
CREATE VIEW View_MaintenanceTasks AS
SELECT 
    t.task_id,
    t.task_name,
    t.execution_time,
    t.execution_location,
    t.executor,
    t.task_description,
	t.target_plant_id
FROM MaintenanceTasks t
GO
--视图2：植物养略详细信息
--展示植物以及对应养护策略。
GO
CREATE VIEW View_PlantMaintenanceTasks AS
SELECT 
	p.plant_id,
    p.alias,
    t.task_id,
    t.task_name,
    t.execution_time,
    t.execution_location,
    t.executor,
    t.task_description
FROM MaintenanceTasks t
JOIN Plants p ON t.target_plant_id = p.plant_id;

GO
--视图3：植物养护与地区间的关系
--展示植物生长环境与养护管理的联系。
GO
CREATE VIEW View_RegionMaintenance AS
SELECT 
    p.alias,
    p.province,
    p.city,
    p.county,
    p.growth_environment,
    m.task_name AS maintenance_task,
    m.execution_time AS maintenance_execution_time,
    m.execution_location AS maintenance_execution_location,
    m.executor AS maintenance_executor
FROM Plants p
JOIN MaintenanceTasks m ON p.plant_id = m.target_plant_id
GO


--园林病⾍害防治管理

--视图1：病虫害信息
--展示所有病虫害。
GO
CREATE VIEW View_Pests AS
SELECT 
	P.pest_id, 
	P.pest_name
FROM Pests P
GO

--视图2：受影响植物
--展示受病虫害影响的植物。
GO
CREATE VIEW View_AffectedPlants AS
SELECT p.plant_id, p.alias, pc.pest_id, pe.pest_name
FROM Plants p
LEFT JOIN Pests_Plants pc ON p.plant_id = pc.plant_id
LEFT JOIN Pests pe ON pc.pest_id = pe.pest_id;
GO

--视图3：防治策略信息
--展示所有防治策略。
GO
CREATE VIEW View_PestControlStrategies AS
SELECT 
	pc.strategy_id, 
	p.pest_name, pc.method, 
	pc.pesticide_name, 
	pc.pesticide_amount, 
	pc.effective_period, 
	pc.other_info
FROM PestControlStrategies pc
JOIN Pests p ON pc.pest_id = p.pest_id;
GO


--园林植物监测管理

--视图1：监测设备与指标
--展示监测指标以及对饮设备。
GO
CREATE VIEW View_Monitor_Metric AS
SELECT 
	mp.monitor_device_id, 
	m.device_name, 
	mm.metric_id, 
	mt.metric_name
FROM Monitor_Plants mp
JOIN Monitor m ON mp.monitor_device_id = m.device_id
JOIN Monitor_Metric mm ON mp.monitor_device_id = mm.monitor_device_id
JOIN Metric mt ON mm.metric_id = mt.metric_id;
GO

--视图2：被监测植物
--展示设备监测的植物。
GO
CREATE VIEW View_Monitor_Plants AS
SELECT 
	m.device_id, 
	m.device_name, 
	p.plant_id, 
	p.alias, 
	p.morphology, 
	p.province, 
	p.city, 
	p.county
FROM Monitor_Plants mp
JOIN Monitor m ON mp.monitor_device_id = m.device_id
JOIN Plants p ON mp.plant_id = p.plant_id;

GO

--视图3：监测记录
--展示所有监测记录。
GO
CREATE VIEW View_Monitoring AS
SELECT 
	m.monitoring_id, 
	m.monitoring_time, 
	m.monitor_person,
	m.monitoring_location,
	p.alias, 
	mr.metric_name
FROM Monitoring m
JOIN Plants p ON m.target_plant_id = p.plant_id
JOIN Metric mr ON mr.metric_id = M.monitoring_index
GO



--园林植物基本信息管理业务
--存储过程,只允许管理员⾓⾊执⾏
GO
CREATE PROCEDURE AddPlant
@species_id INT,
@alias VARCHAR(255),
@morphology VARCHAR(MAX),
@province VARCHAR(50),
@city VARCHAR(50),
@county VARCHAR(50),
@growth_environment VARCHAR(100),
@cultivation_techniques VARCHAR(MAX),
@utilization_value VARCHAR(MAX)
AS
BEGIN
IF IS_ROLEMEMBER ('AdminRole') = 1
BEGIN
INSERT INTO Plants(species_id, alias, morphology, province, city, county, growth_environment, cultivation_techniques, utilization_value)
VALUES (@species_id, @alias, @morphology, @province, @city, @county, @growth_environment, @cultivation_techniques, @utilization_value)
END
ELSE
BEGIN
RAISERROR ('Insufficient permissions', 16, 1);
END
END;
GO

--园林植物分类管理

--插入种进行判断
-- 检查属是否存在
GO
CREATE TRIGGER CheckGenusExists
ON Species
FOR INSERT
AS
BEGIN
    -- 检查插入的种对应的属是否存在
    IF NOT EXISTS (
        SELECT 1
        FROM Genera
        WHERE genus_id = (SELECT genus_id FROM inserted)
    )
    BEGIN
        -- 属不存在，提示要先插入属
        RAISERROR ('请先插入对应的属', 16, 1)
        ROLLBACK TRANSACTION
        RETURN
    END
END;

GO
-- 使用示例
INSERT INTO Species (genus_id, species_name) VALUES (1, 'Species 1');


--插入属进行判断
-- 检查科是否存在
GO
CREATE TRIGGER CheckFamilyExists
ON Genera
FOR INSERT
AS
BEGIN
    -- 检查插入的种对应的属是否存在
    IF NOT EXISTS (
        SELECT 1
        FROM Families
        WHERE family_id = (SELECT family_id FROM inserted)
    )
    BEGIN
        -- 科不存在，提示要先插入科
        RAISERROR ('请先插入对应的科', 16, 1)
        ROLLBACK TRANSACTION
        RETURN
    END
END;

GO
-- 使用示例
INSERT INTO Genera (family_id, genus_name) VALUES (1, 'Genera 1')



--园林植物养护管理
--存储过程,只允许养护人员执⾏
GO
CREATE PROCEDURE AddMaintenanceTasks
@task_name VARCHAR(255),
@execution_time DATETIME,
@execution_location VARCHAR(255),
@executor VARCHAR(255),
@task_description VARCHAR(255),
@target_plant_id INT
AS
BEGIN
--设置由养护人员控制
IF IS_ROLEMEMBER ('AdminRole') = 2
BEGIN
INSERT INTO MaintenanceTasks(task_name, execution_time, execution_location, executor, task_description, target_plant_id)
VALUES (@task_name, @execution_time, @execution_location, @executor, @task_description, @target_plant_id)
END
ELSE
BEGIN
RAISERROR ('Insufficient permissions', 16, 1);
END
END;
GO


--园林病⾍害防治管理
-- 创建触发器，判断病虫害是否存在
CREATE TRIGGER trg_check_duplicate_pest
ON Pests
FOR INSERT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM inserted i INNER JOIN Pests p ON i.pest_name = p.pest_name)
    BEGIN
        RAISERROR('病虫害已存在，无法插入', 16, 1)
        ROLLBACK TRANSACTION
    END
END


--园林植物检测管理
--存储过程,只允许养护人员执⾏
GO
CREATE PROCEDURE AddMonitoring
@monitoring_time DATETIME,
@monitor_person VARCHAR(255),
@monitoring_location VARCHAR(255),
@target_plant_id INT,
@monitoring_index INT
AS
BEGIN
--设置由监测人员控制
IF IS_ROLEMEMBER ('AdminRole') = 3
BEGIN
INSERT INTO Monitoring(monitoring_time, monitor_person, monitoring_location, target_plant_id, monitoring_index)
VALUES (@monitoring_time, @monitor_person, @monitoring_location, @target_plant_id, @monitoring_index)
END
ELSE
BEGIN
RAISERROR ('Insufficient permissions', 16, 1);
END
END;
GO