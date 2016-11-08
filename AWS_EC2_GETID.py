from pprint import pprint
from boto import ec2
import time
import boto

#these will ad an instance
#ec2instance = boto.connect_ec2()
#reservation = ec2instance.run_instances(image_id='ami-70065467', instance_type='t1.micro', key_name='ec2-sample-key')
#time.sleep(30)

ec2conn = ec2.connection.EC2Connection()
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    #pprint(i.__dict__)
    print "public_dns_name = "
    z = str(i.public_dns_name)
    print z[0:]
    print "ip_address = "
    a = str(i.ip_address)
    print a[0:]
    #pprint(i.ip_address)
    print "instance_type = "
    b = str(i.instance_type)
    print b[0:]
    print "id = "
    #pprint(i.id)
    c = str(i.id)
    print c[0:]
    print "_state = "
    #pprint(i._state)
    d = str(i._state)
    print d[0:]
    #break # remove this to list all instances
