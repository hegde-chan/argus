from argparse import ArgumentParser
import subprocess
from data import task_pb2


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    arg_parser.add_argument('--name', required=True)
    args = arg_parser.parse_args()
    program_name = args.name

    process = subprocess.run([program_name], capture_output=True)
    exit_code = process.returncode

    # Write out to protobuf
    filename = program_name + '.proto'
    task_instance = task_pb2.Task()
    task_instance.name = program_name
    task_instance.exit_code = exit_code
    task_instance.stdout = process.stdout
    task_instance.stderr = process.stderr

if __name__ == "__main__":
    main()
