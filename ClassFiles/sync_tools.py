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

    def __init__(self, local_directory,  remote_directory):
        self.local_directory = local_directory
        self.base = "rsync -avzh --relative "
        self.remote_directory = remote_directory
        self.user = User()

    def push_to_server(self):
        #rsync -avz Documents/ root@157.230.57.175:~/backups/
        r_value = self.base + self.local_directory + " " + self.get_user_name() + "@" + self.get_remote_ip() + ":" + self.get_remote_dir()
        os.system(r_value)

    def pull_from_server(self):
        """
        Example: rsync -avz  root@157.230.57.175:~/backups/ ~/Documents
        """
        r_value = self.base + self.get_user_name() + "@" + self.get_remote_ip() + self.get_remote_dir() + " " + self.local_directory
        print(r_value)
        os.system(r_value)
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
        COMMAND = 'python3 get_directory.py'
        REMOTE = self.get_user_name() + "@" + self.get_remote_ip()
        ssh = subprocess.Popen(['ssh',REMOTE,COMMAND],
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        result = ssh.stdout.readline()
        if(result == []):
            error = ssh.stderr.readlines()
            print >> sys.stderr, "Error: %s" & error
        else:
            print(result)
        '''
        hostname = self.get_remote_ip()
        user = self.get_user_name()
        client = SSHClient()
        client.load_system_host_keys()
        client.connect(hostname, username=user)
        stdin, stdout, stderr = client.exec_command('python newnewdir.py')
        dir = stdout.readlines()
        with open('newnewdirectory.json','w') as fp:
            json.dump(dir,fp)



    def main(self):
        tool = sync_tool()

if __name__ == "__main__":

    sync = sync_tool('~/TestFolder/', '~/TestFolder/')
    sync.get_directory_on_server()



