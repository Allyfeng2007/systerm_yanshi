import streamlit as st
import database

class News:
    def news_show(self):
        db = database.DataBase()
        news_list = db.select_news()  # 返回一个 list，每项是 tuple
        db.qk()
        # 获取所有类别去重
        categories = sorted(set([item[5] for item in news_list]))
        category = st.selectbox("请选择新闻类别",categories,index=None,placeholder="请选择新闻类别")

        if category is not None:
            st.markdown(
                f'<h3 style="text-align:center; font-weight:bold">{category}新闻</h3>',
                unsafe_allow_html=True,
            )

            # 根据用户选择的类别过滤数据并展示
            filtered_news = [item for item in news_list if item[5] == category]
            for item in filtered_news:
                _id, title, summary, content, time, category = item
                with st.expander(f"{title}  🕒 {time}"):
                    st.write("📝 摘要：", summary)
                    st.write("📄 正文：", content)
