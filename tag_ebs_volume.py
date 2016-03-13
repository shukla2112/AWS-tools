""" This function is created to test the AWS lambda
    This function assumes that all your ec2 instnaces are tagged with the creator tag
    and the function execution tags the associated EBS volume with creator tag
"""

import boto3
import boto3.ec2

aws_access_key_id = "AKIAX12345MZZXXAMMA"  #replace with your accesskey
aws_secret_access_key = "7sZRTasdad1234asdfgh12345sdfghj23456sdfg" #replace with your secret key
region_name = 'us-east-1'

def tag_ebs_volumes(event, context):
    """get all the volumes
    Get associated instance id
    get the tag attached to the instance
    attach the tag to the volume"""

    s = boto3.Session(aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key,
                     region_name=region_name)

    ec2 = s.resource('ec2')
    filter = [ { 'Name' : 'status', 'Values' : ['in-use']}]
    volumes = ec2.volumes.filter(Filters=filter)

    for volume in volumes:
        volume_tag_flag = False
        if volume.tags == None:
            print "No tags attached to volume"
        else:
            for tag in volume.tags:
                if 'Creator' in tag.values():
                    volume_tag_flag = True
#                    print volume_tag_flag
                    break
        if volume_tag_flag:
            print "volume already have Creator tag"
        else:
            instance_id = volume.attachments[0]['InstanceId']
            instance = ec2.Instance(instance_id)
            instance_tag_flag = False
            for tag in instance.tags:
 #               print "***********hop1"
                if 'Creator' in tag.values():
                    instance_tag_flag = True
                    creator_tag = tag['Value']
#                    print creator_tag
                    break
            if instance_tag_flag:
#                print "#######" + instance_tag_flag
                creator_tags=[{ 'Key': 'Creator', 'Value': creator_tag}]
                volume.create_tags(Tags=creator_tags)
            else:
                print "No creator tag for the instance also"
