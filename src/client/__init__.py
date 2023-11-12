from .client import start_client


def main(args=None):
    import argparse
    import logging
    import asyncio

    parser = argparse.ArgumentParser(
        prog=__name__,
        description="Connect to an AIDA websocket server.",
    )
    parser.add_argument("-p", "--port", type=int, default=6342)
    parser.add_argument("-a", "--address", type=str, default="localhost")
    parser.add_argument("-v", "--verbose", action="count", default=0)

    options = parser.parse_args(args)

    if options.verbose == 1:
        log_level = logging.INFO
    elif options.verbose >= 2:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)
    uri = f"ws://{options.address}:{options.port}"
    asyncio.get_event_loop().run_until_complete(start_client(uri))


if __name__ == "__main__":
    import sys

    rc = 1
    try:
        main()
        rc = 0
    except Exception as e:
        print("Error: %s" % e, file=sys.stderr)
    sys.exit(rc)
