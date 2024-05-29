import os.path
from argparse import ArgumentParser
import subprocess
from data import task_pb2
import time
import re


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args, program_to_run = arg_parser.parse_known_args()
    program_name = " ".join(program_to_run)

    filename = os.getenv('HOME') + '/.argus/' + "".join(program_to_run) + str(time.time()) + '.proto'
    task_instance = task_pb2.Task()
    task_instance.name = program_name
    task_instance.status = task_pb2.Status.QUEUED
    if not os.path.exists(os.getenv('HOME') + '/.argus/'):
        os.makedirs(os.getenv('HOME') + '/.argus/')
    with open(filename, 'xb') as f:
        f.write(task_instance.SerializeToString())
        print(f'wrote output to {filename}')

    process = subprocess.run(program_to_run, capture_output=True)
    exit_code = process.returncode

    # Write out to protobuf

    task_instance = task_pb2.Task()
    task_instance.name = program_name
    task_instance.exit_code = exit_code
    task_instance.stdout = process.stdout
    task_instance.stderr = process.stderr
    task_instance.status = task_pb2.Status.FINISHED
    with open(filename, 'wb') as f:
        f.write(task_instance.SerializeToString())
        print(f'Task finished')
        print(f'wrote output to {filename}')

if __name__ == "__main__":
    main()
