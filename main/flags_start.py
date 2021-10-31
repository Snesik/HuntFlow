import argparse

def flags():
    parser = argparse.ArgumentParser()
    parser.add_argument('key', type=str, help='key for use api')
    parser.add_argument('path', type=str, help='path in dir bd and resume')
    args = parser.parse_args()
    return args

