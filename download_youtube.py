"""Download YouTube transcripts for SEO research videos."""

from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

OUTPUT_DIR = Path(__file__).resolve().parent / "research" / "youtube-transcripts"

VIDEOS = [
    {
        "id": "VNXjG1OZxPw",
        "title": "How to do B2B Content Strategy & SEO: Bernard Huang (Clearscope Office Hours)",
        "channel": "Clearscope",
        "url": "https://www.youtube.com/watch?v=VNXjG1OZxPw",
        "filename": "clearscope-b2b-content-strategy-seo.md",
    },
    {
        "id": "ZytMamXMG0M",
        "title": "How to Rank SEO Content in the Era of Generative AI: Bernard Huang (Clearscope)",
        "channel": "Clearscope",
        "url": "https://www.youtube.com/watch?v=ZytMamXMG0M",
        "filename": "clearscope-rank-seo-content-generative-ai.md",
    },
    {
        "id": "K_Y9MYiW0Go",
        "title": "The Future of Authority Sites... (Ep. 337)",
        "channel": "Authority Hacker Podcast",
        "url": "https://www.youtube.com/watch?v=K_Y9MYiW0Go",
        "filename": "authority-hacker-future-of-authority-sites.md",
    },
]


def build_markdown(video: dict, transcript_text: str, language_code: str) -> str:
    return "\n".join(
        [
            f"# {video['title']}",
            "",
            f"- **Channel:** {video['channel']}",
            f"- **Video ID:** {video['id']}",
            f"- **URL:** {video['url']}",
            f"- **Transcript language:** {language_code}",
            "",
            "## Transcript",
            "",
            transcript_text,
            "",
        ]
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    api = YouTubeTranscriptApi()

    for video in VIDEOS:
        print(f"Fetching transcript for {video['id']}...")
        transcript = api.fetch(video["id"], languages=["en", "en-US"])
        transcript_text = " ".join(snippet.text for snippet in transcript)
        output_path = OUTPUT_DIR / video["filename"]
        output_path.write_text(
            build_markdown(video, transcript_text, transcript.language_code),
            encoding="utf-8",
        )
        print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
