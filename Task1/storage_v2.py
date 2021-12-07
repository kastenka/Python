import argparse
import tempfile
import os
import json


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, "r") as file:
        raw_data = file.read()
        if raw_data:
            return json.load(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, "w") as file:
        file.write(json.dumps(data))


def put_data(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get_data(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Key")
    parser.add_argument("--val", help="Value")
    return parser.parse_args()


def main(storage_path):
    args = parse()

    if args.key and args.val:
        put_data(storage_path, args.key, args.val)
    elif args.key and not args.val:
        print(*get_data(storage_path, args.key), sep=", ")
    else:
        print("Something is wrong!")


if __name__ == "main":
    storage_path = os.path.join(tempfile, "storage.data")
    main(storage_path)
    
