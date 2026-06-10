import streamlit as st
from database import DataBase

class LoginPage:
    def login(self):
        db = DataBase()
        st.subheader("🔐 用户登录")

        username = st.text_input("用户名", placeholder="电话号码")
        password = st.text_input("密码", type="password")

        if st.button("登录"):
            if not username or not password:
                st.warning("请输入用户名和密码！")
            else:
                result = db.login_user(username, password)#[('1', '1', '张三')]
                if result:
                    st.session_state["logged_in"] = True
                    st.session_state["nickname"] = result[0][2]
                    st.session_state["page"] = "首页"
                    st.success(f"登录成功，欢迎 {result[0][2]}!")
                    db.qk()
                    st.rerun()  # 停止当前执行，从脚本第一行重新运行但同时保持 st.session_state 的所有变量不变，让 UI 立即更新。也可以理解为强制跳转
                else:
                    st.error("用户名或密码错误")
