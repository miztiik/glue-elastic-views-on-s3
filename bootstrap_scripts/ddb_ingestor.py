#!/usr/bin/env python3

import json
import logging
import os
from decimal import Decimal

import boto3


class GlobalArgs:
    OWNER = "Mystique"
    ENVIRONMENT = "production"
    MODULE_NAME = "eventbridge_data_consumer"
    MOVIES_DATA_FILE = "../sample_data/movie_data_01.json"
    DDB_TABLE_NAME = "elasticViewsMoviesTable_2021"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


def set_logging(lv=GlobalArgs.LOG_LEVEL):
    """ Helper to enable logging """
    logging.basicConfig(level=lv)
    logger = logging.getLogger()
    logger.setLevel(lv)
    return logger


LOG = set_logging()
ddb_res = boto3.resource("dynamodb")


def _get_movies_data(f_name):
    with open(f_name) as f:
        data = json.load(f, parse_float=Decimal)
    return data


def put_movie(tbl_name, year, title, m_info):
    table = ddb_res.Table(tbl_name)
    response = table.put_item(
        Item={
            "year": year,
            "title": title,
            "info": m_info
        }
    )
    return response


if __name__ == "__main__":
    m_data = _get_movies_data(GlobalArgs.MOVIES_DATA_FILE)

    print(f'{{"total_movies":{len(m_data)}}}')
    cnt = 0
    for idx, _i in enumerate(m_data, start=1):
        try:
            put_movie(GlobalArgs.DDB_TABLE_NAME,
                      _i["year"], _i["title"], _i["info"])
            cnt += 1
            if cnt % 500 == 0:
                print(f"insert_status: {idx} Count:  {cnt}")
        except Exception as e:
            print(f"ERROR:{str(e)}")
    print("Insert Successful")


"""
    {
        "year": 2013,
        "title": "Rush",
        "info": {
            "directors": ["Ron Howard"],
            "release_date": "2013-09-02T00:00:00Z",
            "rating": 8.3,
            "genres": [
                "Action",
                "Biography",
                "Drama",
                "Sport"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX400_.jpg",
            "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
            "rank": 2,
            "running_time_secs": 7380,
            "actors": [
                "Daniel Bruhl",
                "Chris Hemsworth",
                "Olivia Wilde"
            ]
        }
    }
"""
