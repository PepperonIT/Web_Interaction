# Installation of Web_Interaction \<tool x>
 
## Linux/Debian

## Usage

If you are not using the development container, you will need to install the required dependencies first. Otherwise you can skip to step 4.

**Step 1.** Install [Python 2.7](https://www.python.org/download/releases/2.7/).

**Step 2.** Start by installing the required modules

```bash
pip install -r requirements.txt
```

**Step 3.** Download and extract the [Pepper SDK](PepperSDK.md). TODO

**Step 4.** Start the application with `python ./src/main.py`

## Ask Pepper

In order to ask pepper questions you firstly need to chose which function to call in the main.py file.

```bash
python ./src/main.py
```

Pepper will prompt you to ask a question. Watch the terminal in order to follow the process. For the time being just stop the process once done by:

```bash
CTRL+C
```

## Development

### Dependencies

All dependencies are managed by pip and are listed in the `requirements.txt` and `requirements-dev.txt` file. The development dependencies are only required if you want to make changes to the code. To install the dependencies, including the development dependencies, run:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

The `requirements.txt` file contains the dependencies required to launch the application and the `requirements-dev.txt` file contains tools used during development.

If a new dependency is added, make sure to update the correct requirement file with name and version of the new dependency. The same applies when removing a dependency. To automatically update the requirements file `requirements.txt`, run:

```bash
pipreqs
```

### Development Container _(optional)_

This repository includes a Visual Studio Code Dev Containers / GitHub Codespaces development container.

- For [Dev Containers](https://aka.ms/vscode-remote/download/containers), use the **Dev Containers: Clone Repository in Container Volume...** command which creates a Docker volume for better disk I/O on macOS and Windows.
  - If you already have VS Code and Docker installed, you can also click [here](vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/D7017E/Rock-Paper-Scissors) to get started. This will cause VS Code to automatically install the Dev Containers extension if needed, clone the source code into a container volume, and spin up a dev container for use.
- For Codespaces, install the [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) extension in VS Code, and use the **Codespaces: Create New Codespace** command.

See the [development container README](.devcontainer/README.md) for more information.