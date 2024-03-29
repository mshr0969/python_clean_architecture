# Pythonでクリーンアーキテクチャを理解する

## 概要

クリーンアーキテクチャについての簡単なメモ。基本的には[Clean Architecture 達人に学ぶソフトウェアの構造と設計](https://www.kadokawa.co.jp/product/301806000678/)に沿っている。

#### 以下の図が有名
![クリーンアーキテクチャ](clean_architecture.jpg)

## 依存性
**ソースコードの依存性は円の内側だけに向かう。**

円の中央に近づくほどソフトウェアのレベルが上がり、外側は仕組みを表す。円の内側は外側について何も知らない。つまり、外側で定義されたものを内側で使ってはいけない。

### エンティティ
エンティティは図の中で最も中心に位置する。エンティティは**最重要ビジネスルール**をカプセル化したもの。外部のシステムを変更したとしてもこれらのオブジェクトに影響を与えることはない。

### ユースケース
ユースケースのソフトウェアには**アプリケーション固有**のビジネスルールが含まれる。ユースケースは、データベース、UI、フレームワークなどの外部の影響は受けない。

覚えておくこと：**ユースケースInteractorを用いてControllerとPresenterを良い感じに連携させる！**(図の右下を参照)

### インターフェイスアダプター
インターフェイスアダプターのソフトウェアは、ユースケースやエンティティに便利なフォーマットから、データベースやウェブなどの外部に便利なフォーマットに変換する。

このレイヤーでは以下の概念がある
- Gateway
    - データに関する抽象化
    - Repositoryはここ
- Presenter
    - Interactorから受け取ったデータをViewに適した形へ
- Controller
    - 受け取ったデータを変換してusecase(Input Boundary)に渡す
### 境界線を超えるには？
図の右下に例があるように、インターフェイスを呼び出すことで解決する！
いったん、コントローラーとプレゼンターをよしなに連携させる、と認識しておく


## TODO
Crean Architectureを使ってAPI作ってみる

## References
- [Clean Architecture 達人に学ぶソフトウェアの構造と設計](https://www.kadokawa.co.jp/product/301806000678/)

- [Pythonでゆっくり学ぶ「依存関係逆転の原則」](https://qiita.com/kobori_akira/items/ff3bae17b90f7adb04cf)

