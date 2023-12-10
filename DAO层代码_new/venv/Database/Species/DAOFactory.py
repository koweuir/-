from SQLSpeciesDAO import SQLSpeciesDAO
import pyodbc
from dbutils.persistent_db import PersistentDB

class DAOFactory:
    @staticmethod
    def create_species_dao():
        # 创建PersistentDB对象
        POOL = PersistentDB(
            creator=pyodbc,  # 使用链接数据库的模块
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。
            ping=0,  # ping MySQL服务端，检查是否服务可用。
            # 如果为False时，conn.close() 实际上被忽略，供下次使用，再线程关闭时，才会自动关闭链接。
            # 如果为True时，conn.close()则关闭链接，那么再次调用pool.connection时就会报错，
            # 因为已经真的关闭了连接（pool.steady_connection()可以获取一个新的链接）。
            threadlocal=None,  # 本线程独享值得对象，用于保存链接对象，如果链接对象被重置。
            driver='{SQL Server}',
            host='127.0.0.1',
            port=3389,
            user='sa',
            password='123456',
            database='education',
        )
        # 从连接池获取连接对象
        conn = POOL.connection()
        return SQLSpeciesDAO(conn)


