import os
import shutil
import time
from user import User
import sys
from paramiko import SSHClient
import subprocess
import pickle
import json
import queue
class sync_tool:

    def __init__(self, local_directory,  remote_directory):
        self.local_directory = local_directory
        self.base = "rsync -avzh --relative "
        self.remote_directory = remote_directory
        self.user = User()
        self.q = []

    def push_to_server(self):
        #rsync -avz Documents/ root@157.230.57.175:~/backups/
        r_value = self.base + self.local_directory + " " + self.get_user_name() + "@" + self.get_remote_ip() + ":" + self.get_remote_dir()
        err = os.system(r_value)
        return True if(err==0) else False

    def pull_from_server(self):
        """
        Example: rsync -avz  root@157.230.57.175:~/backups/ ~/Documents
        """
        r_value = self.base + self.get_user_name() + "@" + self.get_remote_ip() + self.get_remote_dir() + " " + self.local_directory
        print(r_value)
        err = os.system(r_value)
        return True if (err==0) else False
        
    def get_user_name(self):
        return str(self.user.user['user_name'])

    def get_user_ip(self):
        return str(self.user.user['local_ip'])

    def get_remote_ip(self):
        return str(self.user.user['server_ip'])

    def get_remote_dir(self):
        return str(self.remote_directory)
    def get_directory_on_server(self):
   
        hostname = self.get_remote_ip()
        user = self.get_user_name()
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname, username=user)
        try:
            stdin, stdout, stderr = client.exec_command('python newnewdir.py')
            dir = stdout.readlines()
            try:
                with open('newnewdirectory.json','w') as fp:
                    json.dump(dir,fp)
            except EnvironmentError:
                print("IOError")
                return False
            return True
        except(BadHostException,AuthenticationException,SSHException, socket.error) as e:
            print(e)
            return False
        
        #not sure about the output of the json file, kinda funky
        

    def create_directory_server(self,path,new_dir):
        hostname = self.get_remote_ip()
        user = self.get_user_name()
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname, username=user)
        command ="cd " + path + " && mkdir " + new_dir 
        stdin, stdout, stderr = client.exec_command(command)
        try:
            stdin, stdout, stderr = client.exec_command(command)
            return True
         except(BadHostException,AuthenticationException,SSHException, socket.error) as e:
            print(e)
            return False
        


    def main(self):
        tool = sync_tool()

if __name__ == "__main__":

    sync = sync_tool('~/TestFolder/', '~/TestFolder/')
    sync.get_directory_on_server()
    sync.create_directory_server('./Testing','cats')



