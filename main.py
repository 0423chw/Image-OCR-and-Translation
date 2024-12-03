from image_processing.ocr_extraction import extract_text_from_image
from text_translation.translate import translate_text
from text_translation.output_display import overlay_text_on_image

def main():
    # Step 1: 텍스트 추출
    input_image_path = "sample_image.jpg"  # 실제 이미지 경로로 변경 필요
    extracted_text = extract_text_from_image(input_image_path)
    print(f"Extracted Text:\n{extracted_text}")

    # Step 2: 텍스트 번역
    translated_text = translate_text(extracted_text, target_lang="ko")
    print(f"Translated Text:\n{translated_text}")

    # Step 3: 번역된 텍스트를 이미지에 오버레이
    output_image_path = "final_output_image.jpg"
    overlay_text_on_image(input_image_path, translated_text, output_image_path)

if __name__ == "__main__":
    main()
