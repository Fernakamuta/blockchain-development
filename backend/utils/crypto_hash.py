"""
Crypto Hash Function.
"""
import hashlib
import json


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given args.
    """
    print(f'args: {args}')

    stringified_args = sorted([json.dumps(arg) for arg in args])
    print(f'stringified_args: {stringified_args}')

    joined_data = ''.join(stringified_args)
    print(f'joined_data: {joined_data}')

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    """
    Main function for debugging.
    """
    print(
        f'crypto_hash("one", 2, [3]): {crypto_hash("one", 2, [3])}')


if __name__ == '__main__':
    main()
