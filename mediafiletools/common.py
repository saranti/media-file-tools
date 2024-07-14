import os
from tabulate import tabulate


EXTENSIONS = ('.mp4', '.mkv', '.avi', 'ts', 'mov', '.wmv', '.flv', '.webm',
              '.m4v', '.mpg', '.3gp', '.3g2', '.ogv', '.vob', '.rm', '.rmvb',
              '.asf', '.m2ts', '.mxf', '.divx', '.xvid', '.f4v', '.mpe',
              '.mpe', '.drc', '.qt', '.svi', '.bik')


def save_to_file(df, filepath=None, output_type=None, fname=None):
    """
    Helper function to save the resulting DataFrame to
    a file or to print to console.

    Parameters
    ----------
    df: DataFrame
        The resulting DataFrame of the movie database.
    filepath: str, optional
        The directory path for the output csv file.
        Default is /home/user.
    output_type: str, default `txt`
        Choose the resulting filetype/output. Valid types are `txt`,
        `csv`, `console`.
    fname: str
        The filename for the output movie database.
    """
    if output_type == "txt":
        if is_file(filepath):
            fpath = filepath
        else:
            fpath = os.path.join(filepath, fname + ".txt")
        # Convert the dataframe to a left-aligned table string using tabulate
        table_str = _tabulate_df(df)
        with open(fpath, "w", encoding="utf-8") as txt:
            txt.write(table_str)
    elif output_type == "csv":
        if is_file(filepath):
            df.to_csv(filepath, index=False)
        else:
            df.to_csv(os.path.join(filepath, fname + ".csv"), index=False)
    elif output_type == "console":
        table_str = _tabulate_df(df)
        print(table_str)
    else:
        raise ValueError(
            f"{output_type} is not a valid output type. Valid "
            f"keywords are 'txt', 'csv' or 'console'."
        )


def _tabulate_df(df):
    table_str = tabulate(df, headers='keys', tablefmt='plain', stralign='left',
                         numalign='left', showindex=False)
    # Add a space before each item for readability
    return '\n'.join(' ' + line for line in table_str.split('\n'))


def is_file(filepath):
    # Check if the path has a file extension.
    _, ext = os.path.splitext(filepath)
    if ext:
        # Check if the parent directory exists.
        parent_dir = os.path.dirname(filepath)
        return os.path.isdir(parent_dir)
    return False
