import os
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen

from lxml import etree
from youtube_transcript_api import YouTubeTranscriptApi


def video_id(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    - https://youtube.com/shorts/J26zFgFwA1o?si=vtNJtvt86zJaKSN3
    """
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
        if query.path.startswith('/shorts'):
            return query.path.split('/')[2]
    # fail?
    return None


def get_subtitles_text(yt_id, time_info_enable=False) -> str:
    """
    Fetches subtitles text for a YouTube video by ID.

    Args:
        yt_id (str): YouTube video ID.
        time_info_enable (bool): If True, include timestamps in the subtitles.

    Returns:
        str: Subtitles text with or without timestamps.
    """
    try:
        transcripts = YouTubeTranscriptApi.list_transcripts(yt_id)
        languages = [s.language_code for s in transcripts]
        if len(languages) == 0:
            return ""
        subtitles = YouTubeTranscriptApi.get_transcript(yt_id, languages=[languages[0]])
        text = ""
        for i in subtitles:
            if time_info_enable:
                start_time = i['start']
                duration = i['duration']
                text += f"[{start_time:.2f}s - {start_time + duration:.2f}s] {i['text']}" + os.linesep
            else:
                text += i['text'] + os.linesep
        return text
    except Exception as e:
        e_ans = f'yt_id:{yt_id} Error: {e}'
        print(e_ans)
        return e_ans


def get_subtitles_text_by_link(link, time_info_enable=False) -> str:
    yt_id = video_id(link)
    print(yt_id)
    return get_subtitles_text(yt_id, time_info_enable)


def get_title(yt_id) -> str:
    try:
        myparser = etree.HTMLParser(encoding="utf-8")
        youtube = etree.HTML(urlopen("http://www.youtube.com/watch?v=" + yt_id).read(), parser=myparser)
        video_title_e_list = youtube.xpath("//title")
        video_title = video_title_e_list[0].text
        return video_title
    except Exception as e:
        e_ans = f'yt_id:{yt_id} Error: {e}'
        print(e_ans)
        return e_ans


def get_title_by_link(link) -> str:
    yt_id = video_id(link)
    print(f'get_title_by_link yt_id:{yt_id}')
    return get_title(yt_id)


def get_yt_info_by_link(link, time_info_enable=False) -> dict:
    yt_id = video_id(link)
    print(f'yt_id:{yt_id}')
    return {
        "title": get_title(yt_id),
        "subtitles": get_subtitles_text(yt_id, time_info_enable),
        "yt_id": yt_id
    }


if __name__ == '__main__':
    # Test cases
    vid = video_id("https://www.youtube.com/watch?v=iBfQTnA2n2s&list=PLOXw6I10VTv9lin5AzsHAHCTrC7BdVdEM&index=5")
    print(vid)
    print(get_title(vid))
    print(get_subtitles_text(vid, time_info_enable=True))
