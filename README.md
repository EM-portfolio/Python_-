### プロジェクトの概要
職業訓練校の卒業制作として、Webスクレイピングを活用した画像収集ツール を作成しました。
指定したWebページの画像を自動で取得し、ローカルに保存できるWebアプリケーションです。

目的：Webスクレイピングの技術を習得し、実践的なスキルを身につけることです。

#### 使用技術
- バックエンド: Python（Flask）
- フロントエンド: HTML, CSS, JS
- スクレイピング: BeautifulSoup, Requests
- 画像処理: PIL（Pillow）
- データ保存: OSライブラリを使用  


### セットアップ手順

1. **リポジトリをクローン**
- git clone https://github.com/EM-portfolio/project-name.git

2. **必要なライブラリインストール**
- pip install -r requirements.txt


### 工夫したポイント（技術的にこだわった点、苦労した点など）

1. **画像URLの処理を工夫**
   - `src` が相対パスだった場合、`urllib.parse.urljoin(URL, src)` を使い、正しいURLに変換  
   - 任意の画像拡張子に合わせて取得できるように調整しました。

2. **サーバー負荷を考慮**
   - `time.sleep(0.5)` を入れて、スクレイピングの間隔を調整（サイトに負担をかけないように配慮）  