import boto.ec2  
import sys
import time

noOfInstances = int(sys.argv[1])  #Storing the number of instances to be launched from the command line

print "No of instances to be launched------->"+str(noOfInstances)+'\n'

conn = boto.ec2.connect_to_region(sys.argv[2],aws_access_key_id='ENTER YOUR ACCESS KEY',aws_secret_access_key='ENTER YOUR SECRET ACCESS KEY')

myInstances = []
for i in range(0,noOfInstances):
	reservation = conn.run_instances("ami-9ff7e8af", instance_type='t2.micro')
	myInstances.append(reservation.instances[0])
	print myInstances

print "Launching the instances --- Please wait----Thank You\n"

time.sleep(15)

print "Do you want to delete all the instances or by ID? - Press ALL or ID\n"
response = raw_input()

if response.lower() in ['all','ALL']:
	print "All instances are now being TERMINATED!!!!\n" 
	for instance in myInstances:
		instance.terminate()
elif response.lower() in ['ID', 'id']:
	print "How many instances do you want to terminate?\n"
	delete_inst_no = int(raw_input())
	delInstances = []
	for i in range(0,delete_inst_no):
		print "Enter the Instance ID to be terminated\n"
		delInstances.append(raw_input())
		
	print "Deleting the instances --- according to the IDs specified\n"
	conn.terminate_instances(instance_ids=delInstances)
else:
	system.exit(0)



