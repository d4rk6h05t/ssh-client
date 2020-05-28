#!/usr/bin/python

"""

SSH Client

some very important additional notes:
1. you must have ssh installed on your operating system 
2. and the service must be activated to see its status you can use tools such as systemctl or service this varies from your distro GNU/Linux
3. The port you need to use must match your ssh 
4. ssh normally uses port 22, but if you already know this tool, you can change this setting if you wish
5. this code only works to connect with a normal user without many privileges since to use the root user more processes are needed besides this code
6. verify that the firewall is not blocking port 22, if it gives this permission, example in iptables to open a port is enabled as follows

iptables -A INPUT -p tcp -m tcp --dport <port> -j ACCEPT
"""
import os
import sys 
import paramiko

class SSHClient:
    
    def __init__(self,hostname, port, username, password):
        self._port = port
        self._hostname = hostname   
        self._username = username
        self._password = password
    
    def banner(self):
        print(':: An small ssh client v1.0 ')
        print(':: By: d4rk6h05t')
    
    def log(self,filename):
        """
        with this line you create a log file to see more details of your connection and your ssh client
        """
        paramiko.util.log_to_file( filename + '.log' ) 
    
    def init_client(self):
        # create your ssh client object and initialize it
        ssh_client = paramiko.SSHClient()

        # add a policy to accept user authentication services
        ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        try:
            # starts the connection if no exception is successfully made    
            ssh_client.connect(self._hostname , port=self._port, username=self._username, password=self._password)
            print('Connected successfully')
            # executes the command at the moment only executes simple commands, like: ls, less, who, cat, cd 
            stdin, stdout, stderr = ssh_client.exec_command("ls -la /home")
            # see the output status of the channel that implicitly opens the paramiko
            stdout.channel.recv_exit_status()
            # if applicable read the output lines as commands that give an example of output ls, less, who, cat, cd 
            lines = stdout.readlines()
            for line in lines:
                print(line)
            ssh_client.close()
        except paramiko.ssh_exception.AuthenticationException as message:
            print(message)
        except paramiko.ssh_exception.SSHException as message:
            print(message)
        except paramiko.AuthenticationException as message:
            print(message)

def main(argv):
    ssh_client = SSHClient("127.0.0.1",22,"youruser","yourpassword")
    ssh_client.banner()
    ssh_client.log('ssh_client')
    ssh_client.init_client()
    
if __name__ == '__main__':
    main(sys.argv[1:])
