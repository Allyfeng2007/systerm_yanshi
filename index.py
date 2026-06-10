import streamlit as st


class Index:
    def index_show(self):
        choice = st.radio('选择欣赏方式',['🎶音频欣赏', '📽️视频欣赏'], horizontal=True)

        if choice == '🎶音频欣赏':
           # st.title('《登鹳雀楼》朗诵音频')
            st.markdown(
                """
                <h4 style="text-align:center">《登鹳雀楼》朗诵音频</h4>
                """,
                unsafe_allow_html=True
            )
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image('sucai/a.jpg', caption='王之涣 · 登鹳雀楼', width=120)

            with col2:
                #st.write('白日依山尽，黄河入海流。欲穷千里目，更上一层楼。')
                st.markdown(
                    """
                    <p style="font-size:18px; font-weight:bold; line-height:1.8; margin-top:50px;">
                    白日依山尽，黄河入海流。<br>
                    欲穷千里目，更上一层楼。
                    </p>
                    """,
                    unsafe_allow_html=True
                )

            with open('sucai/gushi.mp3', 'rb') as f:
                audio_bytes = f.read()
            st.audio(audio_bytes, format='audio/mp3', loop=True)

        else:  # "📽️视频欣赏"
            st.title('《登鹳雀楼》视频欣赏')
            with open('sucai/video.mp4', 'rb') as f:
                video_bytes = f.read()
            st.video(video_bytes, format='video/mp4', loop=True)