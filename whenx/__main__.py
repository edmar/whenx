# Inside __main__.py in your whenx package
import argparse
from whenx.console import run, create, monitor, list, delete


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='The command to run.')
    parser.add_argument('--mission', help='The mission for the create command.')
    parser.add_argument('--id', help='The id for the delete command.')
    args = parser.parse_args()

    if args.command == 'run':
        run()  # Call the run function
    elif args.command == 'create':
        if args.mission:
            create(args.mission)  # Call the create function with the mission argument
        else:
            print('The create command requires a --mission argument.')
    elif args.command == 'monitor':
        monitor()
    elif args.command == 'list':
        list()
    elif args.command == 'delete':
        delete(args.id)
    else:
        print(f'Unknown command: {args.command}')


if __name__ == '__main__':
    main()
