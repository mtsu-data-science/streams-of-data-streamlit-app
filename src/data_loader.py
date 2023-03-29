import awswrangler as wr


def read_data_from_s3(table_s3_path):
    """read_subreddit_data_from_s3 returns a dataframe stored in s3 for analysis
    Args:
        subreddit_name (str): The name of the subreddit
        file_name (str): A distinct filename
    Returns:
        Pandas DataFrame: The dataframe stored in s3
    """

    return wr.s3.read_parquet(
        path=table_s3_path,
        dataset=True,
    )
