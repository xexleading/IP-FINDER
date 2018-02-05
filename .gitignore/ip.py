import socket
import os

print ('''========= IP FINDER und ROTERABFRAGE =====
                ===========================
                 = coded by marc schröder =
                 = VERSION v1.0 =
                 =========================='''



                 a = input("Bitte geben Sie eine Website ein:")




                 print("IP-Adresse der von Ihnen eingegebenen Website:",socket.gethostbyname(a))

                 print("-" * 60)

                if ping == 'y' :
            os.system("ping -c 5 " + socket.gethostbyname(a))
            print("-" *56)
            if reply == 'y':
              print("UDP Traceroute results":)
              os.system("traceroute" socket.gethostbyname(a))
              print (TCP Traceroute results:") #{ if you want to TcpTracerout, you must become superuser in your OS.
              os.system("tcptraceroute "  + socket.gethostbyname(a))
        elif ping == 'n':
          print("Good Luck ;)")+


        else:
          print("please enter a vaild value?")
