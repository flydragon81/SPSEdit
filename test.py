from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://root@localhost/study?charset=utf8')
Base = declarative_base(engine)
import logging

class User(Base):           # 继承声明基类
    __tablename__ = 'user'  # 设置数据表名字，不可省略
    id = Column(Integer, primary_key=True)   # 设置该字段为主键
    # unique 设置唯一约束，nullable 设置非空约束
    name = Column(String(64), unique=True, nullable=False)
    email = Column(String(64), unique=True)

    # 此特殊方法定义实例的打印样式
    def __repr__(self):
        return '<User: {}>'.format(self.name)