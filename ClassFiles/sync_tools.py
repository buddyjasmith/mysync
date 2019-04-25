import os
import shutil
import time
from user import User
import sys
from paramiko import SSHClient
import subprocess
import pickle
import json

class sync_tool:

    def __init__(self):
        
        self.user = User()
        self.q = []
        

    def push_to_server(self,local_directory,remote_directory):
        #rsync -avz Documents/ root@157.230.57.175:~/backups/
        base = "rsync -avzh "
        r_value = base + local_directory + " " + self.get_user_name() + "@" + self.get_remote_ip() + ":" + remote_directory
        print(r_value)
        err = os.system(r_value)
        return True if(err==0) else False
        

    def pull_from_server(self,local_directory, remote_directory):
        """
        Example: rsync -avz  root@157.230.57.175:~/backups/ ~/Documents
        """
        if(not remote_directory.endswith('/')):
            print("shit went awry")
            remote_directory += '/'
        base = "rsync -avzh "
        r_value = base + self.get_user_name() + "@" + self.get_remote_ip() +":"+ remote_directory + " " + local_directory
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
        '''
        hostname = self.get_remote_ip()
        user = self.get_user_name()
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname, username=user)
        '''
        client = self.create_client()
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
        '''
        hostname = self.get_remote_ip()
        user = self.get_user_name()
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname, username=user)
        '''
        client = create_client()
        command ="cd " + path + " && mkdir " + new_dir 
       
        try:
            stdin, stdout, stderr = client.exec_command(command)
            return True
        except(BadHostException,AuthenticationException,SSHException, socket.error) as e:
            print(e)
            return False

    def create_client(self):
        hostname = self.get_remote_ip()
        user = self.get_user_name()
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname, username=user)
        return client
        
    def add_to_queue(self,path):
        self.q.append(path)
    
    def two_way_sync(self,local_directory,remote_directory):
        self.push_to_server(local_directory,remote_directory)
        self.pull_from_server(local_directory,remote_directory)


    def main(self):
        tool = sync_tool()

if __name__ == "__main__":

    sync = sync_tool()
    #sync.get_directory_on_server()
    #sync.pull_from_server('../../../Testing','~/Testing')
    #sync.pull_from_server('~/Testing','~/Testing')
    sync.two_way_sync('~/Testing/','~/Testing/')
    #sync.create_directory_server('./Testing','cats')



