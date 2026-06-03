import mysql.connector

def get_database_connection():
     connection = mysql.connector.connect(
         host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
         user = '4T9q7Q51gC3kXeA.root',
         password = 'RLdjFDHFFxlQ9F7M',
         database = 'student_task_manager',
         port = 4000
     )

     return connection