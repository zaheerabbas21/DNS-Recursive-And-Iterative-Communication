# DNS-Recursive-And-Iterative-Communication

This is a command line Project which helps to understand how the DNS servers communicate with each other.

# Design Document

Please click the following link : [DesignDoc](https://docs.google.com/document/d/1Eimv41L5Ux_zGSOL4soyMJsISRuCdBDwVvvInedXIpI/edit?usp=sharing)

You can leave comments on the design doc if you have any question regarding it.

# Setup

Fork and Clone OR Clone directly the project. And then follow these below steps.

This project makes use of [dnspython](https://github.com/rthalley/dnspython) library.
Install `dnspython` library:

```bash
pip install dnspython
```

Run the `servers` on different terminals processes:

```bash
python localDnsServer.py
python rootDnsServer.py
python tldDnsServer.py
python authoritativeDnsServer.py
```

Now Run the `client` file:

```bash
python client.py
```

You can give any domain and the servers will give you the respective IP Addresses.

The IP Address is queried using `dnspython` library. But this repo handles the communication between the servers and demos such senario.
If you find any issues, please feel free to open an issue. I will try to solve that issue.

If you like the project, give it a start. I would appreciate it.

Thank you for checking out the project.
