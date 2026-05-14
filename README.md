# Python 教學教材專案

> 資展國際 2026 年度 Python 課程教材
>
> 包含 Python 基礎與進階課程的完整教材、範例程式碼與練習題

## 📚 專案概覽

本專案為完整的 Python 教學教材庫，涵蓋從零基礎到進階主題的系統化課程內容。專案採用分層架構設計，將基礎與進階課程分離為獨立的 Git 子倉庫，便於版本管理與內容更新。

### 專案結構

```
python_material/                # 主專案目錄
├── README.md                   # 專案說明文件（本文件）
├── python_basic.md             # Python 基礎課程教材（主文件）
├── python_advanced.md          # Python 進階課程教材（主文件）
├── SPEC/                       # 規格文件與開發指引
│   ├── MAIN.md                # 主要規格說明
│   └── PROMPT_GUIDE.md        # AI 提示詞指引
├── python_basic/              # Python 基礎課程 [獨立 Git Repo]
│   ├── .git/                  # 獨立的 Git 版本控制
│   ├── README.md              # 基礎課程說明
│   ├── python_basic.md        # 基礎課程完整教材
│   ├── examples/              # 範例程式碼
│   ├── practice/              # 課堂練習
│   ├── homework/              # 回家作業
│   ├── demo/                  # 教學示範
│   ├── info_graphics/         # 教學視覺化素材
│   └── SPEC/                  # 基礎課程規格文件
└── python_advanced/           # Python 進階課程 [獨立 Git Repo]
    ├── .git/                  # 獨立的 Git 版本控制
    ├── README.md              # 進階課程說明
    ├── python_advanced.md     # 進階課程完整教材
    ├── unit01_oop_basics/     # 單元1: 物件導向基礎
    ├── unit02_modularity/     # 單元2: 模組化設計
    ├── unit03_builtin_modules/# 單元3: 內建模組應用
    ├── unit04_closure_decorator/ # 單元4: 閉包與裝飾器
    ├── unit05_file_data_processing/ # 單元5: 檔案與資料處理
    ├── unit06_sql_database/   # 單元6: SQL 資料庫
    ├── unit07_nosql_data/     # 單元7: NoSQL 資料處理
    ├── final_project/         # 期末專案範例
    ├── SPEC/                  # 進階課程規格文件
    └── 待整理資料.md          # 教材整理筆記
```

## 🎯 課程大綱

### Python 基礎課程 (python_basic)

**適合對象**：零基礎學員  
**課程時數**：約 24 小時  
**教材文件**：`python_basic.md`

#### 課程主題

1. **環境設定**

   - Anaconda 安裝與配置
   - conda vs pip 套件管理
   - VS Code 開發環境設定

2. **變數、資料型別、字串組合與運算**

   - 變數命名規範（PEP 8）
   - 基本資料型別（int, float, str, bool）
   - 算術與邏輯運算
   - 字串格式化（f-string）
   - 容器資料型別（list, tuple, dict, set）

3. **程式設計基礎流程與結構**

   - 條件判斷（if/elif/else）
   - 迴圈（for/while）
   - 流程控制（break/continue）

4. **視窗程式設計入門（Tkinter GUI）**

   - 基本視窗建立
   - 常用元件（Label, Button, Entry）
   - 事件處理

5. **錯誤處理**

   - 常見錯誤類型
   - try-except 使用
   - 除錯技巧

6. **字串與串列操作**

   - 字串索引與切片
   - 字串常用方法
   - 串列操作技巧

7. **元組、字典與集合**

   - 資料結構特性與應用
   - 資料結構轉換

8. **函式設計**
   - 函式定義與呼叫
   - 參數傳遞（位置、關鍵字、預設值）
   - 變數作用域
   - Lambda 匿名函式
   - 常用函式庫（math, datetime, random, os, json）

#### 檔案結構

