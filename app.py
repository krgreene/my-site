# Streamlit application to display my personal/professional projects.

import streamlit as st

st.set_page_config(
    page_title='My profile',
    page_icon=':vulcan_salute:'
)

st.header('My profile')

with st.container(border=True):

    st.subheader('About me')
    with st.container(border=False, horizontal=True, width='content'):
        st.write('Khalil Greene')
        st.image('assets/flag-barbados.png', width=32)
        st.caption('🇧🇧')

    st.write('Postgrduate Researcher at the University of Southampton')
    st.write('Skills: Full-stack development, mapping, GIS')
    st.write('[https://orcid.org/0009-0008-0115-6812](https://orcid.org/0009-0008-0115-6812)')
    st.space('small')

    with st.container(border=False, horizontal=True, width='stretch', vertical_alignment='center', gap='large'):
        st.image('assets/python-logo-only.svg', width=32)
        st.image('assets/Primary_Horizontal_Lockup_Full_Color.svg', width=120)
        st.image('assets/react-dev-logo.png', width=32)
        st.image('assets/qgis-nl-logo.png', width=32)

st.subheader('Sample projects')

with st.container(border=True):
    st.write('[Sargassum Sub-regional Outlook Bulletin](https://sargassum-outlook.web.app/)')
    st.caption('Forecasting invasive seaweed')
    st.caption('IDL to Python, NoSQL, React')

    with st.expander(label='Preview', expanded=False):
        st.iframe(
            src='https://sargassum-outlook.web.app/',
            width='stretch',
            height=600
    )

with st.container(border=True):
    st.write('[Barbados Map Tools](https://map-tools.web.app/)')
    st.caption('Map Reading training aid')
    st.caption('React, Leaflet')

    with st.expander(label='Preview', expanded=False):
        st.iframe(
            src='https://map-tools.web.app/',
            width='stretch',
            height=600
    )

with st.container(border=True):
    st.write('[Geo-informatics for Agriculture](https://krgreene.github.io/geo-info/)')
    st.caption('Geo-informatics training manual')
    st.caption('Markdown, Just the Docs, QGIS')

    with st.expander(label='Preview', expanded=False):
        st.iframe(
            src='https://krgreene.github.io/geo-info/',
            width='stretch',
            height=600
    )