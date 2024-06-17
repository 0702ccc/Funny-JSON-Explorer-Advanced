import argparse
import json
from icon_family import IconFamily
from Stratgy import *

def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='Display style')
    parser.add_argument('-i', '--icon', required=False, choices=['pocker', 'star', 'box'], help='Icon family')
    args = parser.parse_args()

    # Load JSON file
    with open(args.file, 'r') as file:
        data = json.load(file)
    context = Context()
    # Select the factory based on style
    if args.style == 'tree':
        context.set_strategy(Strategy_tree())
    elif args.style == 'rectangle':
        context.set_strategy(Strategy_rectangle())
    else:
        raise ValueError(f"Unknown style: {args.style}")

    # Select icon family
    icon = IconFamily(args.icon)

    # Construct and render the JSON tree
    root = context.execute_strategy()
    root.show(icon, data)


if __name__ == "__main__":
    main()
