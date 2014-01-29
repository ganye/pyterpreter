# pyterpreter.py

pyterpreter is an application meant to allow for quick and easy script
development and deployment. It does this by allowing for modules to be easily
written, which can then be easily loaded into the interpreter for configuration
and then running.

### Requirements
The base program uses only the standard library - however, many of the modules
may require scapy. The program will work just fine without scapy; however, it
will crash if you attempt to load a module which you don't have the 
requirements for.

### Example of a simple module being run:

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

### Usage
Simply type either '?' or 'help' to get a list of all commands and their
description/usage.

```
> ?
|-- load    Loads the given module for configuration and usage.
|-- quit    Exits the program cleanly.
|-- set     Change the current module's given property
|-- run     Execute the currently loaded module.
|-- help    Prints the help menu.
|-- list    Prints a list of all available modules in the given directory.
|-- exit    Exits the program cleanly.
|-- options Lists all the options for the currently loaded module
|-- ?       Prints the help menu.
```

### Writing a module
Writing a module is meant to be simple and effecient. Simply create a file in
the modules folder, inside of whatever subdirectory you see fit. Then, import
the base module

```python
from base.module import Module
```

and any other requirements, declaring a Module class. The name of the class
MUST be the same as the filename, with a capital letter; so arping.py looks
like

```python
class Arping(Module):
```

Next, declare an initialize function; inside this function, call
self.update_info() and self.set_options. Both of these functions will be passed
a dictionary declaring information about the script and the options for
configuration.

```python
class Arping(Module):
   def initialize(self):
      self.updae_info({
          'name' : 'Arping',
          'description' : 'Simple module to send an ARP out to the given' +
                          'network and prints the results.',
          'license' : 'BSD',
          'author' : ['ganye'],
      })
      self.set_options({
          'network' : [True, 'The network to scan for responses.',]
      })
```

The information passed to update_info is largely inconsequential - it is used
entirely for descriping and crediting a module.

For set_options, a dict should be passed containing a key that corresponds to
option being set, while the value is a list of the format

```
[Required, Description, <Default Value>]
```

So in this example, our Arping module has an option, 'network', which is
required, has a description of 'The network to scan for responses.', and no
default value.

Assigning a default value is just as simple

```python
      self.set_options({
          'foo' : [True, 'Fubar the foo bar', 'foo']
      })
```

Finally, just declare a run() function that does whatever you want your module
to do - this is the meat and potatoes, and entirely up to you to write.
