import unittest
import tempfile
import shutil
import os
from src.directory_creator import DirectoryCreator

class TestDirectoryCreator(unittest.TestCase):
    def setUp(self):
        # 一時ディレクトリを作成
        self.test_dir = tempfile.mkdtemp()
        self.structure_text = """your_project/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   └── database_manager.py
└── data/
    └── sample_data.csv
"""

    def tearDown(self):
        # 一時ディレクトリを削除
        shutil.rmtree(self.test_dir)

    def test_create_structure(self):
        creator = DirectoryCreator(self.structure_text, self.test_dir)
        creator.create_structure()

        # プロジェクトフォルダのパス
        project_root = os.path.join(self.test_dir, 'your_project')

        # 期待されるファイルとディレクトリのパス
        expected_paths = [
            os.path.join(project_root, 'app.py'),
            os.path.join(project_root, 'requirements.txt'),
            os.path.join(project_root, 'README.md'),
            os.path.join(project_root, 'src', '__init__.py'),
            os.path.join(project_root, 'src', 'database_manager.py'),
            os.path.join(project_root, 'data', 'sample_data.csv'),
        ]

        for path in expected_paths:
            self.assertTrue(os.path.exists(path), f"{path} が存在しません。")

if __name__ == '__main__':
    unittest.main()
