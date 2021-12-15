#!/usr/bin/python
# -*- coding: latin-1 -*-

"""Console script for gogoportefollioopt."""
import argparse
import sys
from jobs.ingestion import Ingestion

def main():
    """Console script for gogoportefollioopt."""
    parser = argparse.ArgumentParser()
    #parser.add_argument('_', nargs='*')
    parser.add_argument("-c", "--config", help=" fichier de configuration",required=True)
    parser.add_argument("-d", "--data", help=" symbols des stocks à récuperer",required=True)
    args = parser.parse_args()

    print("Arguments: " + str(args))
    ingestion = Ingestion(args)
    ingestion.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

