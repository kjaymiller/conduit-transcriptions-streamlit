import streamlit
import pathlib
import frontmatter


streamlit.title("Conduit Transcriptions")
streamlit.session_state["episode_title"] = "Choose and episode to begin"
streamlit.session_state["description"] = "Select an episode from the sidebar to view its transcription."
streamlit.session_state["episode_pub_date"] = ""
streamlit.session_state["episode_url"] = ""

episode_header_image, episode_header_content = streamlit.columns([1,3])
episode_header_image.image("assets/conduit_artwork.jpg", caption="Conduit Podcast Artwork", use_column_width=True)

streamlit.divider()

transcription_container = streamlit.container()

def set_transcription_data():
    """Set the transcription content."""
    streamlit.session_state["episode_title"] = episode["title"]
    streamlit.session_state["episode_pub_date"] = episode["pub_date"]
    streamlit.session_state["episode_url"] = f"[Listen to the episode]({episode['url']})"
    streamlit.session_state["description"] = episode["description"]
    streamlit.session_state["transcription"] = episode.content
    
    with episode_header_content:
        streamlit.header(streamlit.session_state["episode_title"])
        streamlit.markdown("\n\n".join([streamlit.session_state["episode_pub_date"], streamlit.session_state["episode_url"], streamlit.session_state["description"]]))
    
    transcription_container.empty()
    transcription_container.write(streamlit.session_state["transcription"])


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


