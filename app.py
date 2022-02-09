#import libraries
import requests
import mysql.connector
from mysql.connector import Error

#get data from api call
url = 'https://api.twitter.com/2/users/by?usernames=wavesprotocol,SignatureChain,neutrino_proto,sasha35625&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at'
bearerToken = 'AAAAAAAAAAAAAAAAAAAAALvmYwEAAAAAJPSM4F8E1IbwuSJHvThJMlXkJw8%3DbJCYq2JIWaEllT1CiUxdxgsYklmJUmIMwA44ai4Lgu3nQVGtn3'
headers = {'Authorization' : 'Bearer ' + bearerToken}
response = requests.get(url = url, headers = headers)
data = response.json()['data']
new_records = []

for item in data:
    list = []
    list.append(int(item['id']))
    list.append(item['username'])
    new_records.append(tuple(list))

print(new_records)

#connect to mysql database
userName = 'u122k7mhfbxvt0rp'
password = 'sYLq0OQvnWYw8Lv56bB6'
hostName = 'bp1o15l1iwoajeyerhf6-mysql.services.clever-cloud.com'
databaseName = 'bp1o15l1iwoajeyerhf6'

try:
    #cn = connect.MySQLConnection(
    #    user = userName,
    #    password = password,
    #    host = hostName, 
    #    database = databaseName,
    #)

    cn = mysql.connector.connect(
        user = userName,
        password = password,
        host = hostName, 
        database = databaseName,
    )

    print(cn)


    db = cn.database
    insert_statement = """INSERT INTO twitter_users (userId, userName) VALUES (%s, %s)"""
    #new_records = 

    if cn.is_connected():
        print(cn.get_server_info())
        cs = cn.cursor()
        #cs.execute()
        print(cs)
        cs.execute(operation="select database();")
        rows = cs.fetchall()
        print(rows)
        cs.execute(operation="select * from test;")
        tableData = cs.fetchall()
        print(tableData)
        cs.executemany(insert_statement, new_records)
        cn.commit()
        print(cs.rowcount)

except Error as e:
    print("Error while connecting to MySQL", e)
