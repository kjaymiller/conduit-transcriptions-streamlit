import streamlit
import pathlib
import frontmatter


streamlit.title("Conduit Transcriptions")

episode_header_image, episode_header_content = streamlit.columns([1,3])
episode_header_image.image("assets/conduit_artwork.jpg", caption="Conduit Podcast Artwork", use_column_width=True)


streamlit.divider()

transcription_container = streamlit.container()

def set_transcription_data():
    """Set the transcription content."""
    pass

with streamlit.sidebar:
    episode = streamlit.radio(
        "Select an episode",
        sorted(
            [frontmatter.loads(path.read_text()) for path in pathlib.Path("transcripts").iterdir()],
            key=lambda episode: int(episode["title"].split(": ")[0]),
            reverse=True,
        ),
        format_func=lambda episode: episode["title"],
        on_change=set_transcription_data,
    )


with episode_header_content:
    streamlit.header(episode["title"] + f" [:link:]({episode['url']})")
    streamlit.text(episode["pub_date"])
    streamlit.caption(f'{episode["description"]}')

transcription_container.write(episode.content)
