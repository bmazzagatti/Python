#!/usr/bin/env python3
# This scripts allows the SCP function of multiple files to multiple remote hosts, in multiple locations
# written by Braeland Mazzagatti
#Date written: August 8th, 2023

import os
import subprocess
import readline
import glob

def complete(text, state):
    return (glob.glob(text + '*') + [None])[state]

readline.set_completer_delims('\t\n')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

def get_local_files():
    local_files = []
    print("Enter local file paths. Press Enter with no input to finish.")
    while True:
        local_path = input("Local file path: ")
        if not local_path:
            break
        if os.path.isfile(local_path):
            local_files.append(local_path)
        else:
            print("File not found. Provide a valid file path.")
    return local_files

def get_remote_hosts():
    remote_hosts = []
    print("Enter remote hosts. Press Enter with no input to finish.")
    while True:
        remote_host = input("Remote host (user@host): ")
        if not remote_host:
            break
        remote_hosts.append(remote_host)
    return remote_hosts

def validate_remote_path(remote_host, remote_path):
    command = f"ssh {remote_host} 'test -d {remote_path}'"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def main():
    local_files = get_local_files()
    remote_hosts = get_remote_hosts()

    if not local_files:
        print("No valid files provided. Exiting.")
        return
    
    if not remote_hosts:
        print("No valid hosts provided. Exiting.")
        return

    same_location = input("Copy all files to the SAME remote location on ALL hosts? (y/n): ").lower().strip() == 'y'
    remote_path = ""

    if same_location:
        remote_path = input("Enter remote path for all files on all hosts: ")

    successful_attempts = []
    unsuccessful_attempts = []

    for local_file in local_files:
        for remote_host in remote_hosts:
            if not same_location:
                remote_path = input(f"Enter remote path for {local_file} on {remote_host}: ")

            if validate_remote_path(remote_host, remote_path):
                scp_command = f"scp {local_file} {remote_host}:{remote_path}"
                result = subprocess.run(scp_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                if result.returncode == 0:
                    successful_attempts.append(scp_command)
                    print(f"SCP {local_file} to {remote_host}:{remote_path} completed!")
                else:
                    unsuccessful_attempts.append((scp_command, result.stderr.decode('utf-8')))
                    print(f"Failed to SCP {local_file} to {remote_host}:{remote_path}. Error: {result.stderr.decode('utf-8')}")
            else:
                print(f"Invalid remote path on {remote_host}. Provide a valid path.")

    print("\nSuccessful SCP attempts:")
    for cmd in successful_attempts:
        print(cmd)

if __name__ == "__main__":
    main()
