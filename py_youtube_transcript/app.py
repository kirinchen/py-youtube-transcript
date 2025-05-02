# This is a sample Python script.
import argparse

from py_youtube_transcript import transcript_service


def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube video subtitles with optional timestamps.")
    parser.add_argument("-l", "--link", required=True, help="YouTube video link")
    parser.add_argument("-t", "--timestamp", action="store_true", help="Enable timestamps in subtitles")
    args = parser.parse_args()

    if not args.link:
        print("Error: You must provide a YouTube link using -l or --link.")
        return

    try:
        subtitles = transcript_service.get_subtitles_text_by_link(args.link, time_info_enable=args.timestamp)
        print(subtitles)
    except Exception as e:
        print(f"An error occurred: {e}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
