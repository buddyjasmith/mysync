import os
import time
from user import User
import sys
from paramiko import SSHClient
import subprocess



class sync_tool:

    def __init__(self):
        """
        :par
        """
        self.user = User()
        self.check_local_remote_mount_path()
        self.mount_remote_server()
        self.unmount_remote_directory()
        
       
     

    def check_sshfs_install(self):
        err = os.system("which sshfs")
        if(err == 0):
            return True
        else:
            status = subprocess.call("sudo apt install -y sshfs",shell=True)
        return True if(status==0) else False

    def mount_remote_server(self):
        mount_command = "sshfs " + self.user.get_user_name() + "@" + self.user.get_server_ip() + ":" + self.user.get_remote_path()
        mount_command += " " + self.user.get_local_remote_mount()
        #err = os.system(mount_command)
        #return True if(err==0) else False
        process = subprocess.Popen(mount_command,shell=True)
        process.communicate()
        process.wait()
        print(process)
    
        

    def check_local_remote_mount_path(self):
        MySyncRemote = os.path.expanduser(self.user.get_local_remote_mount())
        if(not os.path.isdir(MySyncRemote)):
            os.mkdir(MySyncRemote)

    def unmount_remote_directory(self):
        unmount_command = "fusermount -u " + os.path.expanduser(self.user.get_local_remote_mount())
        err = os.system(unmount_command)
        return True if(err == 0) else False
            
        
    def push_to_server(self,local_directory,remote_directory):
        #rsync -avz Documents/ root@157.230.57.175:~/backups/
        base = "rsync -avzh "
        local_directory = os.path.expanduser(local_directory)
        remote_directory= os.path.expanduser(remote_directory)
        rsync_cmd = base + local_directory + "/ " + remote_directory
        print (rsync_cmd)
        err = os.system(rsync_cmd)
        return True if(err==0) else False
        

    def pull_from_server(self,local_directory, remote_directory):
        """
        Example: rsync -avz  root@157.230.57.175:~/backups/ ~/Documents
        """
        local_directory = os.path.expanduser(local_directory)
        remote_directory = os.path.expanduser(remote_directory)
        base = "rsync -avzh "
        r_value = base + remote_directory +" " + local_directory
        print(r_value)
        err = os.system(r_value)
        return True if (err==0) else False
        
    def two_way_sync(self,local_directory,remote_directory):
        self.push_to_server(local_directory,remote_directory)
        self.pull_from_server(local_directory,remote_directory)

    def delete_from_remote(self,path):
        delete_path = os.path.expanduser(path)
        cmd = "rm -rf " + delete_path
        err = os.system(cmd)
        return True if (err==0) else False

    def add_directory_remote(self,new_dir_path):
        new_dir_path = os.path.expanduser(new_dir_path)
        cmd = "mkdir " + new_dir_path
        err = os.system(cmd)
        return True if (err==0) else False

    def main(self):
        tool = sync_tool()

if __name__ == "__main__":

    sync = sync_tool()
  



