# find the ifindex values and each veth names 
find /sys/class/net/veth* | xargs -I % echo 'cut -z -d"/" -f5 <<< % | tr "\n" " "; cat %/ifindex' | bash

# find the iflink of the container. it should be run in the container
cat /sys/class/net/eth0/iflink

# or if you want to traverse all the containers use this
for container in `docker ps -q`; do docker inspect --format='{{.Name}}' $container | tr '\n' ' '; docker exec -it $container cat /sys/class/net/eth0/iflink; done

# you can find which veth interface is mapped to which container
