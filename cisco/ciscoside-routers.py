import jinja2

routers = [
    {"hostname": "R1", "AS": "6509", "RR": "False", "interfaces" : [
        {"ip": "10.1.1.1", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.11.2", "netmask": "255.255.255.252", "interface": "f2/0", "type": "external"},
        {"ip": "10.0.12.1", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.0.11.1", "AS": "6453", "NxtSlf": "no"},
            {"ip": "10.2.2.2", "AS": "6509", "NxtSlf": "yes"}
    ]},
    {"hostname": "R2", "AS": "6509", "RR": "True", "interfaces" : [
        {"ip": "10.2.2.2", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal" },
        {"ip": "10.0.12.2", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"},
        {"ip": "10.0.17.1", "netmask": "255.255.255.252", "interface": "f2/0", "type": "external"},
        {"ip": "10.0.18.1", "netmask": "255.255.255.252", "interface": "f3/0", "type": "external"},
        {"ip": "10.0.23.1", "netmask": "255.255.255.252", "interface": "f0/0", "type": "internal"},
        {"ip": "10.0.24.1", "netmask": "255.255.255.252", "interface": "f4/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.1.1.1", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.3.3.3", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.4.4.4", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.0.17.2", "AS": "15296", "NxtSlf": "no"},
            {"ip": "10.0.18.2", "AS": "15296", "NxtSlf": "no"}
    ]},
    {"hostname": "R3", "AS": "6509", "RR": "False", "interfaces" : [
        {"ip": "10.3.3.3", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.23.2", "netmask": "255.255.255.252", "interface": "f0/0", "type": "internal"},
        {"ip": "10.0.34.1", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.2.2.2", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.4.4.4", "AS": "6509", "NxtSlf": "no"}
    ]},
    {"hostname": "R4", "AS": "6509",  "RR": "True", "interfaces" : [
        {"ip": "10.4.4.4", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.34.2", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"},
        {"ip": "10.0.45.1", "netmask": "255.255.255.252", "interface": "f5/0", "type": "internal"},
        {"ip": "10.0.104.1", "netmask": "255.255.255.252", "interface": "f2/0", "type": "external"},
        {"ip": "10.0.114.1", "netmask": "255.255.255.252", "interface": "f3/0", "type": "external"},
        {"ip": "10.0.24.2", "netmask": "255.255.255.252", "interface": "f4/0", "type": "internal"},
        {"ip": "10.0.46.1", "netmask": "255.255.255.252", "interface": "f6/0", "type": "internal"}
        ],
        "advertising" : [
        {"ip": "199.212.24.0", "netmask": "255.255.252.0"},
        {"ip": "205.189.32.0", "netmask": "255.255.255.0"},
        ],
        "neighbors": [
            {"ip": "10.6.6.6", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.2.2.2", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.3.3.3", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.5.5.5", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.0.114.2", "AS": "26677", "NxtSlf": "no"},
            {"ip": "10.0.104.2", "AS": "26677", "NxtSlf": "no"}
    ]},
    {"hostname": "R5", "AS": "6509", "RR": "False", "interfaces" : [
        {"ip": "10.5.5.5", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.56.1", "netmask": "255.255.255.252", "interface": "f2/0", "type": "internal"},
        {"ip": "10.0.35.2", "netmask": "255.255.255.252", "interface": "f1/0", "type": "external"},
        {"ip": "10.0.45.2", "netmask": "255.255.255.252", "interface": "f0/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.4.4.4", "AS": "6509", "NxtSlf": "yes"},
            {"ip": "10.6.6.6", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.0.35.1", "AS": "6453", "NxtSlf": "no"}
    ]},
    {"hostname": "R6", "AS": "6509", "RR": "False", "interfaces" : [
        {"ip": "10.6.6.6", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.56.2", "netmask": "255.255.255.252", "interface": "f2/0", "type": "internal"},
        {"ip": "10.0.46.2", "netmask": "255.255.255.252", "interface": "f6/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.5.5.5", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.4.4.4", "AS": "6509", "NxtSlf": "no"}
    ]},
    {"hostname": "R7", "AS": "15296", "RR": "False", "interfaces" : [
        {"ip": "10.7.7.7", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.79.1", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"},
        {"ip": "10.0.17.2", "netmask": "255.255.255.252", "interface": "f2/0", "type": "external"},
        {"ip": "10.0.78.1", "netmask": "255.255.255.252", "interface": "f4/0", "type": "internal"}
        ],
        "advertising" : [
        {"ip": "162.246.156.0", "netmask": "255.255.252.0"},
        {"ip": "198.202.130.0", "netmask": "255.255.255.0"},
        {"ip": "199.116.232.0", "netmask": "255.255.252.0"}
        ],
        "neighbors": [
            {"ip": "10.0.17.1", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.9.9.9", "AS": "15296", "NxtSlf": "no"},
            {"ip": "10.8.8.8", "AS": "15296", "NxtSlf": "no"}
    ]},
    {"hostname": "R8", "AS": "15296", "RR": "False", "interfaces" : [
        {"ip": "10.8.8.8", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.89.1", "netmask": "255.255.255.252", "interface": "f2/0", "type": "internal"},
        {"ip": "10.0.18.2", "netmask": "255.255.255.252", "interface": "f3/0", "type": "external"},
        {"ip": "10.0.78.2", "netmask": "255.255.255.252", "interface": "f4/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.0.18.1", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.9.9.9", "AS": "15296", "NxtSlf": "no"},
            {"ip": "10.7.7.7", "AS": "15296", "NxtSlf": "no"}
    ]},
    {"hostname": "R9", "AS": "15296", "RR": "False", "interfaces" : [
        {"ip": "10.9.9.9", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.79.2", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"},
        {"ip": "10.0.89.2", "netmask": "255.255.255.252", "interface": "f2/0", "type": "internal"},
        {"ip": "10.0.94.1", "netmask": "255.255.255.252", "interface": "f3/0", "type": "external"},
        {"ip": "10.0.95.1", "netmask": "255.255.255.252", "interface": "f4/0", "type": "external"},
        {"ip": "10.0.96.1", "netmask": "255.255.255.252", "interface": "f5/0", "type": "external"},
        {"ip": "10.0.97.1", "netmask": "255.255.255.252", "interface": "f6/0", "type": "external"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.8.8.8", "AS": "15296", "NxtSlf": "no"},
            {"ip": "10.7.7.7", "AS": "15296", "NxtSlf": "no"},
            {"ip": "10.0.94.2", "AS": "542", "NxtSlf": "no"},
            {"ip": "10.0.95.2", "AS": "542", "NxtSlf": "no"},
            {"ip": "10.0.96.2", "AS": "33091", "NxtSlf": "no"},
            {"ip": "10.0.97.2", "AS": "33091", "NxtSlf": "no"}
    ]},
    {"hostname": "R10", "AS": "26677", "RR": "False", "interfaces" : [
        {"ip": "10.10.10.10", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.104.2", "netmask": "255.255.255.252", "interface": "f2/0", "type": "external"},
        {"ip": "10.0.102.1", "netmask": "255.255.255.252", "interface": "f0/0", "type": "internal"},
        {"ip": "10.0.111.1", "netmask": "255.255.255.252", "interface": "f4/0", "type": "internal"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.0.104.1", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.12.12.12", "AS": "26677", "NxtSlf": "no"},
            {"ip": "10.11.11.11", "AS": "26677", "NxtSlf": "no"}
    ]},
    {"hostname": "R11", "AS": "26677", "RR": "False", "interfaces" : [
        {"ip": "10.11.11.11", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.112.1", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"},
        {"ip": "10.0.114.2", "netmask": "255.255.255.252", "interface": "f3/0", "type": "external"},
        {"ip": "10.0.111.2", "netmask": "255.255.255.252", "interface": "f4/0", "type": "internal"}
        ],
        "advertising" : [
        {"ip": "38.112.112.0", "netmask": "255.255.255.0", "NxtSlf": "no"},
        {"ip": "66.97.16.0", "netmask": "255.255.240.0", "NxtSlf": "no"},
        {"ip": "142.155.0.0", "netmask": "255.255.0.0", "NxtSlf": "no"}
        ],
        "neighbors": [
            {"ip": "10.0.114.1", "AS": "6509", "NxtSlf": "no"},
            {"ip": "10.12.12.12", "AS": "26677", "NxtSlf": "no"},
            {"ip": "10.10.10.10", "AS": "26677", "NxtSlf": "no"}
    ]},
    {"hostname": "R12", "AS": "26677", "RR": "False", "interfaces" : [
        {"ip": "10.12.12.12", "netmask": "255.255.255.255", "interface": "lo0", "type": "internal"},
        {"ip": "10.0.102.2", "netmask": "255.255.255.252", "interface": "f0/0", "type": "internal"},
        {"ip": "10.0.112.2", "netmask": "255.255.255.252", "interface": "f1/0", "type": "internal"},
        {"ip": "10.0.128.1", "netmask": "255.255.255.252", "interface": "f3/0", "type": "external"},
        {"ip": "10.0.129.1", "netmask": "255.255.255.252", "interface": "f4/0", "type": "external"},
        {"ip": "10.0.120.1", "netmask": "255.255.255.252", "interface": "f5/0", "type": "external"},
        {"ip": "10.0.121.1", "netmask": "255.255.255.252", "interface": "f6/0", "type": "external"}
        ],
        "advertising" : [],
        "neighbors": [
            {"ip": "10.10.10.10", "AS": "26677", "NxtSlf": "yes"},
            {"ip": "10.11.11.11", "AS": "26677", "NxtSlf": "no"},
            {"ip": "10.0.94.2", "AS": "5664", "NxtSlf": "no"},
            {"ip": "10.0.95.2", "AS": "5664", "NxtSlf": "no"},
            {"ip": "10.0.96.2", "AS": "32638", "NxtSlf": "no"},
            {"ip": "10.0.97.2", "AS": "32638", "NxtSlf": "no"}
    ]}
]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
template = environment.get_template("ciscoside-config.txt")

for router in routers:
    filename = f"config_{router['hostname']}.txt"
    content = template.render(
        router,
        hostname = router['hostname']
    )
    with open(filename, mode="w", encoding="utf-8") as blah:
        blah.write(content)
        print(f"... wrote {filename}")
