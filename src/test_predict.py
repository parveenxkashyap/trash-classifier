import argparse
import requests


def main():
    parser = argparse.ArgumentParser(description="Send an image to a /predict HTTP endpoint.")
    parser.add_argument("--url", default="http://127.0.0.1:5000/predict")
    parser.add_argument("--file", required=True, help="Path to image file")
    args = parser.parse_args()

    with open(args.file, "rb") as f:
        files = {"file": f}
        response = requests.post(args.url, files=files)

    print("Status:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    main()
