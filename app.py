import streamlit as st
import os
from src.directory_creator import DirectoryCreator

def main():
    st.title("プロジェクトディレクトリ生成アプリ")

    st.write("以下の形式でディレクトリ構成を入力してください。")
    st.code("""your_project/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   └── database_manager.py
""")

    structure_text = st.text_area("ディレクトリ構成を入力", height=200)
    root_path = st.text_input("プロジェクトを生成するフォルダを選択（親フォルダ）", value=os.getcwd())

    if st.button("実行"):
        if not structure_text.strip():
            st.error("ディレクトリ構成を入力してください。")
        elif not os.path.isdir(root_path):
            st.error("有効なフォルダパスを入力してください。")
        else:
            creator = DirectoryCreator(structure_text, root_path)
            try:
                creator.create_structure()
                st.success("ディレクトリとファイルの生成が完了しました。")
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
