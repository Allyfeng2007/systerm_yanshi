import streamlit as st
from streamlit_option_menu import option_menu #需要安装
from login import LoginPage
from index import Index
from news import News
from uploadfile import UploadFile
from cipin import WordFreq
from visual_relationship import Relation
#类一定要实例化后才能用
login_page = LoginPage()
index_page = Index()
news_page = News()

upload = UploadFile()
wordfreq = WordFreq()
relation = Relation()

st.set_page_config(page_title='Streamlit综合示例', page_icon='🔑')
st.session_state.setdefault('logged_in', False)
st.session_state.setdefault('nickname', '')
st.session_state.setdefault('page', '登录')

with st.sidebar:
    st.title('👀 Streamlit综合示例')
    if st.session_state['logged_in']:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f'😊 欢迎您，{st.session_state["nickname"]}!')
        with col2:
            if st.button('退出'):
                st.session_state['logged_in']=False
                st.session_state['nickname']=''
                st.session_state['page']='登录'
                st.rerun()
    else:
        st.write('😂 未登录')

    PAGES = ['登录', '首页', '新闻展示', '词频分析', '人物关系图']
    selected_page = option_menu(
        menu_title=None,
        options=PAGES,
        icons=["box-arrow-in-right", "house", "newspaper", "bar-chart", "diagram-3"],
        orientation="vertical"
    )

if selected_page == '登录':
    if st.session_state['logged_in']:
        st.success(f'👌已登录，当前用户是：{st.session_state["nickname"]}!')
    else:
        login_page.login()
else:
    if not st.session_state['logged_in']:
        st.warning('🟰请先登录')
        st.stop()
    if selected_page == '首页':
        index_page.index_show()
    elif selected_page == '新闻展示':
        st.title('新闻展示')
        news_page.news_show()
    elif selected_page == '词频分析':
        tab1, tab2= st.tabs(['📄文件上传', '📄词频显示'])
        with tab1:
            file_contents = upload.upload_file()
        with tab2:
            if file_contents:
                with st.spinner('正在分析中。。。。', show_time=True):
                    words = wordfreq.word_freq(file_contents)
                num = st.selectbox('显示前N个赐于', list(range(5, 100, 5)), 3)
                st.write(words[0:num+1])
            else:
                st.warning('请先上传文件')


    elif selected_page == '人物关系图':
        st.title('人物关系图')
        relation.draw_realtion()

# import streamlit as st
# from streamlit_option_menu import option_menu
#
# # 设置页面配置
# st.set_page_config(
#     page_title="我的个人博客",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
#
# # 模拟文章数据（按分类存储）
# blog_posts = {
#     "全部": [
#         {"title": "如何高效学习 Python？", "summary": "分享一些 Python 学习技巧与资源..."},
#         {"title": "Streamlit 入门指南", "summary": "从安装到第一个应用的完整教程..."},
#         {"title": "周末去了趟植物园", "summary": "记录一次轻松的户外休闲时光..."}
#     ],
#     "技术博客": [
#         {"title": "如何高效学习 Python？", "summary": "分享一些 Python 学习技巧与资源..."},
#         {"title": "Streamlit 入门指南", "summary": "从安装到第一个应用的完整教程..."}
#     ],
#     "生活随笔": [
#         {"title": "周末去了趟植物园", "summary": "记录一次轻松的户外休闲时光..."}
#     ],
# }
#
# # 定义菜单项和图标
# MENU_ITEMS = [
#     {"name": "博客首页", "icon": "house"},
#     {"name": "个人简介", "icon": "person-circle"},
#     {"name": "文章分类", "icon": "tags"}
# ]
#
# # 左侧边栏菜单
# with st.sidebar:
#     st.title('👀 个人博客日志')
#     selected_menu = option_menu(
#         menu_title=None,
#         options=[item["name"] for item in MENU_ITEMS],
#         icons=[item["icon"] for item in MENU_ITEMS],
#         orientation="vertical",
#         default_index=2  # 默认选中"博客首页"
#     )
#
# # 主内容区域
# st.header("我的个人博客")
# st.button("发布新文章")  # 仅作展示，无需真实功能
#
# # 根据选择的菜单项显示不同内容
# if selected_menu == "个人简介":
#     st.write("大家好，我是前端开发者小 A，热爱技术分享～")
#
# elif selected_menu == "文章分类":
#
#     selected_category = st.radio("选择分类：", list(blog_posts.keys()), horizontal=True)
#     st.write("大家好，我是前端开发者小 A，热爱技术分享～")
#
# elif selected_menu == "博客首页":
#     st.subheader("最新文章")
#     # 默认显示全部分类的文章
#     posts_to_show = blog_posts.get("全部", [])
#     if posts_to_show:
#         for post in posts_to_show:
#             with st.container():
#                 st.markdown(f"**{post['title']}**")
#                 st.caption(post['summary'])
#                 st.divider()
#     else:
#         st.info("暂无文章")