```
python_basic/
├── examples/              # 範例程式碼（按主題編號）
│   ├── 00_hello.py       # Hello World
│   ├── 01_string_format.py
│   ├── 02-1_variables_naming.py
│   ├── 02-2_data_types.py
│   ├── 02-3_operations.py
│   ├── 02-4_type_conversion_precedence.py
│   ├── 02-5_input.py
│   ├── 03_conditional_statements.py
│   ├── 03_for_loops.py
│   ├── 03_while_loops.py
│   ├── 04_Tkinter01.py
│   ├── 04_Tkinter02_grid.py
│   ├── 05_error_exception.py
│   ├── 05_lists.py
│   ├── 10_functions.py
│   ├── 10_function_before.py
│   ├── 10_function_after.py
│   └── 11_common_libraries.py
├── practice/             # 課堂練習
│   ├── cost_exercise.py
│   ├── if_exercise.py
│   ├── for_loop_exercise.py
│   ├── while_loop_exercise.py
│   ├── string_slicing_practice.py
│   └── string_exercise.py
├── homework/             # 回家作業
│   ├── exercise_1_basic_calculations.py
│   ├── exercise_2_grade.py
│   ├── exercise_3_even_odd.py
│   ├── exercise_4_sum.py
│   ├── exercise_5_max_value.py
│   ├── exercise_6_guess_number.py
│   ├── exercise_7_nested_loops.py
│   ├── exercise_9_string_methods_exercise.py
│   └── exercise_10_lucky_number_logger.py
└── demo/                 # 教學示範
    ├── cost_example.py
    ├── if_else_example.py
    ├── for_while_example.py
    ├── string_example.py
    ├── string_methods_example.py
    └── string_slice.py
```

**檔案編號規則**：

- `00-01` 系列：入門與基礎語法
- `02` 系列：變數、型別與運算
- `03` 系列：流程控制
- `04` 系列：GUI 視窗程式
- `05` 系列：進階主題（錯誤處理、資料結構）
- `10` 系列：函式設計

### Python 進階課程 (python_advanced)

**適合對象**：具備 Python 基礎的學員  
**課程時數**：約 32 小時  
**教材文件**：`python_advanced.md`

#### 課程主題

1. **物件導向程式設計基礎 (unit01_oop_basics)**

   - 類別與物件
   - 繼承與多型
   - 封裝
   - 練習：學生成績系統、洗衣機模擬、課程管理系統

2. **模組化設計 (unit02_modularity)**

   - 模組導入與使用
   - 套件結構
   - 練習：三明治製作系統

3. **內建模組應用 (unit03_builtin_modules)**

   - datetime：日期時間處理
   - json, sys：系統與資料交換
   - math：數學運算
   - os, pathlib：檔案系統操作
   - random：隨機數生成

4. **閉包與裝飾器 (unit04_closure_decorator)**

   - 閉包概念與應用
   - 裝飾器設計模式
   - 實用裝飾器：登入驗證、執行時間測量

5. **檔案與資料處理 (unit05_file_data_processing)**

   - 檔案讀寫操作
   - CSV 資料處理
   - JSON 資料操作
   - 錯誤處理與資料清理
   - 練習：成績管理、資料備份、整合系統

6. **SQL 資料庫 (unit06_sql_database)**

   - SQLite 基礎操作
   - CRUD 操作（Create, Read, Update, Delete）
   - 查詢語法
   - JOIN 表格關聯
   - 交易處理
   - 練習：資料庫建立、成績統計、圖書館系統

7. **NoSQL 資料處理 (unit07_nosql_data)**

   - TinyDB 基礎
   - 查詢操作
   - 練習：待辦事項系統

8. **期末專案 (final_project)**
   - 整合型專案範例
   - 資料庫設計
   - 模型定義
   - 工具函式

#### 單元結構

每個單元包含：

- `example*.py`：範例程式碼（漸進式教學）
- `exercise*.py`：練習題目
- `README.md`：單元說明文件（部分單元）

## 🔧 技術規格

