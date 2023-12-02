# 完整数据库表

**1. 科表 (Families)**

Families(科ID INT PK, 名称 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**2. 属表 (Genera)**

Genera(属ID INT PK, 科ID INT FK -> Families.科ID, 名称 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**3. 种表 (Species)**

Species(种ID INT PK, 属ID INT FK -> Genera.属ID, 名称 VARCHAR, 省 VARCHAR, 市 VARCHAR,县 VARCHAR,生长环境 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**4. 植物表 (Plants)**

Plants(植物编号 INT PK, 种ID INT FK -> Species.种ID, 病名 VARCHAR, 别名 VARCHAR, 形态特征 VARCHAR, 栽培技术要点 VARCHAR, 应用价值 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**5. 配图表 (Pictures)**

Pictures(配图ID INT PK, 植物编号 INT FK -> Plants.植物编号, 拍摄地点 VARCHAR, 描述 VARCHAR, 拍摄人 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**6. 养护任务表 (MaintenanceTasks)**

MaintenanceTasks(养护任务编号 INT PK, 任务名称 VARCHAR, 执行时间 DATETIME, 执行地点 VARCHAR, 执行人员 VARCHAR, 任务描述 VARCHAR, 养护对象 INT FK -> Plants.植物编号, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**7. 病虫害表 (Pests)**

Pests(病虫害编号 INT PK, 名称 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**8. 病虫害防治策略表 (PestControlStrategies)**

PestControlStrategies(策略ID INT PK, 病虫害编号 INT FK -> Pests.病虫害编号, 防治方法 VARCHAR, 药剂名称 VARCHAR, 药剂用量 VARCHAR, 作用期限 VARCHAR, 其他相关信息 VARCHAR)

**9. 监测表 (Monitoring)**

Monitoring(监测ID INT PK, 监测时间 DATETIME, 监测人员 VARCHAR, 监测地点 VARCHAR, 监测对象 INT FK -> Plants.植物编号, 监测指标 VARCHAR, 监测设备 VARCHAR, 创建人员 VARCHAR, 创建时间 DATETIME, 更新时间 DATETIME)

**10. 异常监测记录表 (AbnormalMonitoringRecords)**（可选）

AbnormalMonitoringRecords(记录ID INT PK, 监测ID INT FK -> Monitoring.监测ID, 异常值 VARCHAR, 记录时间 DATETIME, 备注 VARCHAR)

**11. 员工表 (Employees)**

Employees(员工ID INT PK, 姓名 VARCHAR, 联系方式 VARCHAR, 角色 VARCHAR, 其他相关信息 VARCHAR)
