import subprocess
import pytest
import os


def prepare_test_environment():

    def go_up_one_level(path):
        parent_dir = os.path.dirname(path)
        return os.path.abspath(os.path.join(parent_dir, os.pardir))

    current_path = os.path.abspath(__file__)
    root_directory = go_up_one_level(current_path)
    os.chdir(root_directory)


@pytest.mark.integration_test
def test_cli_execution():
    prepare_test_environment()
    samples_directory = os.path.join(os.getcwd(), "samples")
    samples = [
        f for f in os.listdir(samples_directory)
        if os.path.isfile(os.path.join(samples_directory, f))
    ]

    for sample in samples:
        command = [
            "python", "simpleclassifier", "-y",
            os.path.join("samples", sample)
        ]

        completed_process = subprocess.run(command,
                                           capture_output=True,
                                           text=True)
        assert completed_process.returncode == 0
