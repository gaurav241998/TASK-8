#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")


if plate_no == "MH13 BN8454":
    print("<body style='padding: 40px;'>")
    print('''<pre>
    Registration Year : 2015
    Description: Audi A3 35 Attraction
    Engine Size: 1986
    Make / Model : Audi / A3
    Registration Date : 20/05/2015
    Registering Authority : SOLAPUR, INDIA
    Fuel Type : DIESEL
    </pre>''')
    print("</body>")

elif plate_no == "MH01A V8866":
    print("<body style='padding: 40px;'>")
    print('''<pre>
    Registration Year: 2010
    Description: JAGUAR XF PETROL 5.0 V8
    Engine Size: 5000
    Make / Model : JAGUAR / XF
    Registration Date : 22/02/2011
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : PETROL
    Fuel Type : CNG
    Engine No : 10052323430508PN
    </pre>''')
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
