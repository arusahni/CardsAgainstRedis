#!/usr/bin/env python3

"""A tool for great evil... and fun! (But mostly evil)."""

import redis

def get_connection(host="10.28.59.172", port=6379, db=0):
    """Get a connection

    :param host: TODO
    :param port: TODO
    :param db: TODO
    :returns: TODO

    """
    conn = redis.StrictRedis(host=host, port=port, db=db)
    return conn


if __name__ == "__main__":
    conn = get_connection()
    val = conn.get('foo')
    print("Found: {}".format(val.decode('utf-8', 'ignore')) if val else "Not found :-(")
