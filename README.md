# プロジェクトディレクトリ生成アプリ

このアプリケーションは、ChatGPTで提案されたプロジェクトのディレクトリ構成を基に、実際のフォルダとファイルを作成するツールです。Streamlitを使用してユーザーフレンドリーなインターフェースを提供し、簡単にプロジェクトの雛形を生成できます。

## 特徴

* **ディレクトリ構成の入力**: ユーザーがテキスト形式でディレクトリ構成を入力できます。
* **自動生成**: 指定された構成に基づいて、フォルダと空のファイルを自動生成します。
* **GUIの提供**: Streamlitを使用して直感的なユーザーインターフェースを提供します。
* **ユニットテスト**: コードの信頼性を確保するためのユニットテストが含まれています。

## 目次

* [前提条件](#%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6)
* [インストール](#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
* [使い方](#%E4%BD%BF%E3%81%84%E6%96%B9)
* [テスト](#%E3%83%86%E3%82%B9%E3%83%88)
* [ディレクトリ構成](#%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E6%A7%8B%E6%88%90)
* [注意事項](#%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A0%85)
* [ライセンス](#%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9)
* [貢献](#%E8%B2%A2%E7%8C%AE)
* [作者](#%E4%BD%9C%E8%80%85)

## 前提条件

* Python 3.7以上がインストールされていること

## インストール

1. **リポジトリをクローンまたはダウンロード**

   ```bash
   git clone https://github.com/your_username/project_generator.git
   cd project_generator
   ```

2. **仮想環境の作成（オプショナル）**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合は venv\Scripts\activate
   ```

3. **必要なパッケージをインストール**

   ```bash
   pip install -r requirements.txt
   ```

## 使い方

1. **アプリケーションの起動**

   ```bash
   streamlit run app.py
   ```

2. **ブラウザでの操作**

   アプリケーションが自動的にブラウザで開きます。以下の手順で操作してください。

   * **ディレクトリ構成の入力**

     テキストエリアに以下の形式でディレクトリ構成を入力します。

     ```markdown
     your_project/
     ├── app.py
     ├── requirements.txt
     ├── README.md
     ├── src/
     │   ├── __init__.py
     │   └── database_manager.py
     └── tests/
         └── test_database_manager.py
     ```

   * **プロジェクトを生成するフォルダの選択**

     プロジェクト名フォルダが作成される**親フォルダ**のパスを入力します。デフォルトでは現在の作業ディレクトリが設定されています。

   * **実行**

     「実行」ボタンをクリックすると、指定したフォルダ内にディレクトリとファイルが生成されます。

## テスト

ユニットテストを実行して、コードが正しく動作することを確認できます。

```bash
python -m unittest discover tests
```

## ディレクトリ構成

```markdown
project_generator/
├── app.py
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   └── directory_creator.py
└── tests/
    ├── __init__.py
    └── test_directory_creator.py
```

* **app.py**: Streamlitアプリケーションのエントリーポイント。
* **requirements.txt**: 必要なパッケージのリスト。
* **README.md**: プロジェクトの説明書（このファイル）。
* **src/directory\_creator.py**: ディレクトリとファイルを生成するロジックを含むモジュール。
* **tests/**: ユニットテスト用のディレクトリ。

## 注意事項

* **インデントとツリー構造の記号**

  * ディレクトリ構成を入力する際、**インデントはツリー構造の記号（`│`、`├`、`└`）の数で表現**されます。
  * インデントや記号が正しくない場合、期待通りのディレクトリ構造が生成されない可能性があります。

* **フォルダとファイルの判定**

  * ファイル名にドット（`.`）が含まれない場合、**フォルダと認識**される可能性があります。
  * フォルダであることを明示したい場合は、名前の末尾に`/`を追加してください。

* **権限とパス**

  * 指定したフォルダに対して**書き込み権限**が必要です。
  * パスの指定に誤りがないことを確認してください。

## ライセンス

このプロジェクトは [MIT License]() の下で公開されています。

## 貢献

バグ報告や機能の提案、プルリクエストを歓迎します。貢献方法については、以下の手順に従ってください。

1. リポジトリをフォークします。

2. 新しいブランチを作成します。

   ```bash
   git checkout -b feature/your_feature
   ```

3. 変更をコミットします。

   ```bash
   git commit -m "Add your message"
   ```

4. リモートブランチにプッシュします。

   ```bash
   git push origin feature/your_feature
   ```

5. プルリクエストを作成します。

## 作者

* **名前**: *stemtazoo*
* **メール**: *[stem.sci.tech.eng.math.2013@gmail.com]()*
* **GitHub**: [stemtazoo](https://github.com/stemtazoo)