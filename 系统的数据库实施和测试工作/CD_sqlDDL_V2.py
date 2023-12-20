#园林植物基本信息管理业务

# 插入植物
"INSERT INTO Plants VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (plant.species_id, plant.disease_name, plant.alias, plant.morphology, plant.cultivation_techniques, plant.utilization_value, plant.creator, plant.create_time, plant.update_time)

# 根据编号删除植物
"DELETE FROM Plants WHERE plant_id = %d",plant_id

#修改植物
"UPDATE Plants SET disease_name = %s, alias = %s, morphology = %s, cultivation_techniques = %s, utilization_value = %s, update_time = %s WHERE plant_id = %d",
                        (plant.disease_name, plant.alias, plant.morphology, plant.cultivation_techniques, plant.utilization_value, plant.update_time)

# 查询植物基本信息
"SELECT * FROM Plants WHERE disease_name like concat('%',%s,'%') OR alias like concat('%',%s,'%') OR morphology like concat('%',%s,'%') OR cultivation_techniques like concat('%',%s,'%') OR utilization_value like concat('%',%s,'%') ",
                        (disease_name, alias, morphology, cultivation_techniques, utilization_value)

# 查询配图信息
"SELECT * FROM Pictures WHERE plant_id = %s ",plant.plant_id

# 查询病虫害防止策略
"SELECT * FROM PestControlStrategies WHERE plant_id = %s ",plant.plant_id

#统计每科植物数量
"SELECT Families.family_name, COUNT(Plants.plant_id) AS plant_count FROM Families LEFT JOIN Genera ON Families.family_id = Genera.family_id " \
"LEFT JOIN Species ON Genera.genus_id = Species.genus_id " \
"LEFT JOIN Plants ON Species.species_id = Plants.species_id " \
"GROUP BY Families.family_name " \
"ORDER BY plant_count DESC"

# 创建视图，用于获取属和种的信息
"CREATE VIEW GenusAndSpecies AS SELECT g.genus_id, g.genus_name, g.family_id, f.family_name, s.species_id, s.species_name" \
"FROM Genera g" \
"JOIN Families f ON g.family_id = f.family_id" \
"JOIN Species s ON g.genus_id = s.genus_id"

# 创建视图，用于获取植物详细信息
"CREATE VIEW PlantDetails AS SELECT p.plant_id, p.disease_name, p.alias, p.morphology, p.cultivation_techniques, p.utilization_value, s.species_name, g.genus_name, f.family_name" \
"FROM Plants p" \
"JOIN Species s ON p.species_id = s.species_id" \
"JOIN Genera g ON s.genus_id = g.genus_id" \
"JOIN Families f ON g.family_id = f.family_id"

# 创建视图，用于获取植物照片信息
"CREATE VIEW PlantPictures AS SELECT pic.plant_id, pic.photo, pic.position, pic.descrip, p.disease_name" \
"FROM Pictures pic" \
"JOIN Plants p ON pic.plant_id = p.plant_id"



# 园林植物分类管理

# 增加科
"INSERT INTO Families VALUES (%s, %s, %s, %s)",
                       (family.family_name, family.creator, family.create_time, family.update_time)

# 删除科
"DELETE FROM Families WHERE family_id = %d",family_id

# 修改科
"UPDATE Families SET family_name = %s, update_time = %s ",
                       (family.family_name, family.update_time)

# 查询科
"SELECT * FROM Families WHERE family_name like concat('%',%s,'%')",family_name

# 增加属
"INSERT INTO Genera VALUES (%d, %s, %s, %s, %s)",
                       (genera.family_id, genera.genus_name, genera.creator, genera.create_time, genera.update_time)

# 删除属
"DELETE FROM Genera WHERE genus_id = %d",genus_id

# 修改属
"UPDATE Genera SET family_id = %d, genus_name = %s, update_time = %s WHERE genus_id = %d",
                       (genera.genus_id, genera.family_id, genera.genus_name, genera.update_time)

# 查询属
"SELECT * FROM Genera WHERE genus_name like concat('%',%s,'%')",genus_name

# 增加种
"INSERT INTO Species VALUES (%d, %s, %s, %s, %s, %s, %s)",
                       (species.genus_id, species.species_name, species.region, species.env, species.creator, species.create_time, species.update_time)

# 删除种
"DELETE FROM Species WHERE species_id = %d",species_id

# 修改种
"UPDATE Species SET genus_id = %d, species_name = %s, region = %s, env = %s, update_time = %s WHERE species_id = %d",
                       (species.species_id, species.genus_id, species.species_name, species.region, species.env, species.update_time)

# 查询种
"SELECT * FROM Species WHERE species_name like concat('%',%s,'%') OR region like concat('%',%s,'%') OR env like concat('%',%s,'%')",
                        (species.species_name, species.region, species.env)

#与植物基本信息的联动(根据植物id查找植物的种属科)
"SELECT sp.species_name, gn.genus_name, fm.family_name FROM Plants pl " \
"INNER JOIN Species sp ON pl.species_id = sp.species_id " \
"INNER JOIN Genera gn ON sp.genus_id = gn.genus_id " \
"INNER JOIN Families fm ON gn.family_id = fm.family_id " \
"WHERE pl.plant_id = [Your_Plant_ID]"

