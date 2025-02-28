from sqlalchemy import Column,Integer,String,create_engine, MetaData, Table
 
#create a Database Engine
engine = create_engine('sqlite:///C:/Users/harsh/Desktop/harsha_wipro/pythonweb/testdb.db',echo=True)
 
 
#base class for model
meta = MetaData()
 
Students = Table(
	'students',meta, Column('id',Integer,primary_key=True),
                         Column('name',String),
		         Column('city',String)
)
 
#create the table in database
meta.create_all(engine)
 
print('Table is created')