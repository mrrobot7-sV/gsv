# nmap-gsv
Generate nmap version detection command (-sV) from the XML-output file generated by an nmap scan.
# Installation

+ Install requirements: ```pip install python-libnmap```
+ Download [nmap-gsv.py](nmap_parse_mrrobot7-sV/nmap_parse.py)

# How to use
```
python3 nmap-gsv.py -h
python3 nmap-gsv.py -x ./nmap_report.xml
python3 nmap-gsv.py -x ./nmap_report.xml -p ports
```

# Example
```
$ python3 nmap-gsv.py -x ./nmap_report.xml
nmap 10.10.11.47 -p 80,135,139,445,3389,49663,49667,49669 -sV -vv

$ python3 nmap-gsv.py -x ./nmap_report.xml -p ports
80,135,139,445,3389,49663,49667,49669
```
