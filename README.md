# TensorFlow-ML-Zero-to-Hero
Introduction to Machine Learning with TensorFlow

## Setting Up Machine
### Setting up WSL
- Firstly, we need to set up WSL(Windows Subsystem for Linux) on our machine.
  - Navigate to *Powershell* and run the command:
    ```Powershell
    wsl --install
    ```
  > Note: By default, the installed Linux distribution will be Ubuntu. This can be changed using the -d flag.
- Since I will be using *Visual Studio Code(VSCode)*, I then add the [WSL](ms-vscode-remote.remote-wsl) extension
  - This allows us to run a command using `CTRL` + `SHIFT` + `P`
    - Type `WSL`
    - Select *`WSL: Connect to WSL`*
  - This has just opened VS Code in an Ubuntu(WSL) Distribution.

### Setting up Python and Package Installer 
- Now we also want to install *Python* so download and install it.
- Once in *VSCode* if we open a terminal and type we should hopfully see the output: 
  ```bash
  # python3 --version
  Python 3.12.3
  ```
- Let's install the [Python](ms-python.python) extension in *VSCode* and then select an Interpretor for *Python*
- To install Python Packages we need *PIP(Pip installs packages)* so we run the command:
  ```bash
  apt install python3-pip
  ```
### Setting up Virtual Environment
- To run a Virtual Environment on *WSL* we need to install *Python-venv* so we run the command:
  ```bash
  apt install python3-venv
  ```
  - Then we create a Virtural Environtment using:
    ```bash
    python3 -m venv myenv
    ```
  - In the Project explorer you should now see a new folder called `myenv`
  - To activate this *venv* we run:
    ```bash
    source myenv/bin/activate
    ```
  - We should now see our terminal prefixed with `(myenv)` meaning that we are working within the Virtual Environment now
 
## Working within the Venv(Virtual Environment)
### Installing TensorFlow
- In order to use packages in the project we need to use *PIP* to install them on the *Venv* so we run:
  ```(venv)bash
  pip install tensorflow
  ```
- At this point we should be pretty much set up to run the project! 
  