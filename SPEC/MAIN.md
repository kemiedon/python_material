# 專案規格書

## 專案描述

本專案是一個關於 Python 進階學習教材。

## 技術棧

- MarkDown 語法
- Python 3.x

## 資料夾結構規範

教材檔案位於 `python_advanced/` 目錄下，按單元組織，**資料夾命名使用英文**：

```
python_advanced/
├── unit01_oop_basics/           # 單元 1：物件導向基礎（OOP）
├── unit02_oop_advanced/         # 單元 2：OOP 進階（繼承、多型）
├── unit03_modularity/           # 單元 3：模組化
├── unit04_builtin_modules/      # 單元 4：Python 內建模組
├── unit05_closure_decorator/    # 單元 5：閉包 & 裝飾器
├── unit06_file_data_processing/ # 單元 6：檔案與資料處理
├── unit07_sql_database/         # 單元 7：關聯式資料庫
├── unit08_nosql_data/           # 單元 8：非關聯式資料
└── final_project/               # 期末整合專案
```

每個單元資料夾內包含：

- `{example_name}_example1.py` - 程式範例 1
- `{example_name}_example2.py` - 程式範例 2
- `exercise_solutions.py` - 練習題解答

## 待辦事項

### 已完成

- 單元 01：物件導向基礎（OOP） — 範例檔已建立
- 單元 03：模組化（把程式拆乾淨） — 範例與練習檔已加入 (`unit03_modularity`)
- 單元 04：Python 內建模組 — 範例與練習檔已加入 (`unit04_builtin_modules`)

### 執行中

- 單元 05：閉包 & 裝飾器 — 教材更新（2025-11-23）：單元說明、生活化範例與練習題已更新於 `python_advanced.md`（範例檔案尚未建立）
- [x] 單元 5：閉包 & 裝飾器 - 建立程式範例檔（教材內容已更新於 `python_advanced.md`；請確認是否要同時建立範例 `.py` 檔）
- [x] 單元 3：模組化（把程式拆乾淨）- 建立程式範例檔
- [x] 單元 4：Python 內建模組 - 建立程式範例檔
- [ ] 單元 5：閉包 & 裝飾器 - 建立程式範例檔

## 指令歷史

以下為與本次教材修改相關的建議或可執行指令（可存為教學操作範例）：

- `python3 closure_counter.py` # 測試閉包計數器範例
- `python3 require_login.py` # 測試登入檢查裝飾器
- `python3 timeit_decorator.py` # 測試計時裝飾器
- `python3 role_decorator.py` # 測試帶參數的權限裝飾器

編輯紀錄（自動）：

- 2025-11-23：更新 `python_advanced.md` 單元 5 — 移除「要示範的課堂活動」、新增生活化程式範例與四則練習題（由 AI 助手修改）。
- [ ] 單元 6：檔案與資料處理 - 建立程式範例檔
- [ ] 單元 7：關聯式資料庫 - 建立程式範例檔
- [ ] 單元 8：非關聯式資料 - 建立程式範例檔
- [ ] 期末整合專案：學生成績管理系統 v3

## 教材整理 Prompt

當整理教材內容時，請遵循以下規則：

1. **Markdown 格式**：使用標準 Markdown 語法
2. **移除 emoji**：所有表情符號都應移除
3. **統一副標題**：
   - 使用「生活化範例」取代「用生活解釋」或「生活例子」
   - 使用「練習題」取代「練習」或其他變體
4. **程式範例**：每個單元需要 2 個程式範例檔
5. **AI 協助學習 Prompt**：
   - 每個單元之後加入「AI 協助學習 Prompt」區塊
   - 提供具體的 prompt 讓學生可以回家練習及複習
   - prompt 應該針對該單元的重點內容
