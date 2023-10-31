from .server import start_server
from .ai import AI


def main(args=None):
    import argparse
    import logging
    import asyncio
    import pathlib

    parser = argparse.ArgumentParser(
        prog=__name__,
        description="Start the websocket server for clients to connect to.",
    )
    parser.add_argument(
        "-m",
        "--model-path",
        type=pathlib.Path,
        required=True,
        help="Path to Llama-2 huggingface model",
    )
    parser.add_argument("-p", "--port", type=int, default=6342)
    parser.add_argument("-a", "--address", type=str, default="localhost")
    parser.add_argument("-v", "--verbose", action="count", default=0)

    options = parser.parse_args(args)

    if options.verbose == 1:
        log_level = logging.INFO
    elif options.vervose >= 2:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)
    # AI.start(options.model_path)
    asyncio.run(start_server(options.address, options.port))


if __name__ == "__main__":
    import sys

    rc = 1
    try:
        main()
        rc = 0
    except Exception as e:
        print("Error: %s" % e, file=sys.stderr)
    sys.exit(rc)
