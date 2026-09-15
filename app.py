# Streamlit application to display my personal/professional projects.

import streamlit as st

st.set_page_config(
    page_title='My profile',
    page_icon=':vulcan_salute:'
)

st.header('My profile')

with st.container(border=False, horizontal=True, width='content'):
    st.subheader('About me')
    st.image('assets/flag-barbados.png', width=32)
    st.caption('🇧🇧')
st.write('Postgrduate Researcher at the University of Southampton')
st.write('Skills: Full-stack development, mapping, data visualisation, GIS')
st.write('[https://orcid.org/0009-0008-0115-6812](https://orcid.org/0009-0008-0115-6812)')

st.subheader('Sample projects')

with st.container(border=True):
    st.write('[Sargassum Sub-regional Outlook Bulletin](https://sargassum-outlook.web.app/)')
    st.caption('Forecasting invasive seaweed')
    st.caption('IDL to Python, NoSQL, React')

with st.container(border=True):
    st.write('[Barbados Map Tools](https://map-tools.web.app/)')
    st.caption('Map Reading training aid')
    st.caption('React, Leaflet')

with st.container(border=True):
    st.write('[Geo-informatics for Agriculture](https://krgreene.github.io/geo-info/)')
    st.caption('Geo-informatics training manual')
    st.caption('Markdown, Just the Docs, QGIS')