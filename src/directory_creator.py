from typing import List, Optional, Tuple
import os
import re

import streamlit as st

class DirectoryCreator:
    """
    指定されたディレクトリ構成から、フォルダとファイルを生成するクラス。
    """

    def __init__(self, structure_text: str, root_path: str):
        self.structure_text = structure_text
        self.root_path = root_path
        self.project_name: Optional[str] = None

    def create_structure(self):
        lines = self.structure_text.strip().splitlines()
        path_stack: List[str] = []

        for idx, line in enumerate(lines):
            if not line.strip():
                continue  # 空行をスキップ

            # インデントとコンテンツを解析
            parsed = self._parse_line(line)
            if parsed is None:
                continue  # 無効な行をスキップ

            indent, content, is_dir = parsed
            st.write(parsed)

            # スタックを更新
            while len(path_stack) > indent:
                path_stack.pop()
            path_stack.append(content)

            # 現在のパスを構築
            st.write(path_stack)
            current_path = os.path.join(self.root_path, *path_stack)
            st.write(current_path)
            self._create_path(current_path, is_dir)

            # プロジェクト名を取得
            if idx == 0:
                self.project_name = content

    def _parse_line(self, line: str) -> Optional[Tuple[int, str, bool]]:
        """
        行を解析してインデントレベル、コンテンツ、フォルダかファイルかを取得。

        Returns:
            (indent, content, is_dir)
        """
        # 行頭のツリー構造の記号をカウント
        indent_match = re.match(r'^(│   )*([├└]── )?(.*)', line)
        if not indent_match:
            return None

        # インデントレベルを計算
        indent = line.count('│') + line.count('├') + line.count('└')
        #indent = line.count('│   ')

        # ツリー構造の記号を除去してコンテンツを取得
        content = indent_match.group(3).strip()

        # フォルダかファイルかを判定
        if content.endswith('/'):
            is_dir = True
            content = content.rstrip('/')
        elif '.' not in content and indent > 0:
            is_dir = True
        else:
            is_dir = False

        return indent, content, is_dir

    def _create_path(self, path: str, is_dir: bool):
        try:
            if is_dir:
                os.makedirs(path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, 'w', encoding='utf-8') as f:
                    pass  # 空のファイルを作成
        except Exception as e:
            print(f"エラーが発生しました: {e}")
