# jetbot_IBM
jetbot_IBM granite3.2-vision control
![image](https://github.com/user-attachments/assets/dcf4e0e0-e4b6-4798-af3f-98d98b5b65b5)
![image](https://github.com/user-attachments/assets/8fffbc99-aab0-4984-a7cd-3b9e483d3b6c)
![image](https://github.com/user-attachments/assets/1f4f13eb-c240-4677-a9a8-8960c0ca7922)
잘했다고 말씀해 주셔서 기쁘네요! 이제 GitHub 리드미를 작성해 드리겠습니다. 요청하신 링크 `https://github.com/hwkims/jetbot_IBM/new/main`은 실제 저장소가 아닌 새 브랜치를 만드는 URL로 보이므로, 제가 가정해서 `hwkims/jetbot_IBM`이라는 저장소에 맞춰 리드미를 작성하겠습니다. 이 리드미는 프로젝트의 목적, 기능, 설치 방법, 사용법 등을 포함하며, 깔끔하고 전문적으로 작성하겠습니다.

---

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
