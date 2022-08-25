```
#!/bin/bash

# This script is designed to query the Morpheus Data platform for various variables that can be used to create, delete, or modify any type of instance or object. 

# The following variables are available on the Morpheus Data platform: 

# accountId - The id of the account 
# apiEndpoint - The API endpoint URL 
# appEndpoint - The App endpoint URL 
# appVersion - The App version number 
# cloudId - The id of the cloud 
# containerId - The id of the container 
# containerName - The name of the container 
# groupId - The id of the group 
# instanceId - The id of the instance 
# instanceName - The name of the instance 
# masterInstanceId - The id of the master instance 
# masterInstanceName - The name of the master instance 
# planId - The id of the plan 
# siteId - The id of the site 
# siteName - The name of the site 
# storageContainerId - The id of the storage container 
# storageContainerName - The name of the storage container 
# storagePoolId - The id of the storage pool 
# storagePoolName - The name of the storage pool 
# tenantId - The id of the tenant 
# userId - The id of the user 
# userEmail - The email address of the user 
# userFirstName - The first name of the user 
# userLastName - The last name of the user 


echo "Enter the variable you would like to query: "
read variable

if [ $variable = "accountId" ]
then
	echo "The id of the account is: "
elif [ $variable = "apiEndpoint" ]
then 
	echo "The API endpoint URL is: "
elif [ $variable = "appEndpoint" ]
then
	echo "The App endpoint URL is: "
elif [ $variable = "appVersion" ]
then 
	echo "The App version number is: "
elif [ $variable = "cloudId" ]
then 
	echo "The id of the cloud is: "
elif [ $variable = "containerId" ]
then 
	echo "The id of the container is: "
elif [ $variable = "containerName" ]
then 
	echo "The name of the container is: "
elif [ $variable = "groupId" ]
then 
	echo "The id of the group is: "
elif [ $variable = "instanceId" ]
then 
	echo "The id of the instance is: "
elif [ $variable = "instanceName" ]
then 
	echo "The name of the instance is: "
elif [ $variable = "masterInstanceId" ]
then 
	echo "The id of the master instance is: "
elif [ $variable = "masterInstanceName" ]
then 
	echo "The name of the master instance is: "
elif [ $variable = "planId" ]
then 
	echo "The id of the plan is: "
elif [ $variable = "siteId" ]
then 
	echo "The id of the site is: "
elif [ $variable = "siteName" ]
then 
	echo "The name of the site is: "
elif [ $variable = "storageContainerId" ]
then 
	echo "The id of the storage container is: "
elif [ $variable = "storageContainerName" ]
then 
	echo "The name of the storage container is: "
elif [ $variable = "storagePoolId" ]
then 
	echo "The id of the storage pool is: "
elif [ $variable = "storagePoolName" ]
then 
	echo "The name of the storage pool is: "
elif [ $variable = "tenantId" ]
then 
	echo "The id of the tenant is: "
elif [ $variable = "userId" ]
then 
	echo "The id of the user is: "
elif [ $variable = "userEmail" ]
then 
	echo "The email address of the user is: "
elif [ $variable = "userFirstName" ]
then 
	echo "The first name of the user is: "
elif [ $variable = "userLastName" ]
then 
	echo "The last name of the user is: "
else
	echo "That is not a valid variable."
fi
```
