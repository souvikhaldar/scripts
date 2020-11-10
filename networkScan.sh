#!/usr/bin/sh
echo "-----------------------------------------------------------------------"
echo "Scanning $1 for available machines, result stored in /tmp/list.txt"
echo "-----------------------------------------------------------------------"
sudo nmap -sn -oG /tmp/list.txt $1
echo "-----------------------------------"
echo "Scanning vulnerability of each host"
echo "-----------------------------------"
for ip in $(cat /tmp/list.txt | grep "Host" | cut -d " " -f 2)
do
	echo "------------------------------------------"
	echo "Scanning $ip for all vulnerabilities"
	echo "------------------------------------------"
	sudo nmap --script vuln $ip
	echo "------------------------------------------"
done | tee scan_result_$(date +%s).txt
