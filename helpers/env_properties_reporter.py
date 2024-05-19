import os
from typing import ClassVar

import pytest


class EnvironmentSaver:

    """Saves environment variables to xml and properties files.
    https://docs.qameta.io/allure/#_environment.
    """

    list_of_env_vars: ClassVar[list[str]] = [
        "E2E_BRANCH",
        "BASE_URL",
        "GITHUB_ACTOR",
        "RUNNER_OS",
        "RERUNS",
        "E2E_SHA",
        "BROWSER",
        "PYTEST_XDIST_WORKER_COUNT",
    ]

    def __init__(self, prop_filename="environment.properties"):
        self.prop_filename = prop_filename

    def save_to_properties(self):
        """Saves environment variables to environment.properties file.

        Returns: None
        -------

        """
        with open(self.prop_filename, "w") as f:
            for env_var in self.list_of_env_vars:
                value = os.getenv(env_var, None)
                if value:
                    f.write(f"{env_var}={value}\n")


@pytest.fixture(scope="session", autouse=True)
def save_env_to_alluredir(request):
    """Saves environment variables to environment.properties file.

    Returns: None
    -------

    """
    allure_dir = request.config.getoption("--alluredir")

    if allure_dir:  # if --alluredir is specified in pytest command
        prop_file_path = os.path.join(allure_dir, "environment.properties")

        saver = EnvironmentSaver(prop_filename=prop_file_path)
        saver.save_to_properties()
