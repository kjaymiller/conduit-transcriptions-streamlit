import itertools
import streamlit as st
from db.search import similarity_search


def search(query:str):
    results = similarity_search(query)
    return results


def display_results(results):
    for grouped_results in itertools.groupby(results, lambda x: (x[0].metadata['title'], x[0].metadata['url'])):
        section = st.container()
        section.header(grouped_results[0][0])
        section.markdown(f"[Check out Episode]({grouped_results[0][1]})")
        section.subheader("Results in this Episode:")
        for result in grouped_results[1]:
            section.divider()
            section.write(result[0].page_content.lstrip(". "))

search_form = st.form('Search')
search_bar = search_form.text_input("Search for a topic")
search_submit = search_form.form_submit_button("Search")

if search_submit and search_bar:
    results = search(search_bar)
    display_results(results)

