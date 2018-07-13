# -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, Table, Column, Integer,
    String, MetaData)
from sqlalchemy.schema import CreateTable

eng = create_engine("mysql://powerfuliu:Gurity123@rdsbi4u1v33wc6zn0w71o.mysql.rds.aliyuncs.com/moremom_dev")

meta = MetaData()
meta.reflect(bind=eng)

for table_name, table in meta.tables.items():
    print(table)
    print(CreateTable(table))