# 查找下属的植物情况
"SELECT * FROM Plants " \
"JOIN Plants ON Species.species_id = Plants.species_id " \
"WHERE species_name like concat('%',%s,'%') OR region like concat('%',%s,'%') OR env like concat('%',%s,'%')",
                        (species.species_name, species.region, species.env)

# ⽣⻓环境的模糊查询
"SELECT * FROM Species WHERE env like concat('%',%s,'%')",env


# 园林植物养护管理

# 增加
"INSERT INTO MaintenanceTasks VALUES (%d, %s, %s, %s, %s, %d, %s, %s, %s)",
                       (maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id, maintenanceTasks.creator, maintenanceTasks.create_time, maintenanceTasks.update_time)

# 删除
"DELETE FROM MaintenanceTasks WHERE task_id = %d",task_id

# 修改
"UPDATE MaintenanceTasks SET task_name = %s, execution_time = %s, execution_location = %s, executor = %s, task_description = %s, target_plant_id = %d, update_time = %s WHERE task_id = %d",
                       (maintenanceTasks.task_id, maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id, maintenanceTasks.update_time)

# 查询
"SELECT * FROM MaintenanceTasks WHERE task_name like concat('%',%s,'%') OR execution_time like concat('%',%s,'%') OR execution_location like concat('%',%s,'%') OR executor like concat('%',%s,'%') OR task_description like concat('%',%s,'%') OR target_plant_id like concat('%',%d,'%')",
                       (maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id)

# 与检测之间的联动(查找植物对应的检测指标以及养护任务等信息)
"SELECT MT.task_name AS MaintenanceTaskName,P.alias AS PlantAlias,P.disease_name AS PlantDiseaseName,M.monitoring_index AS MonitoringIndex FROM MaintenanceTasks MT " \
"JOIN Plants P ON MT.target_plant_id = P.plant_id " \
"LEFT JOIN Monitoring M ON P.plant_id = M.target_plant_id " \
"WHERE MT.task_id = %d",task_id

# 园林病⾍害防治管理

# 对病⾍害信息的增加、修改、删除和查询
"INSERT INTO Pests VALUES (%s, %s, %s, %s)",
                       (pests.pest_name, pests.creator, pests.create_time, pests.update_time)

"UPDATE Pests SET pest_name = %s, update_time = %s WHERE pest_id = %d",
                        (pests.pest_id, pests.pest_name, pests.update_time)

"DELETE FROM Pests WHERE pest_id = %d",pest_id

"SELECT * FROM Pests WHERE pest_name like concat('%',%s,'%')",pest_name

# 联动查询病虫害以及防治信息(根据id查询病虫害名称以及防治策略信息)
"SELECT P.pest_name,PCS.method,PCS.pesticide_name,PCS.pesticide_amount,PCS.effective_period,PCS.other_info FROM Plants PL " \
"JOIN PestControlStrategies PCS ON PCS.plant_id = PL.plant_id " \
"JOIN Pests P ON P.pest_id = PCS.pest_id " \
"WHERE PL.plant_id = %d",plant_id

# 与分类和养护管理的联动(查询受某种病虫害影响的植物的科)
"SELECT f.family_name FROM Families f " \
"INNER JOIN Genera g ON f.family_id = g.family_id " \
"INNER JOIN Species s ON g.genus_id = s.genus_id " \
"INNER JOIN Plants p ON s.species_id = p.species_id " \
"WHERE p.disease_name = %s",disease_name


# 园林植物检测管理

# 对相关信息的增加、修改、删除和查询
"INSERT INTO Monitoring VALUES (%s, %s, %s, %d, %d, %s, %s, %s, %s)",
                       (monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location, monitoring.target_plant_id, monitoring.monitoring_index, monitoring.monitoring_device, monitoring.creator, monitoring.create_time, monitoring.update_time)

"UPDATE Monitoring SET monitoring_time = %s, monitor_person = %s, monitoring_location = %s, target_plant_id = %d, monitoring_index = %d, monitoring_device = %s, update_time = %s  WHERE monitoring_id = %d",
                        (monitoring.monitoring_id, monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location, monitoring.target_plant_id, monitoring.monitoring_index, monitoring.monitoring_device, monitoring.update_time)

"DELETE FROM Monitoring WHERE monitoring_id = %d",monitoring_id

"SELECT * FROM Monitoring WHERE monitoring_time like concat('%',%s,'%') OR monitor_person like concat('%',%s,'%') OR monitoring_location like concat('%',%s,'%') OR target_plant_id = %d OR monitoring_index = %d OR monitoring_device like concat('%',%s,'%')",
                        (monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location, monitoring.target_plant_id, monitoring.monitoring_index, monitoring.monitoring_device)

# 提供平均值查询、最⼤值查询等统计查询
"SELECT AVG(monitoring_index) AS average_index " \
"FROM Monitoring " \
"WHERE target_plant_id = [目标植物ID]"

"SELECT MAX(monitoring_index) AS max_index " \
"FROM Monitoring " \
"WHERE target_plant_id = [目标植物ID]"

