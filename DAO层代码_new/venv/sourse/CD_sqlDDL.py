# #园林植物基本信息管理业务
#
# # 插入植物
# "INSERT INTO Plants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?)",
#                        (plant.species_id, plant.alias, plant.morphology, plant.province, plant.city, plant.county, plant.growth_environment, plant.cultivation_techniques, plant.utilization_value, plant.creator, plant.create_time, plant.update_time)
#
# # 插入植物同时也要插入植物-病虫害对应表
# "INSERT INTO Pests_Plants VALUES(?, ?)",
#                         (plant.pest_id, plant.plant_id)
#
# # 根据编号删除植物
# "DELETE FROM Plants WHERE plant_id = ?",plant_id
#
# #修改植物
# "UPDATE Plants SET species_id = ?, alias = ?, morphology = ?, province = ?, city = ?, county = ?, growth_environment = ? ,cultivation_techniques = ?, utilization_value = ?, update_time = ? WHERE plant_id = ?",
#                         (plant.plant_id, plant.species_id, plant.alias, plant.morphology, plant.province, plant.city, plant.county, plant.growth_environment, plant.cultivation_techniques, plant.utilization_value, plant.update_time)
#
# # 查询植物基本信息
# "SELECT * FROM Plants WHERE plant_id = ? OR  alias like concat('%',?,'%') OR morphology like concat('%',?,'%') OR province like concat('%',?,'%') OR city like concat('%',?,'%') OR county like concat('%',?,'%') OR growth_environment like concat('%',?,'%') OR cultivation_techniques like concat('%',?,'%') OR utilization_value like concat('%',?,'%')",
#                         (plant_id, alias, morphology, province, city, county, growth_environment, cultivation_techniques, utilization_value)
#
# # 查询配图信息
# "SELECT * FROM Pictures WHERE plant_id = ? ",plant.plant_id
#
# # 查询病虫害防止策略
# "SELECT * FROM PestControlStrategies WHERE pest_id = (SELECT pest_id FROM Pests_Plants WHERE plant_id = ?) ",plant.plant_id
#
# #统计每科植物数量
# "SELECT Families.family_name, COUNT(Plants.plant_id) AS plant_count FROM Families LEFT JOIN Genera ON Families.family_id = Genera.family_id " \
# "LEFT JOIN Species ON Genera.genus_id = Species.genus_id " \
# "LEFT JOIN Plants ON Species.species_id = Plants.species_id " \
# "GROUP BY Families.family_name " \
# "ORDER BY plant_count DESC"
#
#
# # 园林植物分类管理
#
# # 增加科
# "INSERT INTO Families VALUES (?, ?, ?, ?)",
#                        (family.family_name, family.creator, family.create_time, family.update_time)
#
# # 删除属下所有种
# "DELETE FROM Species WHERE genus_id IN (SELECT genus_id FROM Genera WHERE family_id = (SELECT family_id FROM Families WHERE family_name = ?))",family_name
# # 删除科下所有属
# "DELETE FROM Genera WHERE family_id = (SELECT family_id FROM Families WHERE family_name = ?)",family_name
# # 删除科
# "DELETE FROM Families WHERE family_name = ?",family_name
#
#
# # 修改科
# "UPDATE Families SET family_name = ?, update_time = ? ",
#                        (family.family_name, family.update_time)
#
# # 查询科
# "SELECT * FROM Families WHERE family_id = ? OR family_name like concat('%',?,'%')",(family_id, family_name)
#
# # 增加属
# "INSERT INTO Genera VALUES (?, ?, ?, ?, ?)",
#                        (genera.family_id, genera.genus_name, genera.creator, genera.create_time, genera.update_time)
# # 删除属下所有种
# "DELETE FROM Species WHERE genus_id = (SELECT genus_id FROM Genera WHERE genus_name = ?)",genus_name
# # 删除属
# "DELETE FROM Genera WHERE genus_name = ?",genus_name
#
# # 修改属
# "UPDATE Genera SET family_id = ?, genus_name = ?, update_time = ? WHERE genus_id = ?",
#                        (genera.genus_id, genera.family_id, genera.genus_name, genera.update_time)
#
# # 查询属
# "SELECT * FROM Genera WHERE genus_id = ? OR  genus_name like concat('%',?,'%')",(genus_id, genus_name)
#
# # 增加种
# "INSERT INTO Species VALUES (?, ?, ?, ?, ?)",
#                        (species.genus_id, species.species_name, species.creator, species.create_time, species.update_time)
#
# # 删除种
# "DELETE FROM Species WHERE species_name = ?",species_name
#
# # 修改种
# "UPDATE Species SET genus_id = ?, species_name = ?, update_time = ? WHERE species_id = ?",
#                        (species.species_id, species.genus_id, species.species_name, species.update_time)
#
# # 查询种
# "SELECT * FROM Species WHERE species_id = ? OR species_name like concat('%',?,'%')",
#                         (species.species_id, species.species_name)
#
# #与植物基本信息的联动(根据植物id查找植物的种属科)
# "SELECT sp.species_name, gn.genus_name, fm.family_name FROM Plants pl " \
# "INNER JOIN Species sp ON pl.species_id = sp.species_id " \
# "INNER JOIN Genera gn ON sp.genus_id = gn.genus_id " \
# "INNER JOIN Families fm ON gn.family_id = fm.family_id " \
# "WHERE pl.plant_id = [Your_Plant_ID]"
#
# # 查找下属的植物情况
# "SELECT * FROM Plants " \
# "JOIN Plants ON Species.species_id = Plants.species_id " \
# "WHERE species_name like concat('%',?,'%')",species.species_name
#
# # ⽣⻓环境的模糊查询
# "SELECT * FROM Plants WHERE province like concat('%',?,'%') OR city like concat('%',?,'%') OR county like concat('%',?,'%') OR growth_environment like concat('%',?,'%') OR",
#                         (plant.province, plant.city, plant.county, plant.growth_environment)
#
#
# # 园林植物养护管理
#
# # 增加
# "INSERT INTO MaintenanceTasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
#                        (maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id, maintenanceTasks.creator, maintenanceTasks.create_time, maintenanceTasks.update_time)
#
# # 删除
# "DELETE FROM MaintenanceTasks WHERE task_id = ?",task_id
#
# # 修改
# "UPDATE MaintenanceTasks SET task_name = ?, execution_time = ?, execution_location = ?, executor = ?, task_description = ?, target_plant_id = ?, update_time = ? WHERE task_id = ?",
#                        (maintenanceTasks.task_id, maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id, maintenanceTasks.update_time)
#
# # 查询
# "SELECT * FROM MaintenanceTasks WHERE task_name like concat('%',?,'%') OR execution_time like concat('%',?,'%') OR execution_location like concat('%',?,'%') OR executor like concat('%',?,'%') OR task_description like concat('%',?,'%') OR target_plant_id like concat('%',?,'%')",
#                        (maintenanceTasks.task_name, maintenanceTasks.execution_time, maintenanceTasks.execution_location, maintenanceTasks.executor, maintenanceTasks.task_description, maintenanceTasks.target_plant_id)
#
# # 与检测之间的联动(查找植物对应的检测指标以及养护任务等信息)
# "SELECT MT.task_name AS MaintenanceTaskName,P.alias AS PlantAlias,P.disease_name AS PlantDiseaseName,M.monitoring_index AS MonitoringIndex FROM MaintenanceTasks MT " \
# "JOIN Plants P ON MT.target_plant_id = P.plant_id " \
# "LEFT JOIN Monitoring M ON P.plant_id = M.target_plant_id " \
# "WHERE MT.task_id = %d",task_id
#
# # 园林病⾍害防治管理
#
# # 对病⾍害信息的增加、修改、删除和查询
# "INSERT INTO Pests VALUES (?, ?, ?, ?)",
#                        (pests.pest_name, pests.creator, pests.create_time, pests.update_time)
#
# # 对病⾍害信息的修改
# "UPDATE Pests SET pest_name = ?, update_time = ? WHERE pest_id = ?",
#                         (pests.pest_id, pests.pest_name, pests.update_time)
#
# # 对病⾍害信息的删除
# "DELETE FROM Pests WHERE pest_id = %d",pest_id
#
# # 对病⾍害信息的查询
# "SELECT * FROM Pests WHERE pest_name like concat('%',?,'%')",pest_name
#
# # 联动查询病虫害以及防治信息(根据id查询病虫害名称以及防治策略信息)
# "SELECT P.pest_name,PCS.method,PCS.pesticide_name,PCS.pesticide_amount,PCS.effective_period,PCS.other_info FROM Plants PL " \
# "JOIN PestControlStrategies PCS ON PCS.plant_id = PL.plant_id " \
# "JOIN Pests P ON P.pest_id = PCS.pest_id " \
# "WHERE PL.plant_id = %d",plant_id
#
# # 与分类和养护管理的联动(查询受某种病虫害影响的植物的科)
# "SELECT DISTINCT F.family_name " \
# "FROM Families F " \
# "INNER JOIN Genera G ON F.family_id = G.family_id " \
# "INNER JOIN Species S ON G.genus_id = S.genus_id " \
# "INNER JOIN Plants P ON S.species_id = P.species_id " \
# "INNER JOIN Pests_Plants PP ON P.plant_id = PP.plant_id " \
# "INNER JOIN Pests PT ON PP.pest_id = PT.pest_id " \
# "WHERE PT.pest_name = ?",pest_name
#
#
# # 园林植物检测管理
#
# # 检测设备增删改
# "INSERT INTO Monitor VALUES (?)",device_name
#
# "DELETE FROM Monitor WHERE device_id = ?",device_id
#
# "UPDATE Monitor SET device_name = ? WHERE device_id = ?",(Monitor.device_id, Monitor.device_name)
#
# # 检测指标增删改
# "INSERT INTO Metric VALUES (?)",metric_name
#
# "DELETE FROM Metric WHERE metric_id = ?",metric_id
#
# "UPDATE Metric SET metric_name = ? WHERE metric_id = ?",(Metric.metric_id, Metric.metric_name)
#
# # 监测设备_监测指标对照表增删改
# "INSERT INTO Monitor_Metric VALUES (?, ?)",(monitor_device_id, metric_id)
#
# "DELETE FROM Monitor_Metric WHERE metric_id = ?",metric_id
#
# "UPDATE Monitor_Metric SET metric_id = ? WHERE monitor_device_id = ?",(monitor_device_id, metric_id)
#
# # 监测设备_监测对象对照表删改
# "DELETE FROM Monitor_Plants WHERE monitor_device_id = ? OR plant_id = ?",(monitor_device_id, plant_id)
#
#
# # 对监测表的增加
# "INSERT INTO Monitoring VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
#                        (monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location, monitoring.target_plant_id, monitoring.monitoring_index, monitoring.creator, monitoring.create_time, monitoring.update_time)
#
# # 插入监测设备_监测对象对照表
# "INSERT INTO Monitor_Plants VALUES (?, ?)",(monitor_device_id, plant_id)
#
# # 对监测表的修改
# "UPDATE Monitoring SET monitoring_time = ?, monitor_person = ?, monitoring_location = ?, target_plant_id = ?, monitoring_index = ?, update_time = ?  WHERE monitoring_id = ?",
#                         (monitoring.monitoring_id, monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location, monitoring.target_plant_id, monitoring.monitoring_index, monitoring.update_time)
#
# # 修改监测设备_监测对象对照表
# "UPDATE Monitor_Plants SET plant_id = ? WHERE monitor_device_id = (SELECT monitor_device_id FROM Monitor_Metric WHERE metric_id = ?)",metric_id
#
# # 删除
# "DELETE FROM Monitoring WHERE monitoring_id = ?",monitoring_id
#
# # 删除监测设备_监测对象对照表
# "DELETE FROM Monitor_Plants WHERE plant_id = (SELECT target_plant_id FROM Monitoring WHERE monitoring_id = ?)",monitoring_id
#
# # 查询
# "SELECT * FROM Monitoring WHERE monitoring_time like concat('%',?,'%') OR monitor_person like concat('%',?,'%') OR monitoring_location like concat('%',?,'%') OR target_plant_id = ? OR monitoring_index = ? ",
#                         (monitoring.monitoring_time, monitoring.monitor_person, monitoring.monitoring_location, monitoring.target_plant_id, monitoring.monitoring_index)
#
# # 查询监测设备_监测对象对照表(查询设备对应的植物)
# "SELECT m.device_name, p.plant_id, p.alias AS plant_name " \
# "FROM Monitor_Plants mp " \
# "JOIN Monitor m ON mp.monitor_device_id = m.device_id " \
# "JOIN Plants p ON mp.plant_id = p.plant_id " \
# "WHERE m.device_id = ?",monitor_device_id
#
# # 查询某一设备所对应的指标数量
# "SELECT m.device_name, COUNT(DISTINCT met.metric_id) AS metric_count " \
# "FROM Monitor_Metric mm " \
# "JOIN Monitor m ON mm.monitor_device_id = m.device_id " \
# "JOIN Metric met ON mm.metric_id = met.metric_id " \
# "WHERE m.device_id = ?" \
# "GROUP BY m.device_name",monitor_device_id
#
# # 提供平均值查询、最⼤值查询等统计查询
# "SELECT AVG(metric_count) AS avg_metric_count " \
# "FROM (" \
#         "SELECT m.device_name, COUNT(DISTINCT met.metric_id) AS metric_count " \
#         "FROM Monitor_Metric mm " \
#         "JOIN Monitor m ON mm.monitor_device_id = m.device_id " \
#         "JOIN Metric met ON mm.metric_id = met.metric_id " \
#         "GROUP BY m.device_name " \
# ") AS subquery"
#
# "SELECT MAX(metric_count) AS avg_metric_count " \
# "FROM (" \
#         "SELECT m.device_name, COUNT(DISTINCT met.metric_id) AS metric_count " \
#         "FROM Monitor_Metric mm " \
#         "JOIN Monitor m ON mm.monitor_device_id = m.device_id " \
#         "JOIN Metric met ON mm.metric_id = met.metric_id " \
#         "GROUP BY m.device_name " \
# ") AS subquery"
#
#
#
