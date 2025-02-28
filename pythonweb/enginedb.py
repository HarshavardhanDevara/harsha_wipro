from sqlalchemy import Column,Integer,String,create_engine, MetaData, Table, insert
 
#create a Database Engine
engine = create_engine(r'sqlite:///C:\Users\harsh\Desktop\harsha_wipro\pythonweb\testdb.db',echo=True)
#by "r" before path takes path more readable if it has backslashes also
 
#base class for model
meta = MetaData()
 
students = Table(
	'students',meta, Column('id',Integer,primary_key=True),
                         Column('name',String),
		         Column('city',String)
)
 
with engine.connect() as connection:
   stmt = insert(students).values(id=101,name="muni",city="tirupati")
   connection.execute(stmt)
   connection.commit()
 
print('Record is inserted')