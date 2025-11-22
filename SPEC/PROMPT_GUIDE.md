# AI 指令規範書

## 語言規定

- **必須使用繁體中文** 進行所有對話和文檔編寫

## 提交規範

- 每當完成一個任務後，自動 push 到 repository
- Commit 訊息按照以下序列命名：
  - 第 1-26 個：`a`, `b`, `c`, `d`, ... `z`
  - 第 27-52 個：`aa`, `ab`, `ac`, ... `az`
  - 第 53-78 個：`ba`, `bb`, `bc`, ... `bz`
  - 依此類推

## 指令歷史

### 第 1 個指令（Commit: a）
- 建立 SPEC 文件夾結構
- 建立 MAIN.md（專案規格書）和 PROMPT_GUIDE.md（AI 指令規範書）

### 第 2 個指令（Commit: b）
- 更新 PROMPT_GUIDE.md 加入語言規定和提交規範
- 第一次 commit 並 push

### 第 3 個指令（Commit: c）
- 更新 MAIN.md 專案規格書，記錄專案描述、技術棧、待辦事項
- 待辦事項分為：已完成、執行中、未完成三個區塊
- 待辦事項項目前加上 Checkbox

### 第 4 個指令（Commit: c）
- 調整待辦事項，移除文件更新相關項目，只保留教材編修相關部分

### 第 5 個指令（Commit: c）
- 新建 python_advance.md 檔案作為主要教材內容
- 設定標題為「Python 進階課程」

