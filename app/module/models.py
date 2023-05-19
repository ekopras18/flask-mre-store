from flask_mysqldb import MySQL,MySQLdb
from app import app



app.config['MYSQL_HOST'] = 'mre.local'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'optima'
app.config['MYSQL_PASSWORD'] = 'optim4$#@!'
app.config['MYSQL_DB'] = 'flask_mre_store'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
