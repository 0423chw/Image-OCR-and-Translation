# Image-OCR-and-Translation

## 1. 프로젝트 구조

![image](https://github.com/user-attachments/assets/46c8bd79-fc27-4872-afc1-5c1b9f7b94d2)


## 2. 작업 내용 요약

### 2.1. 이미지 전처리
- OpenCV를 사용하여 **이미지에서 불필요한 노이즈 제거** 및 **텍스트 영역 강조**.
- 전처리 작업:
  - **흑백 변환 (Grayscale)**: 컬러 이미지를 흑백으로 변환.
  - **이진화 (Binarization)**: 텍스트 인식률을 높이기 위해 이미지 대비를 조정.
  - **이미지 회전 및 기하학적 변환**: 왜곡된 이미지를 정렬.

### 2.2. 텍스트 추출 (OCR)
- 전처리된 이미지를 **Tesseract OCR**로 입력하여 텍스트를 추출.
- 추출된 텍스트는 **구조화된 데이터**로 저장하여 번역 단계로 전달.
- Tesseract OCR 성능 최적화를 위해 환경 변수 설정 필요:
  ```bash
  # Tesseract 설치 후 경로 추가 (예: Windows)
  setx PATH "%PATH%;C:\Program Files\Tesseract-OCR"

### 2.3. 텍스트 번역
Hugging Face 번역 모델 (Helsinki-NLP/opus-mt-en-ko)을 사용하여 영어 텍스트를 한국어로 번역.
추출된 텍스트는 translate.py에서 번역 처리.
### 2.4. 번역된 텍스트 출력
이미지에 텍스트 오버레이:
번역된 텍스트를 이미지 위에 표시하고 결과 이미지를 저장.
텍스트 파일 출력:
번역된 텍스트를 .txt 파일로 저장.

## 3. 실행 방법
### 3.1. 설치
Python 3.8 이상을 설치합니다.
아래 명령어로 필요한 라이브러리를 설치합니다:
bash
코드 복사
pip install -r requirements.txt
### 3.2. 실행
OCR 및 번역 실행:
main.py를 실행하면, sample_image.jpg를 입력으로 받아 전처리, 텍스트 추출, 번역, 결과 저장을 수행합니다.
bash
코드 복사
python main.py
환경 변수 설정 (Tesseract 설치 후):
Tesseract OCR 경로를 환경 변수에 추가해야 정상 작동합니다.
### 4. 실행 결과
## 4.1. 입력
예제 입력 이미지: sample_image.jpg.
## 4.2. 출력
전처리된 이미지: processed_image.jpg 파일에 저장.
추출된 텍스트: extracted_text.txt 파일에 저장.
번역된 텍스트: translated_text.txt 파일에 저장.
번역된 텍스트가 포함된 이미지: output_image.jpg 파일에 저장.
### 5. 역할 및 브랜치 관리
## 5.1. 역할 1: 이미지 전처리 및 텍스트 추출 담당
이미지 전처리:
OpenCV를 사용하여 노이즈 제거, 흑백 변환, 이진화 등 전처리 작업 수행.
텍스트 추출:Tesseract OCR을 사용하여 텍스트 인식 및 추출.
GitHub 관리:image_processing 브랜치에서 작업 후, Pull Request로 main 브랜치에 병합.
## 5.2. 역할 2: 텍스트 번역 및 결과 출력 담당
텍스트 번역:Hugging Face 번역 모델을 사용하여 텍스트 번역 (예: 영어 → 한국어).
결과 출력:번역된 텍스트를 이미지에 오버레이하거나, 텍스트 파일로 저장.
GitHub 관리:text_translation 브랜치에서 작업 후, Pull Request로 main 브랜치에 병합.
### 6. 공통 GitHub 역할
리더:브랜치 관리 및 Pull Request 병합 담당.
최종적으로 README.md 작성 및 GitHub 리포지토리 설정.
팀원:각자 작업한 코드 커밋 및 푸시.
커밋 메시지를 구체적으로 작성:
예: "Add OCR extraction functionality"
### 7. 예제 커밋 메시지
"Add preprocess.py for image preprocessing"
"Update translate.py to handle multi-language translation"
"Fix bug in output_display.py related to image overlay"
### 8. 추가 참고
Tesseract 설치: Tesseract GitHub
Hugging Face 번역 모델: Helsinki-NLP on Hugging Face
yaml


