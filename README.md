# py-youtube-transcript

`py-youtube-transcript` is a Python-based tool for fetching subtitles (transcripts) from YouTube videos. It provides options to retrieve subtitles with or without timestamps and supports command-line usage for quick access.

---

## Features

- Fetch subtitles from YouTube videos by providing a video URL.
- Optionally include timestamps in the subtitles.
- Easy-to-use command-line interface.
- Handles multiple YouTube URL formats.

---

## Requirements

- Python 3.8+
- Libraries: Install dependencies using `pip install -r requirements.txt`.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kirinchen/py-youtube-transcript.git
   cd py-youtube-transcript
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Command-Line Interface

Run the `app.py` script to fetch subtitles for a YouTube video:

```bash
python app.py -l <youtube_link> [-t]
```

### Arguments

- `-l` or `--link`: The YouTube video link (required).
- `-t` or `--timestamp`: Include timestamps in the subtitles (optional).

#### Example:

1. Fetch subtitles without timestamps:

   ```bash
   python app.py -l "https://www.youtube.com/watch?v=example"
   ```

2. Fetch subtitles with timestamps:

   ```bash
   python app.py -l "https://www.youtube.com/watch?v=example" -t
   ```

---

## API Usage

You can also use the tool programmatically by importing the `transcript_service` module:

```python
from py_youtube_transcript import transcript_service

link = "https://www.youtube.com/watch?v=example"
subtitles = transcript_service.get_subtitles_text_by_link(link, time_info_enable=True)
print(subtitles)
```

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

Developed by Kirin Chen.

For any inquiries, please contact [kirin.chen1001@gmail.com](mailto:kirin.chen1001@gmail.com).

