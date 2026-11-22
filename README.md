# CampusDesk - MIT ADT College Enquiry Chatbot

GenAI mini project, Problem Statement 11.

| Student | Details |
| --- | --- |
| Name | Amrut Sachin Shelke |
| Class | LYCORE-1 |
| Roll number | 11 |
| Enrollment number | ADT23SOCB0122 |

## Problem statement

Admission offices receive repeated questions about courses, fees and admissions. This project provides a chat interface that sends a college information sheet and the conversation history to a local language model. Its system prompt instructs the model to answer from the sheet, cite section IDs, and refer unanswered questions to the admissions office.

This is an academic prototype, not an official MIT ADT University service. The selected information in `college_info.txt` was compiled from official university pages on 22 November 2026. It is a limited snapshot; confirm current information with admissions.

## Features

- Streamlit chat UI using `st.chat_input` and `st.chat_message`.
- Conversation history in `st.session_state`, with a new-conversation button.
- Local Qwen2.5-1.5B-Instruct GGUF inference through llama-cpp-python.
- Course, fee, admission-process and contact information in a readable text file.
- Source-section citation instructions and explicit handling of unknown information.
- Downloadable conversation and information sheet.
- No API key or model training required. Internet is needed for initial installation and model download.

## Setup on Windows

Install Python 3.12 (64-bit) and ensure `python` is available in your terminal. Open PowerShell in this project folder:

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

Setup creates a virtual environment, installs the dependencies, and downloads the official Qwen GGUF (approximately 1.1 GB). Allow several GB of free disk space and RAM. On subsequent runs, the model works locally without network access.

Start the app:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.address 127.0.0.1 --server.port 8501
```

Alternatively, double-click `Start-Chatbot.cmd` after setup. Open http://127.0.0.1:8501 in your browser.

Manual installation:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --only-binary=llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu -r requirements.txt
.\.venv\Scripts\python.exe download_model.py
```

## Implementation

```text
User question + recent history
             |
System rules + college_info.txt
             |
Local Qwen language model
             |
Answer with source-section references
             |
Streamlit chat + session history
```

`chatbot.py` contains the exact system prompt, input validation, history construction, model loading and inference. `app.py` renders the chat and manages the session. `download_model.py` downloads the official model into `models/`. To use another trusted compatible GGUF, set the `COLLEGE_MODEL_PATH` environment variable to its local path.

## Sample checks

Use `sample_inputs.json` for the manual evaluation plan. The cases cover courses, fee figures and category/year, applications, unknown information, follow-up history and attempts to override the source instructions. Evaluate the actual responses against the source sheet; model-generated citations alone do not prove correctness.

## Verification status and limitations

The Python files and prompt construction have been checked locally. End-to-end LLM generation and UI screenshots have **not** been verified: Windows Application Control blocked the native `llama.dll` on the development machine (WinError 4551). The app therefore requires a machine where the official llama-cpp-python runtime is permitted. Do not disable security controls to run this project; consult the device administrator or use an appropriate development machine.

Prompt instructions reduce unsupported answers but do not guarantee factual grounding or resistance to prompt injection. This prototype has no automatic claim verifier. The sheet does not include all courses, hostel fees, deadlines or live seat availability. History is temporary, limited to recent messages for model context, and lost when the session ends. CPU inference speed depends on the computer. A procedure report, actual output screenshots and completed model evaluation are separate submission deliverables and are not included in this source package.

## Official information sources

- [University contact information](https://mituniversity.ac.in/contact-us)
- [Programme fee schedule](https://mituniversity.ac.in/Admissions/admission_program_fees/)
- [Admission application procedure](https://mituniversity.ac.in/Admissions/mitadt_admission_process)
- [School of Engineering and Sciences programmes and eligibility](https://mituniversity.ac.in/academics/faculty/faculty-of-engineering/MIT-School-of-Engineering-and-Sciences/programs-offered/)

## Model and software references

- [Official Qwen2.5-1.5B-Instruct GGUF model](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF)
- [llama-cpp-python installation documentation](https://github.com/abetlen/llama-cpp-python)
- [Streamlit conversational-app documentation](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps)

Model and dependency licenses belong to their respective owners. The model weights, virtual environment and secrets are excluded from this repository.

## Project repository

https://github.com/Amrut1228/GENAI_project-LLM-Model-PS_11-

## Project files

- `app.py`: Streamlit interface and session history.
- `chatbot.py`: system prompt, information-sheet loader and model inference.
- `college_info.txt`: editable MIT ADT information and official source links.
- `download_model.py`: downloads the official local model.
- `requirements.txt`: application dependencies.
- `sample_inputs.json`: eight manual evaluation cases.
- `setup.ps1`: Windows setup.
- `Start-Chatbot.cmd`: Windows launcher.
- `.gitignore`: excludes secrets, model weights and local environments.
- `README.md`: setup, architecture and verification status.

Keep `college_info.txt` beside `chatbot.py`. The app reads this file each time Streamlit reruns; edit the sheet to update the knowledge source. The information is no longer embedded in the Python code.
