#!/bin/sh
#Description:script contains multiple functions to make your life on AWS easy

detach-multiple-volumes() {

# input file	: detachVolumeIDs.input :: It contains the volumeIDs to detach (each line will be having volume id ONLY)
# output file	: detachedVolumes.output :: Output the response from command
# comment	: 1) Message in case command is not successful. Store those volume IDs and display them.
#            	  2) get required volume IDs using aws-cli filters 

	while read line
	 do
		aws ec2 detach-volume --volume-id $line >> detachedVolumes.output
		sleep 3
	 done < detachVolumeIDs.input
}


delete-multiple-volumes() {
        
# input file    : deleteVolumeIDs.input :: It contains the volumeIDs to delete (each line will be having volume id ONLY)
# output file   : deletedVolumes.output :: Output the response from command
# comment       : 1) Message in case command is not successful. Store those volume IDs and display them.
#                 2) get available volume IDs using aws-cli and filter them to get required volumes

        while read line
         do
           	aws ec2 delete-volume --volume-id $line >> deletedVolumes.output
	        sleep 3
         done < deleteVolumeIDs.input
}

allocate-attach-multiple-volumes() {

#This function allocate volumes and attach it to the instance

}

release-elastic-ips() {

# input file	: elasticIPs.input :: contains IPs to release. reads line by line and releases it.
# output file	: releasedEIPs.output :: Output the response from command
# comment	: check it should be unallocated or not

	while read line
	 do
		echo $line >> releasedEIPs.output
		aws ec2 release-address --public-ip $line >> releasedEIPs.output
 
	 done < elasticIPs.input

}


