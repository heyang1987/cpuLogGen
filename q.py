import pymongo
import sys
import datetime

# get the souce file name
fName = sys.argv[1]

try:
    # open the source file and read the first line for title
    f = open(fName, "r")
    line = f.readline()

    # Connect to the database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["cpulog"]

    # Clean up the database
    print("Cleaning up the database ...", end='', flush=True)
    x = mycol.delete_many({})
    print("Done!")
    print("Cleaned up ", x.deleted_count, " documents.")

    # Create a bulkQuery for bulk inserting to improve performance
    bulkQuery = []

    # Store all the queries in bulkQuery
    print("Building bulk insert query ... ", end='', flush=True)
    line = f.readline()
    while line:
        line = line.strip().split('\t')
        query = {"timestamp":line[0],"IP":line[1],"cpu_id":line[2], "usage":line[3]}
        bulkQuery.append(query)
        line = f.readline()
    print("Done!")
    f.close()
    # # Print the bulkQuery    
    # for q in bulkQuery:
    #     print(q)

    # Insert into the database
    print("Inserting logs into database ... ", end='', flush=True)
    mycol.insert_many(bulkQuery)
    print("Done!")

    # Validate the number of logs inserted in the database
    print(mycol.count_documents({}), "logs inserted.")

    # Help Information
    print("=================Welcome to the QUERY Tool!=================")
    print("Available commands:")
    print("QUERY")
    print("  Purpose: query the cpu usage between two timestamps")
    print("  Command syntax: QUERY IP cpu_id time_start time_end")
    print("  e.g. QUERY 192.168.1.10 1 2014-10-31 00:00 2014-10-31 00:05")
    print("EXIT")
    print("  Purpose: exit the tool")
    print("  Command syntax: EXIT")

    # Wait the user to input QUERY or EXIT command
    while True:
        command = input(">").split(" ")
        if command[0] == "":
            pass
        elif command[0] == "EXIT":
            sys.exit()
        elif command[0] == "QUERY":
            # QUERY 192.168.1.10 1 2014-10-31 00:00 2014-10-31 00:05
            try:
                query_ip = command[1]
                query_cpu_id = command[2]
                sdate = command[3].split("-")
                stime = command[4].split(":")
                query_sdatetime = datetime.datetime(int(sdate[0]), int(sdate[1]), int(sdate[2]), int(stime[0]), int(stime[1])).strftime("%s")
                edate = command[5].split("-")
                etime = command[6].split(":")
                query_edatetime = datetime.datetime(int(edate[0]), int(edate[1]), int(edate[2]), int(etime[0]), int(etime[1])).strftime("%s")

                print("CPU{} usage on {}:".format(query_cpu_id, query_ip))
                myList = []
                for doc in mycol.find( {"IP":query_ip, "cpu_id":query_cpu_id, "timestamp":{ "$gte":query_sdatetime, "$lt":query_edatetime } } ):
                    mytime = datetime.datetime.fromtimestamp( int(doc["timestamp"]) )
                    str = "(" + mytime.strftime('%Y-%m-%d %H:%M') + ", " + doc["usage"] + "%)"
                    myList.append(str)
                myString = ",".join(myList)
                print(myString)

            except:
                print("Invalid QUERY command!")
                pass
        else:
            print("Invalid command!")

except IOError:
    print("Could not read file: ", fName)