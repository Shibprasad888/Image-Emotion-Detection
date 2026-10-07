import cv2
from deepface import DeepFace

image_path = "emo_img.avif"
image = cv2.imread(image_path)
if image is None:
    print("Please provide a valid image path. Line 5")
    exit()

try:
    result = DeepFace.analyze(
        img_path=image_path,
        actions=["emotion"],
        enforce_detection=False
    )

    if isinstance(result, list):
        result = result[0]

    dominant_emotion = result["dominant_emotion"]
    emotions = result["emotion"]

    print("\nDetected Emotion:")
    print("------------------------")
    print("Dominant Emotion:", dominant_emotion)

    print("\nConfidence:")
    for emotion, score in emotions.items():
        print(f"{emotion:<10}: {score:.2f}%")

    # Display on Image
    text = f"Emotion: {dominant_emotion}"

    cv2.putText(
        image,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Emotion Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print("Analysis failed.")
    print(e)