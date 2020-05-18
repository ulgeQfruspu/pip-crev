def setup_parser(parent_parser):
    parser = parent_parser.add_parser("current", help="Show your current ID")
    parser.set_defaults(method=_execute)


def _execute(*arg1, **kwargs):
    print("very: ", arg1, kwargs)
