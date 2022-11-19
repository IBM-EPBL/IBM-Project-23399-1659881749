import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xrt02017;PWD=0vLyQSpYuKJUgazb",'','')
print(conn)
print("connection successful")


sql="SELECT * FROM USERS"
stmt = ibm_db.exec_immediate(conn,sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary!=False:
    print("FUll ROW: ",dictionary)
    dictionary=ibm_db.fetch_assoc(stmt)