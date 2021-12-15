"""Main module."""

from jobs.ingestion import Ingestion
if __name__ == '__main__':

    ingestion = Ingestion({})
    ingestion.run()
