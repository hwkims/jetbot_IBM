Okay, I'll structure the content from the provided GitHub READMEs into the requested PowerPoint outline format. This combines information from the `jetbot.kr`, `jetbot_gemma`, and `jetbot_IBM` repositories.

---

**PPT 내용 정리 (JetBot AI 프로젝트)**

**01 프로젝트 개요 (Project Overview)**

*   **JetBot 소개:**
    *   NVIDIA Jetson Nano 기반의 저렴하고 교육적인 오픈소스 AI 로봇 플랫폼.
    *   특징: 합리적 가격 ($250 미만), 교육적 가치 (기본 로봇 공학 ~ 고급 AI), 쉬운 설정 (웹 브라우저 프로그래밍, Docker), 재미 (AI, 이미지 처리, 로봇 공학 탐험).
    *   [이미지: JetBot 사진 또는 로고]
*   **프로젝트 목표:**
    *   JetBot 플랫폼을 활용하여 다양한 AI 기반 로봇 제어 및 상호작용 시스템 개발 및 탐구.
    *   기본적인 AI 주행부터 최신 언어/비전 모델을 활용한 자율 제어까지 단계별 구현.
*   **수행 프로젝트 요약:**
    1.  **기본 AI 주행 (JetBot AI Following):**
        *   도로 따라가기 (Road Following)
        *   컵라면 따라가기 (Object Following - Cup Ramen)
    2.  **LLM 기반 제어 (JetBot Gemma Control):**
        *   로컬 LLM (Ollama + `gemma3:4b`)을 이용한 실시간 영상 분석 및 제어.
        *   음성 피드백 (Edge TTS - 한국어) 기능 구현.
    3.  **비전 LLM 기반 제어 (JetBot IBM Control):**
        *   비전 특화 LLM (Ollama + IBM `granite3.2-vision`) 활용.
        *   수동/자율/설명/커스텀 등 다양한 제어 모드 구현.
        *   Streamlit 기반 웹 인터페이스 및 추가 기능 (얼굴 특징 분석 데모).
*   **주요 사용 기술:**
    *   **하드웨어:** NVIDIA Jetson Nano, JetBot 키트
    *   **소프트웨어:** Python, FastAPI, Streamlit, WebSockets, HTML/CSS/JS, Docker
    *   **AI/ML:**
        *   딥러닝 (Road/Object Following 모델 - Hugging Face)
        *   대규모 언어 모델 (LLM): Ollama (`gemma3:4b`, IBM `granite3.2-vision`)
        *   음성 합성 (TTS): Edge TTS
        *   음성 인식: Web Speech API

**02 프로젝트 팀 구성 및 역할 (Team Composition and Roles)**

