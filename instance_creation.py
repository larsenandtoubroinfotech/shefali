#!/usr/bin/python
#python instance_creation.py "image_id" "key_name" "instance_type" "subnet_id" "service_name"
import boto3
import sys
image_id = sys.argv[1]
name = sys.argv[2]
key_name = sys.argv[3]
instance_type = sys.argv[4]
subnet_id = sys.argv[5]
service_name = sys.argv[6]
#creating ec2 instance and providing the script in the user-data for the installation of sftp service  
ec2 = boto3.connect_ec2()
key_pair = ec2.create_key_pair(key_name)  
key_pair.save('/home/shefali/.ssh')
instance = ec2.run_instances(
    ImageId = image_id,
    MinCount = 1,
    MaxCount = 1, 
    KeyName = key_name, 
    InstanceType = instance_type,
    SubnetId = subnet_id 
    user_data = "sh service_installation.sh"+service_name
)
#checks for the instance creation and display te public dns name
for i in ec2.get_all_instances():
    if i.id == instance.id:
        ec2.create_tags(
        Resources = [i.id],
        Tags = mktag(instance[name])
        break
print i.instances[0].public_dns_name 
