import pymysql

############### CONFIGURE THIS ###################
# Open database connection
db = pymysql.connect("162.241.219.116","ieeeqpuc_qpuser","234Ar234","ieeeqpuc_qpdatabase")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO test(id, name, email) \
   VALUES (0,'hello','luw055@ucsd.edu')"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