*   **팀 구성:** 본 프로젝트는 [hwkims]에 의해 기획 및 개발되었습니다. (Assuming it's an individual project based on the repo owner)
*   **수행 역할:**
    *   **기획:** JetBot 활용 아이디어 구상 및 단계별 프로젝트 목표 설정.
    *   **하드웨어:** JetBot 조립 및 설정.
    *   **소프트웨어 개발:**
        *   JetBot 제어 로직 구현 (Python).
        *   백엔드 API 개발 (FastAPI).
        *   프론트엔드 인터페이스 개발 (HTML/JS/CSS, Streamlit).
        *   실시간 통신 구현 (WebSockets).
    *   **AI 모델 활용:**
        *   데이터셋 수집/활용 (Road/Object Following).
        *   사전 훈련된 모델 활용 및 연동 (Hugging Face).
        *   Ollama 기반 LLM/Vision LLM 설정 및 API 연동.
        *   TTS/음성인식 API 연동.
    *   **테스트 및 디버깅:** 기능 테스트 및 오류 수정.
    *   **문서화 및 공유:** GitHub README 작성, 결과물 공유 (Hugging Face, YouTube).

**03 프로젝트 수행 절차 및 방법 (Project Execution Procedure and Method)**

*   **1단계: 환경 구축 및 기본 설정**
    *   JetBot 하드웨어 조립 및 Jetson Nano OS 설정.
    *   기본 JetBot 소프트웨어 설치 (SD 카드 이미지 또는 Docker 활용).
    *   네트워크 설정 (Wi-Fi 연결) 및 PC와의 통신 확인.
*   **2단계: 기본 AI 주행 기능 구현 (`jetbot.kr`)**
    *   주행 데이터 수집 (도로, 컵라면 이미지).
    *   AI 모델 학습 또는 사전 훈련된 모델 활용 (Hugging Face).
    *   Jupyter Notebook 예제를 참고하여 기본 동작(회피, 경로/객체 추종) 로직 구현.
    *   결과물(모델, 데이터셋) 공유.
*   **3단계: LLM 기반 제어 시스템 개발 (`jetbot_gemma`)**
    *   Ollama 설치 및 `gemma3:4b` 모델 다운로드.
    *   FastAPI 백엔드 서버 구축:
        *   JetBot 카메라 영상 스트리밍 수신.
        *   Ollama API 연동하여 영상 분석 요청.
        *   분석 결과 기반 JetBot 제어 명령 생성 (전진, 후진, 회전 등).
        *   WebSocket을 이용한 JetBot 및 웹 클라이언트와의 실시간 통신.
    *   Edge TTS 연동하여 분석 결과 음성 출력 (한국어).
    *   기본 웹 UI 개발 (HTML/JS/CSS)하여 제어 및 결과 확인.
*   **4단계: 비전 LLM 기반 고급 제어 시스템 개발 (`jetbot_IBM`)**
    *   Ollama에 IBM `granite3.2-vision` 모델 추가.
    *   FastAPI 백엔드 확장:
        *   다양한 제어 모드(수동, 자율, 설명, 커스텀) 로직 구현.
        *   비전 모델 특화 프롬프트 설계.
        *   Web Speech API 활용 음성 명령 인식 기능 추가 (선택 사항).
    *   Streamlit을 이용한 인터랙티브 웹 프론트엔드 개발:
        *   실시간 영상, 제어 버튼, 분석 결과 시각화.
    *   (부가 기능) 별도 Streamlit 앱으로 얼굴 특징 분석 데모 구현.
*   **5단계: 테스트, 개선 및 공유**
    *   각 기능별 단위 테스트 및 통합 테스트 수행.
    *   성능 측정 (응답 속도 등) 및 개선점 도출.
    *   GitHub 통해 소스 코드 및 README 문서 업데이트 및 공유.
    *   데모 영상 제작 및 공유 (YouTube Shorts).

**04 프로젝트 수행 결과 (Project Execution Results)**

*   **결과물 1: 기본 AI 주행 기능 (`jetbot.kr`)**
    *   JetBot 도로 따라가기 기능 구현 및 데모 영상 공개.
        *   [영상: JetBot AI Road Following (YouTube Short 링크)]
    *   JetBot 컵라면 따라가기 기능 구현 및 데모 영상 공개.
        *   [영상: JetBot Cup Ramen Following (YouTube Short 링크)]
    *   관련 데이터셋 및 학습 모델 Hugging Face 통해 공개.
        *   [링크/스크린샷: Hugging Face 데이터셋 및 모델 페이지]
*   **결과물 2: LLM 기반 제어 시스템 (`jetbot_gemma`)**
    *   `gemma3:4b` 모델을 활용, 실시간 영상 분석 기반 JetBot 제어 시스템 프로토타입 완성.
    *   웹 인터페이스를 통한 원격 제어 및 실시간 영상/분석 결과 확인 가능.
    *   상황 분석 결과를 한국어 음성(Edge TTS)으로 출력하는 기능 구현.
    *   [스크린샷: jetbot_gemma 웹 인터페이스]
*   **결과물 3: 비전 LLM 기반 고급 제어 시스템 (`jetbot_IBM`)**
    *   IBM `granite3.2-vision` 모델 활용, 향상된 비전 기반 제어 시스템 구축.
    *   수동 제어, 자율 주행, 장면 설명, 사용자 정의 명령 등 다중 모드 지원.
    *   Streamlit 기반의 시각적이고 인터랙티브한 제어 인터페이스 제공.
    *   [스크린샷: jetbot_IBM Streamlit 인터페이스]
    *   (부가 결과) 얼굴 특징 분석 Streamlit 데모 앱 개발.
*   **공통 결과:**
    *   모든 프로젝트 소스 코드 및 설정 방법 GitHub 통해 공개.
    *   JetBot을 활용한 다양한 최신 AI 기술 적용 사례 제시.

**05 자체 평가 의견 (Self-Assessment Opinion)**

*   **잘된 점 (Strengths):**
    *   저렴한 JetBot 플랫폼을 활용하여 최신 AI 기술(LLM, Vision LLM, TTS) 접목 성공.
    *   단계별 프로젝트 진행을 통해 AI 로봇 제어 기술 심층 학습 및 구현 경험 확보.
    *   FastAPI, WebSockets, Streamlit 등 최신 웹 기술을 활용하여 사용자 친화적인 인터페이스 및 실시간 제어 시스템 구축.
    *   오픈소스(Ollama, JetBot)를 적극 활용하여 개발 효율성 증대.
    *   결과물(코드, 모델, 영상)을 체계적으로 정리하고 공개하여 공유 및 재현 가능성 높임.
*   **어려웠던 점 및 개선할 점 (Weaknesses & Improvements):**
    *   **성능 한계:** Jetson Nano의 연산 능력 및 네트워크 환경에 따른 실시간 처리 지연(latency) 발생 가능성.
    *   **LLM 의존성 및 신뢰도:** LLM의 분석 결과가 항상 정확하거나 일관되지 않을 수 있으며, 이는 로봇 제어의 안정성에 영향. (예: 부정확한 장애물 인식, 예상치 못한 명령 생성)
    *   **장애물 회피 로직:** 현재 구현된 회피 로직이 단순하여(예: 'obstacle' 단어 감지 시 무조건 좌회전), LLM 출력을 더 정교하게 분석하여 상황에 맞는 회피 기동(좌/우/후진 등)이 필요함 (`jetbot_gemma` 개선점).
    *   **프롬프트 엔지니어링:** 원하는 로봇 행동을 유도하기 위한 효과적인 프롬프트 설계의 어려움.
    *   **UI/UX:** 사용자 경험을 더욱 향상시키기 위한 인터페이스 개선 필요.
    *   **에러 핸들링:** 예기치 않은 상황(통신 오류, 모델 응답 실패 등)에 대한 안정성 강화 필요.
*   **배운 점 (Lessons Learned):**
    *   엣지 디바이스(Jetson Nano) 환경에서 AI 모델 배포 및 최적화의 중요성 체감.
    *   하드웨어(로봇)-소프트웨어(제어 로직)-AI(분석/판단) 간의 유기적인 시스템 통합 능력 향상.
    *   LLM/Vision LLM의 로보틱스 분야 적용 가능성 및 현재 기술적 한계점 명확히 인지.
    *   오픈소스 커뮤니티 및 문서 활용 능력 증대.
*   **향후 계획 (Future Work):**
    *   정교한 장애물 회피 및 경로 계획 알고리즘 도입.
    *   특정 객체 인식 및 추적 기능 고도화.
    *   더 다양한 로봇 명령어 및 상호작용 시나리오 추가 (예: 음성 대화 기반 제어).
    *   성능 최적화 (모델 경량화, 코드 최적화 등).
    *   다양한 AI 모델 테스트 및 비교 평가.

---

이 내용을 바탕으로 각 슬라이드를 디자인하고, 필요에 따라 이미지, 영상, 코드 스니펫 등을 추가하면 효과적인 PPT를 만들 수 있습니다.

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
