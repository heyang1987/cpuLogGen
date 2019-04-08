# cpuLogGen

For this coding test, I have used python 3 and MongoDB (pymongo) to implement a CPU logs generator and a query tool under Linux.

The cpu log generator takes a path to the data file as a parameter to generate the cpu usage logs of exact 1000 servers with IP address ranging from 192.168.0.10 to 192.168.3.241 on the day of 2014-10-31.
Every server has two cpus. Each cpu will have a randomized cpu usage for every minute.

The query tool takes a directory of data files as a parameter and lets you query CPU usage for a specific CPU in a given time period. It is an interactive command line tool which read a user’s commands from stdin.
The tool supports two commands. One command will print results to stdout. Its syntax is QUERY IP cpu_id time_start time_end. Time_start and time_end should be specified in the format YYYY-MM-DD HH:MM where YYYY is a four digit year, MM is a
two digit month (i.e., 01 to 12), DD is the day of the month (i.e., 01 to 31), HH is the hour of the day, and MM is the minute of an hour. The second command to support is EXIT. It will exit the tool.

# Prerequisite
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
