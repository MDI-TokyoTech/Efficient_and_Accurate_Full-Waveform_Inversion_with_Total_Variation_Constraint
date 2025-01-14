import subprocess
from pathlib import Path
import requests

from invoke import task

project_root_path = Path(__file__).parent.resolve()



@task
def download_salt_and_overthrust_models(c):
    # ref: https://wiki.seg.org/wiki/SEG/EAGE_Salt_and_Overthrust_Models
    url = "https://s3.amazonaws.com/open.source.geoscience/open_data/seg_eage_models_cd/salt_and_overthrust_models.tar.gz"

    response = requests.get(url, stream=True)
    response.raise_for_status()

    path = project_root_path.joinpath("datasets/salt_and_overthrust_models.tar.gz")

    with open(temp_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    pass


@task
def format(c):
    format_commands = [
        f"isort ./src ./lib",
        f"black ./src ./lib"
    ]

    for cmd in format_commands:
        subprocess.run(cmd, shell=True, cwd=project_root_path)
