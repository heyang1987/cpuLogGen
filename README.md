# cpuLogGen

For this coding test, I have used python 3 and MongoDB (pymongo) to implement a CPU logs generator and a query tool under Linux.

# Usage
To use this software, you will need to have python 3 and mongoDB installed on you Linux system. Python 3 is shipped with Ubuntu 18.04.
To intall MongoDB, type following command in the terminal:

sudo apt install mongodb

Then start the mongodb server by typing following command in the terminal:

sudo service mongodb start

## Log Generator

To use the log generator, type following command wihtin the project folder in the terminal to generate a log file contains 1000 server's cpu usage. Each server has 2 cpu on it. 

./generate.sh /path/to/newLogFile

I have used only one write operation to write to the file, so it only takes several seconds to finish the process.

## Query Tool
To use the query tool, type following command within the project folder in the terminal with an additional parameter specifying the source logfile generated in previous step.

./query /path/to/GeneratedLogfile

The tool will first clean up the potential residual documents stored in the MongoDB database from previous experiment. Then it will generate a bulk query from the source log file and finally insert this query into the MongoDB database. By doing this, 
After above initialization, the query tool will wait for users' query input to return results.
There are two types of commands that are currently supported: QUERY  and EXIT

QUERY

  Purpose: query the cpu usage between two timestamps
  
  Command syntax: QUERY IP cpu_id time_start time_end
  
  e.g. QUERY 192.168.1.10 1 2014-10-31 00:00 2014-10-31 00:05
  
 EXIT
 
  Purpose: exit the tool
  
  Command syntax: EXIT
  
  ## Time spent
  1.5 hours, most of which was spent on commenting, testing, and documentation.
