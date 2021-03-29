
# import cx_Oracle
# import os
#
# os.environ['PATH'] = '~/usr/local/lib/instantclient_19_3'
#
#
# def oracleconnection():
#     os.environ['PATH'] = '~/usr/local/lib/instantclient_19_3'
#     con = cx_Oracle.connect('test','test','localhost/ORCLCDB.localdomain')
#     cur = con.cursor()
#     cur.execute('select username,pwd from users')
#
#     for i in cur:
#         credentials = [i[0],i[1]]
#     cur.close()
#     con.close()
#     return credentials
#
# a = oracleconnection()
# print(a[0])
# print(a[1])