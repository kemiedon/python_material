# AI 指令規範書

## 語言規定

- **必須使用繁體中文** 進行所有對話和文檔編寫

## 提交規範

- 每當完成一個任務後，自動 push 到 repository
- Commit 訊息按照以下格式命名：`日期-時間-版本[編號]`
  - 範例：`2025-11-22-17:20:46-1.0[建立專案結構]`
  - 日期格式：YYYY-MM-DD
  - 時間格式：HH:MM:SS（24 小時制）
  - 版本編號：1.0, 1.1, 1.2...（主版本.次版本，按照當日提交次數遞增）
  - 編號說明：用方括號括起來的簡要說明
- 每次 commit 說明需要整理該次更新的內容重點

## 指令歷史

### 第 1 個指令（Commit: a）

- 建立 SPEC 文件夾結構
- 建立 MAIN.md（專案規格書）和 PROMPT_GUIDE.md（AI 指令規範書）

### 第 2 個指令（Commit: b）

- 更新 PROMPT_GUIDE.md 加入語言規定和提交規範
- 第一次 commit 並 push

### 第 3 個指令（Commit: c）

- 調整待辦事項，移除文件更新相關項目，只保留教材編修相關部分
- 新建 python_advance.md 檔案作為主要教材內容
- 設定標題為「Python 進階課程」

### 第 4 個指令（Commit: d）

- 更新指令歷史記錄

### 第 5 個指令（Commit: f）

- 整理 Python 進階課程教材內容到 python_advance.md
- 按照規則進行整理：Markdown 格式、移除 emoji、統一副標題語意
- 每個單元加入生活化範例、程式範例、練習題、常見問題
- 每個單元加入 AI 協助學習 Prompt 區塊供學生複習
- 更新 MAIN.md 待辦事項，包含 8 個單元和期末專案

### 第 6 個指令（Commit: g）

- 更新單元 1：物件導向基礎（OOP）教材內容
- 加入「什麼是 OOP（物件導向程式設計）？」完整說明
- 加入物件導向的三個元素表格
- 加入偽代碼和真實 Python 程式範例
- 更新練習題為新的練習內容

### 第 7 個指令（Commit: 2025-11-22-17:XX:XX-1.2）

- 調整單元 1 的教材結構
- 將「什麼是 OOP」和「物件導向的三個元素」表格移至生活化範例上方
- 將原有生活化範例文字保留，放在「物件（Object）是類別（Class）的實例」下方

### 第 8 個指令（Commit: 2025-11-23-10:29:04-1.5）

- 在 `python_advanced/` 資料夾下建立 9 個單元的子資料夾（英文命名）
  - unit01_oop_basics, unit02_oop_advanced, unit03_modularity, unit04_builtin_modules
  - unit05_closure_decorator, unit06_file_data_processing, unit07_sql_database
  - unit08_nosql_data, final_project
- 為單元 1 新增程式範例與練習題解答
  - student_example1.py：Student 類別基礎實作
  - student_example2.py：使用多個物件和排序
  - exercise_solutions.py：練習題解答（Student 類別、WashingMachine 類別）
- 更新 SPEC/MAIN.md 加入資料夾結構規範及說明資料夾命名使用英文
- 標記單元 1 待辦事項為已完成
