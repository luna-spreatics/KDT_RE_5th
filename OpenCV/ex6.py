import cv2

img = cv2.imread('OpenCV/images/iu.jpg')

if img is None:
    print('파일을 찾을 수 없습니다.')
else:
    h, w, _ = img.shape

    # 1. 1/2 축소
    small_img = cv2.resize(img, (w // 2, h // 2))

    # 2. 좌우 반전
    flipped_img = cv2.flip(small_img, 1)

    # 3. 우하단 배치
    result = img.copy()
    sh, sw, _ = flipped_img.shape

    # 시작점부터 이미지 높이만큼만 영역 지정
    result[h//2: h//2 + sh, w//2: w//2 + sw] = flipped_img

    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
