---
title: "Relay Sim code released on GitHub"
date: 2026-02-03
draft: false
description: "Code for the Relay Simulator released on Github"
tags: ["RelaySim"]

---

I've finally worked my coded into a state where I think it's ready for it's first **BETA** release.
It can be found here:

Repository: https://github.com/pjchick/Relay-Simulator

Issues: https://github.com/pjchick/Relay-Simulator/issues

I am not a great coder and have been learning as I go with this project so any help, assistance or pointers greatly received!

### Prerequisites

- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pjchick/Relay-Simulator-III.git
   cd "Relay Simulator"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   
   **Windows (PowerShell):**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   **Linux/macOS:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r relay_simulator/requirements.txt
   ```

### Running the Application

**GUI Designer Mode:**
```bash
python relay_simulator/app.py
```

### Building Standalone Executable

To create a standalone Windows executable:

```bash
python build_exe.py
```

The executable will be created in `dist/RelaySimulator.exe`

See `BUILD_INSTRUCTIONS.md` in the repo for more details.
