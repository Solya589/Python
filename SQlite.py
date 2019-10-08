import sqlite3, csv, os

def readFile(filename):
    file=os.path.splitext(filename)[0]
    with open(filename,'r') as fin:
        reader = csv.DictReader(fin, delimiter = "\t")
        fieldnames = reader.fieldnames
        columns = [x + " text" for x in fieldnames]

        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        cursor.execute("DROP TABLE IF EXISTS %s; " % file)
        cursor.execute("CREATE TABLE %s (%s)" % (file,  ",".join(columns)))

        stmt = "INSERT INTO %s (%s) VALUES(%s);" % (file,", ".join(fieldnames), ','.join('?' * len(fieldnames)))

        for record in reader:
            data = {k: v for k, v in record.items()}
            cursor.execute(stmt, list(data.values()))
        conn.commit()

        sql = "select * from %s" % file
        cursor.execute(sql)
        conn.close()
        return(data)

readFile("Project.csv")
readFile("Task.csv")

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
projectName=str(input("Enter a name of the project: "))
cursor.execute("select Project.Name, Task.* from Project "
               "left outer join Task on Project.Name=Task.Project "
               "where Project.Name='%s'" %projectName)
print(cursor.fetchall())
conn.close()
