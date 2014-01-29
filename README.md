# pyterpreter.py

pyterpreter is an application meant to allow for quick and easy script
development and deployment. It does this by allowing for modules to be easily
written, which can then be easily loaded into the interpreter for configuration
and then running.

## Example of a simple module being run:
```
> load tools arping
> (/modules/tools/arping) options
|-- network         The network to scan for responses.
> (/modules/tools/arping) set network 192.168.1.1/20
> (/modules/tools/arping) run
[+] sending arping...
[+] done
[-] warning: couldn't get the terminal window size - printing without formatting.
MAC                     IP
00:25:9c:e2:e1:db       192.168.1.1
00:0e:83:d4:f0:00       192.168.1.10
bc:5f:f4:79:9d:77       192.168.1.101
b8:27:eb:5f:d9:54       192.168.1.111
00:13:7f:24:63:40       192.168.1.11
> (/modules/tools/arping) exit
```
