# jetbot_IBM![image](https://github.com/user-attachments/assets/1962fb04-a450-4c31-b265-72109e456200)
![image](https://github.com/user-attachments/assets/a3be2781-f62a-4fb3-9a9b-987a418208e6)

jetbot_IBM granite3.2-vision control![image](https://github.com/user-attachments/assets/741a829f-0a7a-4527-a79d-93d6ce902ba9)
![image](https://github.com/user-attachments/assets/7fdc8b0b-1b2a-44ef-ba66-c94366e23ab4)

![image](https://github.com/user-attachments/assets/99c5753a-e924-454f-a2b4-3110405e5843)
![image](https://github.com/user-attachments/assets/9e852845-ae11-4831-ba01-3cd6f332cc70)

![image](https://github.com/user-attachments/assets/dcf4e0e0-e4b6-4798-af3f-98d98b5b65b5)
![image](https://github.com/user-attachments/assets/8fffbc99-aab0-4984-a7cd-3b9e483d3b6c)
![image](https://github.com/user-attachments/assets/1f4f13eb-c240-4677-a9a8-8960c0ca7922)
 https://ollama.com/library/granite3.2-vision
 https://jetbot.org/master/index.html
# JetBot Control with Vision and Ollama

This project provides a comprehensive system for controlling a JetBot robot using both direct commands and autonomous, vision-based navigation powered by [Ollama](https://ollama.ai/).  It leverages FastAPI for the backend API, WebSockets for real-time communication, and edge-tts for text-to-speech feedback.  The system supports a Streamlit-based web interface for manual control and visualization of the autonomous process.

## Features

*   **Direct Control:** Issue basic movement commands (forward, backward, left, right, stop, dance) to the JetBot via a web interface.
*   **Vision-Based Autonomous Navigation:**  Utilize the Ollama large language model (specifically `granite3.2-vision`) for image analysis and autonomous decision-making. The JetBot can navigate, avoid obstacles, and describe its environment.
*   **Real-time Image Streaming:** View a live video stream from the JetBot's camera in the web interface.
*   **Text-to-Speech (TTS) Feedback:**  Receive spoken feedback from the JetBot, describing its actions and observations, using `edge-tts`.
*   **Custom Commands:**  Define custom actions based on the vision model's analysis of the scene.
*   **Multiple Control Modes:** Switch between manual control, descriptive mode (where the JetBot describes what it sees), custom command mode, and full autonomous mode.
* **Physiognomy Analysis:** Includes a Streamlit application demonstrating how to analyze a person's face and classify different characteristics.
*   **FastAPI Backend:**  A robust and efficient backend API built with FastAPI.
*   **WebSocket Communication:**  Real-time communication between the web interface, the backend server, and the JetBot.
*   **Streamlit Frontend:**  An interactive web interface built with Streamlit.

## Project Structure

The project consists of the following main components:

*   **`app.py` (FastAPI Backend):**  This is the core of the system.  It handles:
    *   WebSocket connections to both the JetBot and the web client.
    *   Communication with the Ollama API for vision processing.
    *   Text-to-speech generation using `edge-tts`.
    *   Processing commands from the client and sending them to the JetBot.
    *   Serving the static files for the web interface.
*   **`static/` (Web Interface):** Contains the HTML, CSS, and JavaScript files for the basic web interface that interacts with the FastAPI backend.
*   **`physiognomy_app.py` (Streamlit App):** A separate Streamlit application demonstrating the use of Ollama for facial analysis.
*  **`requirements.txt`:** Contains the python dependencies.

## Prerequisites

1.  **JetBot:** A fully assembled and configured JetBot robot. You must have the JetBot's WebSocket server running on the JetBot itself (see JetBot documentation for details).  The default WebSocket URL is `ws://192.168.137.181:8766`.  You may need to adjust this based on your JetBot's IP address.
2.  **Ollama:**  Ollama must be installed and running. Download and install Ollama from [https://ollama.ai/](https://ollama.ai/).  You'll need to pull the `granite3.2-vision` model:
    ```bash
    ollama pull granite3.2-vision
    ```
3.  **Python 3.7+:** This project requires Python 3.7 or higher.
4.  **Dependencies:** Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
5. **Edge-TTS:** `edge-tts` is used for voice generation. It is included in the requirements.txt.

## Setup and Running

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/hwkims/jetbot_IBM.git
    cd jetbot_IBM
    ```

2.  **Configure (if necessary):**
    *   **`app.py`:** If your Ollama server or JetBot WebSocket URL are different from the defaults, modify the `OLLAMA_HOST` and `JETBOT_WEBSOCKET_URL` variables in `app.py`.
    *   **`physiognomy_app.py`:** If your Ollama server is different from the defaults, modify the `OLLAMA_HOST` in `physiognomy_app.py`.

3.  **Start the FastAPI Server:**
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```
    This will start the backend server, making the web interface available at `http://localhost:8000`.  The `--host 0.0.0.0` makes the server accessible from other devices on your network.

4.  **Start the Streamlit App (Optional - for physiognomy analysis):**
    In a *separate* terminal, navigate to the project directory and run:
    ```bash
    streamlit run physiognomy_app.py
    ```    This will start the Streamlit application, typically at `http://localhost:8501`.

5. **Connect your Jetbot** Ensure your Jetbot is powered on, and the Jetbot websocket server is running.

6.  **Access the Web Interface:** Open a web browser and go to `http://localhost:8000` (or the appropriate address if you changed the host/port).

## Usage

### Main Web Interface (`http://localhost:8000`)

The main interface provides buttons for direct control (Forward, Backward, Left, Right, Stop, Dance) and input fields for more complex interactions:

*   **Direct Control Buttons:** These send immediate commands to the JetBot.
*   **Iterations:** Specifies how many times a command should be repeated.
*   **Text Input:** Used for custom prompts and text input for Ollama.
*   **Describe:** Sends the current camera image to Ollama and displays/speaks a description of the scene.
*   **Custom:** Sends the current camera image and the text prompt to Ollama, then executes the returned commands.
*   **Autonomous:** Enters autonomous mode, where the JetBot repeatedly analyzes the scene and navigates based on Ollama's output.

### Physiognomy App (`http://localhost:8501`)

The Streamlit app allows you to either upload an image or use your webcam to capture an image of a face.  It then sends the image to Ollama with a prompt to analyze 32 facial features and provide a physiognomy reading in JSON format. The results are displayed, including a radar chart of the facial features.

## Troubleshooting

*   **JetBot Not Connecting:**
    *   Ensure the JetBot is powered on and connected to the same network as your computer.
    *   Verify that the JetBot's WebSocket server is running.
    *   Double-check the `JETBOT_WEBSOCKET_URL` in `app.py`.
*   **Ollama Not Responding:**
    *   Make sure Ollama is running.
    *   Verify that you have pulled the `granite3.2-vision` model (`ollama pull granite3.2-vision`).
    *   Check the `OLLAMA_HOST` variable in `app.py` and `physiognomy_app.py`.
*   **Web Interface Not Working:**
    *   Ensure the FastAPI server is running (`uvicorn app:app ...`).
    *   Check your browser's developer console for any JavaScript errors.
*   **TTS Not Working**
    * Ensure you have a working internet connection for `edge-tts` to download the required voice data the first time it runs.
* **Streamlit Webcam Issues:**
    * Modern browsers often require secure contexts (HTTPS) for webcam access. If you are experiencing trouble with the webcam in the Streamlit app, you might need to set up HTTPS or use a workaround like `streamlit run physiognomy_app.py --server.enableCORS=false --server.enableXsrfProtection=false`.  **Note:** Disabling CORS and XSRF protection is generally not recommended for production environments, but may be acceptable for local development and testing.  A better solution for production would be to set up a proper HTTPS server.

## Contributing

Contributions are welcome!  Please feel free to submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
# JetBot Control 🤖

![JetBot](https://via.placeholder.com/720x300.png?text=JetBot+Image)  
*JetBot in action - Replace this with an actual image URL or path.*

**JetBot Control**은 NVIDIA Jetson Nano 기반의 교육용 AI 로봇 JetBot을 위한 제어 시스템입니다. IBM의 `granite3.2-vision` 모델을 활용하여 이미지 분석 및 자율 주행을 지원하며, 수동 버튼 조작과 사용자 정의 명령도 가능합니다. 이 프로젝트는 로봇 공학, AI, 비전 처리에 관심 있는 학생과 개발자들에게 실습 경험을 제공합니다.

---

## 주요 기능

- **수동 제어**: 버튼으로 "Forward", "Backward", "Left", "Right", "Stop", "Dance" 동작을 직접 실행.
- **비전 기반 자율 주행**: `granite3.2-vision`을 사용해 실시간 이미지 분석 후 자율 주행.
- **설명 기능**: 카메라 피드를 분석해 장면 설명 제공 (예: "오른쪽에 테이블, 앞에 열린 경로").
- **사용자 정의 명령**: 텍스트 입력 또는 음성으로 자유로운 명령 실행 (예: "spin around").
- **음성 인식**: 한국어(`ko-KR`) 지원으로 "안녕" 같은 명령 처리.
- **반복 실행**: 모든 명령에 대해 반복 횟수 설정 가능.

---

## 기술 스택

- **하드웨어**: NVIDIA Jetson Nano, JetBot 플랫폼
- **백엔드**: FastAPI (Python), WebSocket 통신
- **비전 모델**: IBM `granite3.2-vision` (Ollama 호스팅)
- **프론트엔드**: HTML/CSS/JavaScript (현대적 UI)
- **음성 처리**: Web Speech API, Edge TTS (Jenny Neural 음성)
- **로봇 제어**: JetBot Python 라이브러리

---

## 설치 방법

### 요구 사항
- NVIDIA Jetson Nano 및 JetBot 하드웨어
- Python 3.6+ (JetBot용), Python 3.8+ (FastAPI용)
- Ollama 0.5.13+ (`granite3.2-vision` 설치)
- `ding.mp3` 파일 (`static/` 디렉토리에 추가)

### JetBot 설정
1. JetBot에 접속:
   ```bash
   ssh jetbot@192.168.137.181
   ```
2. 저장소 클론:
   ```bash
   git clone https://github.com/hwkims/jetbot_IBM.git
   cd jetbot_IBM
   ```
3. 종속성 설치:
   ```bash
   pip install jetbot
   ```
4. JetBot 실행:
   ```bash
   python3.6 jetbot.py
   ```

### 서버 설정
1. 로컬 머신에서 저장소 클론:
   ```bash
   git clone https://github.com/hwkims/jetbot_IBM.git
   cd jetbot_IBM
   ```
2. 가상 환경 생성 및 활성화:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. 종속성 설치:
   ```bash
   pip install fastapi uvicorn httpx edge-tts websockets
   ```
4. Ollama 실행 및 모델 설치:
   ```bash
   ollama serve
   ollama run granite3.2-vision
   ```
5. 서버 실행:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### 웹 인터페이스
- 브라우저에서 `http://localhost:8000` 열기.

---

## 사용법

1. **수동 제어**:
   - 버튼 클릭: "Forward", "Backward", "Left", "Right", "Stop", "Dance".
   - "Iterations" 입력으로 반복 횟수 설정.

2. **비전 설명**:
   - "Describe" 버튼 클릭 → 현재 장면 설명 출력 및 TTS 재생.

3. **사용자 정의 명령**:
   - 텍스트 입력: "spin around" 입력 후 "Execute" 클릭.
   - 음성: "Voice" 버튼 클릭 후 "안녕" 또는 "go forward" 말하기.

4. **자율 주행**:
   - "Iterations" 설정 후 "Autonomous" 클릭 → 비전 기반 주행 시작.

---

## 예제 명령

- **수동**: "Forward" 버튼 → 1초간 전진.
- **설명**: "Describe" → "오른쪽에 의자, 앞에 열린 공간입니다."
- **커스텀**: "spin around" → 오른쪽으로 2초 회전.
- **자율**: Iterations 3 → 이미지 분석 후 3번 주행 (예: "forward", "left", "stop").

---

## 기여하기

1. 이슈 제출: 버그나 제안은 [Issues](https://github.com/hwkims/jetbot_IBM/issues)에서.
2. 풀 리퀘스트: 포크 후 브랜치 생성, 변경 후 PR 제출.

---

## 라이선스

이 프로젝트는 [MIT License](LICENSE) 하에 배포됩니다.

---

## 연락처

- **GitHub**: [hwkims](https://github.com/hwkims)
- **Email**: hwkims@example.com (실제 이메일로 교체 필요)

---

이 리드미는 GitHub Markdown 형식으로 작성되었으며, `hwkims/jetbot_IBM` 저장소의 `README.md` 파일로 바로 사용할 수 있습니다. 이미지 URL(`https://via.placeholder.com/...`)은 임시로 넣은 것이니, 실제 JetBot 사진으로 교체하세요. 추가 수정이나 요청 있으면 말씀해주세요!