### Git 架構

本專案採用 **嵌套 Git 倉庫** 架構：

- **主倉庫**：管理整體教材架構、文件與版本
- **子倉庫**：
  - `python_basic/`：獨立維護基礎課程內容
  - `python_advanced/`：獨立維護進階課程內容

> **⚠️ 重要提醒**：  
> `python_basic/` 和 `python_advanced/` 目前以內嵌 Git 倉庫方式管理。  
> 建議未來轉換為 **Git Submodule** 以改善協作與版本同步。

### 轉換為 Submodule 的步驟

```bash
# 1. 記錄子倉庫的遠端 URL
cd python_basic
git remote -v  # 記下 origin URL

cd ../python_advanced
git remote -v  # 記下 origin URL

# 2. 回到主倉庫，移除內嵌的 Git 目錄
cd ..
git rm --cached python_basic python_advanced
rm -rf python_basic/.git python_advanced/.git

# 3. 添加為 submodule
git submodule add <python_basic_repo_url> python_basic
git submodule add <python_advanced_repo_url> python_advanced

# 4. 提交變更
git commit -m "轉換為 Git Submodule 架構"
```

### 開發環境

- **Python 版本**：3.10+
- **套件管理**：Anaconda / conda
- **IDE**：VS Code（推薦）
- **版本控制**：Git

### 必要套件

```bash
# 建立虛擬環境
conda create -n python_material python=3.10

# 啟用環境
conda activate python_material

# 安裝基礎套件
conda install numpy pandas matplotlib

# 進階課程額外套件
pip install tinydb
```

## 📖 使用指南

### 教師使用

1. **課程準備**

   - 閱讀 `python_basic.md` 或 `python_advanced.md` 教材
   - 檢閱 `examples/` 資料夾的範例程式碼
   - 準備 `demo/` 示範檔案

2. **課堂教學**

   - 依序講解教材章節
   - 使用範例程式碼示範
   - 引導學員完成 `practice/` 練習

3. **作業指派**
   - 指派 `homework/` 資料夾的作業
   - 提供範例解答參考

### 學員使用

1. **環境設定**

   - 依照教材第 1 章安裝 Anaconda
   - 設定 VS Code 開發環境
   - 下載教材資料夾

2. **自主學習**

   - 閱讀教材章節
   - 執行並理解範例程式碼
   - 完成課堂練習與作業

3. **問題解決**
   - 參考錯誤處理章節
   - 查看範例程式碼的註解
   - 使用 VS Code 除錯功能

## 📝 版本紀錄

### 最新更新 (2026-04-22)

#### 主倉庫

- ✅ 更新教材架構與範例檔案路徑
- ✅ 修正 `python_basic.md` 所有範例檔案路徑
- ✅ 重構 Python 進階課程單元結構（8 單元 → 7 單元）
- ✅ 新增完整的 README.md 專案說明文件

#### python_basic 子倉庫

- ✅ 重構範例檔案結構與命名規範
- ✅ 新增檔案：GUI 範例、函式設計範例、視覺化素材
- ✅ 採用數字前綴分類系統（02-1, 02-2 等）

#### python_advanced 子倉庫

- ✅ 單元編號重新排序（unit02-08 → unit01-07）
- ✅ 新增期末專案範例程式碼
- ✅ 新增課程 README 與規格文件

### 近期規劃

- [ ] 轉換為 Git Submodule 架構
- [ ] 增加更多實務專案範例
- [ ] 製作教學影片連結
- [ ] 新增線上測驗系統
- [ ] 建立學員專屬討論區

## 🤝 貢獻指南

歡迎提供教材改進建議或錯誤回報：

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📧 聯絡資訊

**課程負責人**：kemiedon  
**機構**：資展國際  
**年度**：2026

## 📄 授權

本教材僅供教學使用，未經授權不得用於商業用途。

---

**最後更新**：2026 年 4 月 22 日  
**文件版本**：1.0.0
