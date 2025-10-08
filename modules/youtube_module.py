from youtube_transcript_api import YouTubeTranscriptApi
from modules.summarizer import summarize_text

def get_transcript(video_id):
    """Get transcript of YouTube video"""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t['text'] for t in transcript_list])
        return text
    except Exception as e:
        return str(e)

def summarize_youtube(video_id):
    transcript = get_transcript(video_id)
    summary = summarize_text(transcript)
    return summary

# Example usage
if __name__ == "__main__":
    video_id = "VIDEO_ID_HERE"
    print(summarize_youtube(video_id))
