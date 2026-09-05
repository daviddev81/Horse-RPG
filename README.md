# Horse RPG

A text-based role-playing game built in Python. The program manages player data, currency transactions, and terminal configurations to simulate property management and route selection in a console environment.

---

## Technical Features

*   **Data Structures:** Custom horse profiles tracking three distinct scalar metrics (Strength, Speed, Health) using conditional layout loops.
*   **Color Formatting:** Implements standard ANSI terminal escape codes for structured text colorization without external dependencies.
*   **Console Geometry Check:** Uses Python's `shutil` library to verify active terminal column and line counts before rendering large structural text assets.
*   **Serialization Engine:** Features a global input handler that intercepts inputs. Entering `save` anywhere invokes a json-based writing routine to serialize data to a localized `savegame.json` file.
*   **Multi-line Arrays:** Includes structural multi-line raw string assets (`r"""`) to render matrix-style maps and objects.

---

## Prerequisites

The project requires a standard **Python 3** installation.

*   **Windows:** Install Python 3 via the Microsoft Store or directly from python.org.
*   **macOS / Linux:** Install via terminal packet managers (`brew install python` or `sudo apt install python3`(Debian based systems) `sudo pacman -S python3`(Arch based systems).

---

## Installation & Execution

### 1. Download Files
Execute the following git command within your workspace directory to clone the project source files:

```bash
git clone https://github.com
```

### 2. Change Directory
```bash
cd Horse-RPG
```

### 3. Run Program
Run the source file through the target interpreter:
```bash
python horserpg.py
```
*(On macOS or Linux systems, invoke `python3 horserpg.py` instead).*

---

## Interface Commands

Submit the following strings when prompted by the application loop:

*   **Entity Evaluation:** Input `joey`, `hammer`, or `oldey` to load individual horse values.
*   **System Action:** Input `save` at any variable prompt to trigger the localized state backup mechanism.
*   **Branch Execution:** Input `mc`, `oc`, or `or` to redirect the sequence execution path to a specific geographical route array.

> 📝 **Constraint Notice:** A terminal window dimensions configuration of at least 120 columns by 40 lines is required to allow rendering of graphic matrices.

---

## License

This software project is licensed under the parameters of the **GNU General Public License v3.0**. Review the localized repository `LICENSE` file for strict parameters.
