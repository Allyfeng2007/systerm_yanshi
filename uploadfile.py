import os
import uuid
import streamlit as st


class UploadFile:
    def upload_file(self):
        save_dir = 'uploads'
        os.makedirs(save_dir, exist_ok=True)  # 如果该目录已经存在，也不会报错
        with st.expander('📝 上传需要处理的文件'):
            uploaded = st.file_uploader('选择一个文件', type=['txt'])

            if uploaded is not None:
                # 构建唯一文件名避免覆盖
                filename = f'{uuid.uuid4().hex}_{uploaded.name}'
                file_path = os.path.join(save_dir, filename)

                # 保存文件到本地
                with open(file_path, 'wb') as f:
                    f.write(uploaded.getbuffer())

                st.success(f'📌 文件已成功保存到: {file_path}')

                text = uploaded.getvalue().decode('utf-8')
                return text
