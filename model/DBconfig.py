# 数据库连接的配置信息
Hostname = "127.0.0.1"  # 数据库主机名，通常是IP地址或域名，这里是本地主机
Port = 3306  # 数据库服务端口，MySQL默认使用3306端口
Username = "username"  # 数据库用户名，用于身份验证
Password = "password"  # 数据库密码，用于身份验证
Database = "database"  # 数据库名称，指要连接的具体数据库

# SQLAlchemy的数据库URI，用于配置数据库连接字符串
SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{Username}:{Password}@{Hostname}:{Port}/{Database}"
)
# 解释：使用pymysql驱动连接MySQL数据库，格式为：
# 'mysql+pymysql://<用户名>:<密码>@<主机>:<端口>/<数据库名>'

# SQLAlchemy的配置项，设置是否跟踪对象的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 解释：设置为False以禁用对对象更改的跟踪，这可以减少内存使用量
