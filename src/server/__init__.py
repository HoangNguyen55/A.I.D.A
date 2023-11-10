from .server import start_server
from .ai import AI


def main(args=None):
    from .config import (
        get_default_config_folder,
        get_default_data_folder,
        generate_config,
    )
    import configargparse
    import logging
    import asyncio
    import pathlib
    import os

    default_config = os.path.join(get_default_config_folder(), "config.ini")
    default_db = os.path.join(get_default_data_folder(), "aida_db.sql")
    parser = configargparse.ArgumentParser(
        default_config_files=[default_config],
        prog=__name__,
        description="start the websocket server for clients to connect to.",
    )

    parser.add_argument(
        "-m",
        "--model-path",
        type=pathlib.Path,
        required=True,
        help="path to Llama-2 huggingface model",
    )

    parser.add_argument(
        "-c",
        "--config",
        is_config_file=True,
        help=f"path to the configuration file, default to '{default_config}'",
    )

    parser.add_argument(
        "--db-path",
        help=f"path to where the sql database file should be located, default to '{default_db}'",
        default=default_db,
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help=f"port number of the server, default to '6342'",
        default=6342,
    )

    parser.add_argument(
        "-a",
        "--host-address",
        type=str,
        help=f"host of the server, default to 'localhost'",
        default="localhost",
    )

    parser.add_argument(
        "--inference-on-startup",
        action="store_true",
        help=f"start the AI when starting the server",
    )

    parser.add_argument(
        "--auto-approve-signup",
        action="store_true",
        help=f"automatically approve anyone who sign up",
    )

    parser.add_argument(
        "--generate-config",
        action="store_true",
        help=f"generate configuration file at destination configured with --config, default to '{default_config}'",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        help="each 'v' increase logging level, WARN -> INFO -> DEBUG, default to WARN",
        default=0,
    )

    options = parser.parse_args(args)

    if options.generate_config:
        generate_config(options)

    if options.verbose == 1:
        log_level = logging.INFO
    elif options.verbose >= 2:
        log_level = logging.DEBUG
    else:
        log_level = logging.WARNING

    logging.basicConfig(level=log_level)
    logging.debug(options)
    if options.start_ai:
        AI.start(options.model_path)

    asyncio.run(start_server(options))


if __name__ == "__main__":
    import sys

    rc = 1
    try:
        main()
        rc = 0
    except Exception as e:
        print("Error: %s" % e, file=sys.stderr)
    sys.exit(rc)
