# Python 入門課程

範例檔下載
![截圖 2025-12-30 晚上8.08.51](https://hackmd.io/_uploads/rywr7S-V-x.png)

請至 [https://github.com/kemiedon/python_basic](https://github.com/kemiedon/python_basic) 下載

## 什麼是 Python?

Python 是一種簡潔又強大的高階程式語言，以「可讀性高、開發效率快」著稱。
它被廣泛應用於各種領域，就像一把瑞士刀，從網頁開發、資料分析、人工智慧到自動化作業，都能拿出來用。
因語法簡潔易懂，常被作為第一門學習的程式語言，
幫助初學者理解邏輯思維與運算概念。
![截圖 2026-01-29 晚上10.45.02](https://hackmd.io/_uploads/BJ3FMgFU-x.png)

### 網頁開發（Web Development）

透過框架如 **Django**、**Flask**，可以快速建立網站或後端服務。
**應用範例：** 部落格系統、會員管理平台、電商網站。

### 資料分析與科學運算（Data Science）

使用 **NumPy**、**Pandas**、**Matplotlib** 等套件，可進行資料整理、統計分析與視覺化。
**應用範例：** 學生成績分析、銷售趨勢報表、財務預測。

### 人工智慧與機器學習（AI & ML）

結合 **TensorFlow**、**PyTorch**，可用於影像辨識、自然語言處理與推薦系統。
**應用範例：** ChatGPT、影像分類模型、語音助理。

### 自動化與爬蟲應用（Automation & Web Crawling）

可用 **Selenium**、**BeautifulSoup** 寫出自動化腳本或爬取網站資料。
**應用範例：** 自動下載檔案、批次寄信、蒐集新聞資料。

---

## 1. 環境設定

### 什麼是 Anaconda？

Anaconda 是專為科學計算、資料分析、機器學習設計的 Python 發行版本。內建許多資料科學常用套件，也提供強大的「環境管理」與「套件管理」功能
下載安裝:https://www.anaconda.com/download

![02_為何要使用Anaconda_infographic](https://hackmd.io/_uploads/BJgz7kJv-g.jpg)

### Anaconda 內建工具一覽

| 工具                   | 功能說明                                        |
| ---------------------- | ----------------------------------------------- |
| **Anaconda Navigator** | GUI 操作介面，可啟動 Jupyter、Spyder 等工具     |
| **Jupyter Notebook**   | 互動式程式筆記本，適合資料分析與教學使用        |
| **Spyder**             | Python IDE，類似 MATLAB 的操作介面              |
| **VS Code**            | 微軟推出的程式編輯器，需額外下載                |
| **conda**              | 指令列套件與環境管理工具（與 pip 類似但更強大） |

### 什麼是 conda 與 pip？

在學習 Python 開發過程中，我們經常會用到「套件」來擴充功能（如：資料分析、網頁開發、視覺化等），這些套件通常需要透過套件管理工具來安裝與管理。

Python 中最常見的兩種套件管理工具是：

- `pip`：Python 官方內建的套件管理工具
- `conda`：Anaconda 平台的套件與環境管理工具

### conda vs pip 差異

| 項目         | `conda`              | `pip`                       |
| ------------ | -------------------- | --------------------------- |
| 管理對象     | Python + 套件 + 環境 | 只管理 Python 套件          |
| 支援套件來源 | Conda repository     | PyPI (Python Package Index) |
| 虛擬環境     | `conda create`       | `venv` 或 `virtualenv`      |
| 相依性解決   | 更強大               | 可能發生衝突                |

✅ 建議：使用 Anaconda 時，優先用 conda install，若找不到套件再使用 pip install。

### 常見 conda 指令速查表

```
# 檢查 conda 版本
conda --version

# 建立新的虛擬環境
conda create -n myenv python=3.10

# 啟用環境
conda activate myenv

# 安裝套件
conda install numpy

# 移除套件
conda remove numpy

# 更新套件
conda update pandas

# 查看所有環境
conda env list

# 匯出環境需求檔
conda env export > environment.yml

# 從需求檔建立環境
conda env create -f environment.yml

```

### 實務演練

1. 下載並安裝 Anaconda（選擇包含 Python 3.10+）
2. 透過 `conda create -n pyclass python=3.10` 建立開發環境
3. 安裝 VS Code 並設定 Python Extension
4. 在 VS Code 中開啟 `.py` 檔並執行 `print("Hello, Python!")`
5. 使用 `conda install numpy pandas matplotlib` 安裝常用套件
6. 建立專案資料夾與基本程式碼結構（如 `main.py`）

:::info
初階練習只要在 VS Code 裡執行 Python 程式即可；Anaconda 主要用在進階主題（資料分析、機器學習）或需要管理多個開發環境時再使用。
:::

### 回家小作業 1

#### 完成套件與環境安裝練習

### 💡 補充：VS Code 教學指引

- 開啟專案資料夾後，按下 `Ctrl + Shift + P`，搜尋 `Python: Select Interpreter`，選擇 Anaconda 虛擬環境
- 安裝擴充功能：`Python`、`Jupyter`、`Pylance`
- 可在 VS Code 中使用「右上角 ▶️ 執行」或「右鍵 → Run Python File」直接執行

---

### 檢查與練習

| 練習項目                    | 說明                                               |
| --------------------------- | -------------------------------------------------- |
| ✅ 檢查 Python 是否安裝成功 | 終端機輸入 `python --version` 或 `conda --version` |
| ✅ 練習切換虛擬環境         | VS Code 中選擇正確 conda 環境                      |
| ✅ 執行 Hello World 程式    | 建立一個 `main.py` 並印出 "Hello, Python!"         |
| ✅ 練習安裝套件             | 使用 `conda install` 或 `pip install` 安裝指定套件 |

---

### 延伸學習資源

- [Anaconda 安裝教學](https://www.anaconda.com/products/distribution)
- [VS Code 官方下載](https://code.visualstudio.com/)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [conda 指令速查表](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)

---

## 2. 變數、資料型別、字串組合與運算

### 變數命名規則

- 必須以 英文字母或底線 \_ 開頭
- 可包含數字，但不能以數字開頭
- 不能使用保留字（如 if、for、class）
- 建議使用有意義的英文名稱（全英文、小寫＋底線）

### 命名風格對照(根據官方的風格指南 PEP8)

✅ 好的命名

| 命名風格                               | 用途說明                                               | 範例                                          |
| -------------------------------------- | ------------------------------------------------------ | --------------------------------------------- |
| **`snake_case`**                       | 適用於函式名稱、方法名稱、變數名稱、模組名稱和套件名稱 | `my_function`、`calculate_total`、`user_name` |
| **`CamelCase`**                        | 適用於類別名稱（首字母大寫）                           | `MyClass`、`UserAccount`、`HttpRequest`       |
| **`SNAKE_CASE`**                       | 用於模組或套件中的**常數名稱**                         | `MAX_CONNECTIONS`、`DEFAULT_PORT`             |
| **`_single_leading_underscore`**       | 表示內部使用（private），不建議外部呼叫                | `_internal_helper`                            |
| **`__double_leading_underscore`**      | 內部變數名稱混淆，避免與子類別衝突（名稱改寫）         | `__mangled_variable`                          |
| **`__double_underscore__`** （dunder） | 內建特殊方法與屬性                                     | `__init__`、`__str__`、`__len__`              |

**<span style="color: brown;">範例檔參考: examples/02-1_variables_naming.py</span>**

### 基本資料型別

Python 中的基本資料型別常見有：

| 型別    | 說明           | 範例               |
| ------- | -------------- | ------------------ |
| `int`   | 整數           | `10`、`-5`         |
| `float` | 浮點數（小數） | `3.14`、`-0.5`     |
| `str`   | 字串           | `'Hello'`、`"123"` |
| `bool`  | 布林值         | `True`、`False`    |

### 範例

```python
age = 18          # int
pi = 3.14159      # float
name = "Alice"    # str
is_student = True # bool
```

#### 注意事項

- 字串必須用 ' 或 " 包起來。
- 布林值是 True 和 False（首字母需大寫)

**<span style="color: brown;">範例檔參考: examples/02-2_data_types.py</span>**

### 數值運算處理

### 算術運算子與邏輯運算子

算術運算子用於執行基本的數學計算，而邏輯運算子用於組合關係運算的結果（True 或 False），以進行更複雜的條件判斷，通常在 if 或 elif 中使用。

#### 算術運算子一覽表

|  運算子  |     名稱     |   範例   | 說明                       | 結果 |
| :------: | :----------: | :------: | :------------------------- | :--: |
|  **+**   |     加法     | `5 + 3`  | 將運算元相加               |  8   |
|  **-**   |     減法     | `5 - 3`  | 將左邊減去右邊             |  2   |
|  **\***  |     乘法     | `5 * 3`  | 將運算元相乘               |  15  |
|  **/**   |     除法     | `5 / 2`  | 標準除法，結果為**浮點數** | 2.5  |
|  **//**  | **地板除法** | `5 // 2` | 除法後，**向下取整**       |  2   |
|  **%**   |  **取餘數**  | `5 % 2`  | 傳回除法的餘數             |  1   |
| **\*\*** |   **次方**   | `5 ** 2` | 左邊運算元的右邊運算元次方 |  25  |

```python=
a = 15
b = 4

print("--- 變數設定 ---")
print(f"變數 a = {a}")
print(f"變數 b = {b}")
print("----------------")

# 1. 加法 (+)
# 範例: 15 + 4
print(f"1. 加法 (a + b): {a + b}")

# 2. 減法 (-)
# 範例: 15 - 4
print(f"2. 減法 (a - b): {a - b}")

# 3. 乘法 (*)
# 範例: 15 * 4
print(f"3. 乘法 (a * b): {a * b}")

# 4. 除法 (/) - 結果會是浮點數
# 範例: 15 / 4 = 3.75
print(f"4. 除法 (a / b): {a / b}")

# 5. 地板除法 (//) - 取小於或等於該數的最大整數
# 範例: 15 // 4 = 3
print(f"5. 地板除法 (a // b): {a // b}")

# 6. 取餘數 (%)
# 範例: 15 除以 4 餘 3
print(f"6. 取餘數 (a % b): {a % b}")

# 7. 次方 (**)
# 範例: 4 的 3 次方 (我們將變數位置對調，方便看出結果)
print(f"7. 次方 (b ** 3): {b ** 3}")
```

**<span style="color: brown;">範例檔參考: examples/02-3_operations.py</span>**

### 隨堂練習

<span style="color: darkblue;">開啟 cost_exercise.py，完成下列練習題</span>
:::info

#### 1. 計算與型別：

假設書本 250 元，咖啡 75 元。計算總花費。

#### 2. 購物找零

你買了 3 瓶價格為 45 元的飲料和 2 個價格為 30 元的三明治。
如果你用一張 500 元的鈔票付款，請問應該找回多少錢？

#### 3. 分糖果

有 100 顆糖果，要分給 8 個小朋友。請計算每個小朋友可以分到幾顆糖果？剩下幾顆糖果？

:::

**<span style="color: brown;">範例檔參考: demo/cost_example.py</span>**
**<span style="color: darkblue;">練習檔參考: practice/cost_exercise.py</span>**

---

### 字串的組合

在 Python 中組合字串的兩種主要方法：使用 + 運算子和使用 f-string，並提供簡單的範例。

這兩種方法都能達到組合字串的目的，但在可讀性、效能和方便性上有所不同。

![11_f_string為什麼重要_infographic](https://hackmd.io/_uploads/S1g6J3tUWx.jpg)

### 1. 使用 + 運算子進行字串相加 (Concatenation)

這是最直觀的方法，就像數學中的加法一樣，+ 運算子可以將兩個或多個字串「相加」在一起，組合成一個新的字串。

**特點：**

- **直觀易懂**：對於簡單的串接，語法非常清晰。
- **需要手動轉型別**：如果想將非字串類型（如數字 int 或 float）與字串組合，必須手動使用 str() 函數將其轉換為字串，否則會引發 TypeError。
- **效能考量**：在大量字串串接的場景下（例如在迴圈中組合上千個短字串），效能會比 f-string 差，因為每次 + 操作都會產生一個新的字串物件。

#### 範例

```python
# --- 範例 1: 基本的字串串接 ---
first_name = "Grace"
last_name = "Hopper"

# 使用 + 組合姓名，並在中間加上空格和逗號
full_name = last_name + ", " + first_name
print(f"使用 '+' 組合的結果: {full_name}")


# --- 範例 2: 組合字串與數字 (需要手動轉型) ---
item = "筆記型電腦"
price = 35000

# 錯誤示範：直接將字串與數字相加會導致 TypeError
# description = "商品: " + item + ", 價格: " + price  # 這行會報錯

# 正確作法：使用 str() 將數字轉換為字串
description = "商品: " + item + ", 價格: " + str(price)
print(f"使用 '+' 組合字串與數字: {description}")

```

### 2. 使用 f-string (格式化字串字面值, Formatted String Literals)

f-string 是 Python 3.6 版以後引入的功能，是一種非常現代、高效且可讀性極佳的字串格式化方法。

**特點：**

- **可讀性高**：直接在字串中嵌入變數或表達式，結構清晰，看起來就像最終輸出的樣子。
- **自動轉型別**：它會自動將 {} 中的變數轉換成字串形式，無需手動呼叫 str()，非常方便。
- **高效能**：在大多數情況下，f-string 是組合字串最快的方法。
  功能強大：你可以在 {} 中放入任何有效的 Python 表達式，例如進行數學運算、呼叫函數等。

```python

# f-string 會自動處理數字轉型
description = f"商品: {item}, 價格: {price}"
print(f"使用 f-string 組合字串與數字: {description}")


# 在 f-string 中使用表達式
quantity = 2
total_price = f"總價是 {price * quantity} 元" # 直接在 {} 中進行運算
print(f"在 f-string 中運算: {total_price}")
```

**<span style="color: brown;">範例檔參考: examples/02-4_type_conversion_precedence.py</span>**

### 3. 使用 print 輸出訊息

- 可以印出文字：print("歡迎來到天氣穿搭小程式")。
- 可以印出變數：print("今天的天氣是：", weather)，逗號會自動幫你加空白並轉成字串
- 可以同時印出多個東西：print("總分：", score, "平均：", avg)。
  :::info
  print() 很常搭配 f-string 一起用，讓字串裡直接夾變數，例如：print(f"今天建議穿搭是：{outfit}")，可讀性高又方便。
  :::

### 4.使用 input 取得使用者輸入

input() 用來向使用者要一段輸入，並把輸入存成字串（str 型別）。

基本用法：

```python=
變數名稱 = input("提示文字：")
```

例如：weather = input("請輸入今天天氣（晴天/陰天/下雨）：")。
![截圖 2026-01-30 下午4.56.06](https://hackmd.io/_uploads/r1vNzxqLbx.png)

這行會先在螢幕上顯示括號裡的提示文字。
等使用者輸入內容並按 `Enter`之後，把輸入的字存到 weather 這個變數。

因為 `input()` 回傳的一律是字串，如果你需要數字，要再轉型
例如：

```python=
x = int(input("請輸入數字x："))
y = int(input("請輸入數字y："))

result = x + y
print(f"x + y 的結果是：{result}")
```

先讓使用者輸入，再用 int() 轉成整數。

**<span style="color: brown;">範例檔參考: examples/02-4_type_conversion_precedence.py</span>**

---

### 常用容器資料型別

### 為什麼需要「容器」？

在寫程式時，我們常會需要儲存「多個資料」。如果我們只用單一變數來儲存，例如：

```python
score1 = 90
score2 = 85
score3 = 78
```

這樣會很難一次處理或統計所有分數。這時候就需要能「裝多個資料」的資料結構，我們稱之為 **資料容器（Data Container）**。

### 什麼是資料容器？

資料容器就像不同類型的「資料盒子」，每種盒子有不同的特性和用途。

| 類型              | 說明                  | 範例                                                   | 特性                     |
| :---------------- | :-------------------- | :----------------------------------------------------- | :----------------------- |
| **List（串列）**  | 有順序、可修改        | `["apple", "banana", "cherry"]`                        | 可新增、刪除、改值       |
| **Tuple（元組）** | 有順序、不可修改      | `("red", "green", "blue")`                             | 用於保護資料不被意外修改 |
| **Dict（字典）**  | 鍵值配對（key:value） | `{"name": "Tom", "age": 18}`                           | 可快速查找資料           |
| **Set（集合）**   | 無順序、不重複        | `{"apple", "banana", "apple"}` → `{"apple", "banana"}` | 自動去除重複值           |

### 📦 容器的概念表

如果用生活中的例子來比喻，可以這樣理解：
![12_為什麼需要容器，什麼是容器_infographic](https://hackmd.io/_uploads/Bk9eg2KLZl.jpg)

---

## 3. 程式設計基礎流程與結構

### `if`、`elif`、`else` 條件判斷

![05_條件判斷為什麼很重要_infographic](https://hackmd.io/_uploads/BJiGentUZx.jpg)

:::info
條件判斷是程式碼中的「決策者」。它讓程式能根據條件是否成立，來執行不同的程式碼區塊。
:::

想像你在做生活中的選擇題：

- **`if` (主要條件)**：這是你的第一個、最重要的判斷。
  - **範例：** **如果**今天天氣是晴天，我就去公園跑步。
- **`elif` (次要條件)**：這是當第一個判斷不成立時，你接下來考慮的備用選項。可以有很多個。
  - **範例：** **否則，如果**今天是陰天，我就去健身房。
- **`else` (最終備案)**：這是所有條件都不成立時，你不得不執行的最終行動。
  - **範例：** **否則**（如果既不是晴天也不是陰天，例如下雨），我就在家看書。

> **重點：** Python 使用**縮排**（空格）來定義「如果條件成立，要做什麼事」的程式碼區塊。

#### 範例程式

```python
weather = "下雨"  # 你可以試著改成 "晴天" 或 "陰天" 看看結果！

print(f"\n今天天氣是: {weather}")

# 主要條件: 如果今天天氣是晴天
if weather == "晴天":
    print("我就去公園跑步。")

# 次要條件: 否則，如果今天是陰天
elif weather == "陰天":
    print("我就去健身房。")

# 最終備案: 否則（如果既不是晴天也不是陰天）
else:
    print("我就在家看書。")
```

#### 常見應用情境

**網站登入**：如果使用者名稱和密碼都正確，就顯示個人頁面；否則顯示「密碼錯誤」的訊息。
**App 通知**：如果今天是使用者的生日，發送簡訊通知；否則，如果有未讀訊息，發送提醒；否則不發送任何通知。

### 比較與邏輯運算子

這些運算子常用於條件判斷式，回傳結果通常是布林值（`True` 或 `False`）。

|   類型   |   運算子    | 說明                                                            |
| :------: | :---------: | :-------------------------------------------------------------- |
| **比較** |    `==`     | 等於                                                            |
|          |    `!=`     | 不等於                                                          |
|          |  `>` / `<`  | 大於 / 小於                                                     |
|          | `>=` / `<=` | 大於等於 / 小於等於                                             |
| **邏輯** |    `and`    | 邏輯「與」：兩邊都 `True`，結果才是 `True`                      |
|          |    `or`     | 邏輯「或」：任一邊 `True`，結果即為 `True`                      |
|          |    `not`    | 邏輯「非」：將布林值反轉 (`True` 變 `False`，`False` 變 `True`) |

#### 範例程式

```python
temperature = 30
is_sunny = True

# 複合條件判斷範例 (使用 and / or)
if temperature > 28 and is_sunny:
    print("天氣炎熱且晴朗，適合去游泳！")
elif temperature < 10 or not is_sunny: # not is_sunny 等同於 is_sunny == False
    print("天氣寒冷或多雲，請待在室內。")
else:
    print("天氣狀況還不錯。")
```

比較與邏輯運算子與 if 經常搭配使用，常用於組合多個條件來進行複雜的決策，例如：年齡與收入門檻 (age >= 18 and income >= 30000)。

**<span style="color: brown;">範例檔參考: examples/03_conditional_statements.py</span>**

### 隨堂練習

**<span style="color: darkblue;">練習檔參考: practice/string_slicing_practice.py</span>**

---

### 課堂練習

#### 練習題一：判斷營業時間與狀態

使用 `if-elif-else` 結構判斷多重狀態，模擬商店營業邏輯。

寫一個程式，接收當前時間 `current_hour`（24 小時制）和商店狀態 `is_holiday`（是否為假日）。請根據以下條件判斷商店應顯示的訊息：

1. 如果是假日（`is_holiday` 為 `True`），商店總是印出 "今日公休。"
2. 如果是非假日：
   a. 時間在 9 到 18 點之間（含 9 點，不含 18 點），印出 "營業中，歡迎光臨！"
   b. 其他時間印出 "非營業時間，請明天再來。"

#### 練習題二：判斷會員折扣 (中等)

寫一個程式，根據客戶的消費金額 amount 和是否為會員 is_member 來計算最終應付金額。

- 如果是會員（is_member 為 True）且消費金額超過 1000 元，給予 8 折優惠。
- 如果不是會員但消費金額超過 500 元，給予 9 折優惠。
- 其他情況則不打折。

#### 練習題三：判斷年度季節 (進階)

寫一個程式，接收一個代表月份的整數 month（範圍 1 到 12），並判斷它屬於哪個季節。
春季： 3, 4, 5 月
夏季： 6, 7, 8 月
秋季： 9, 10, 11 月
冬季： 12, 1, 2 月
如果月份不在 1 到 12 的範圍內，印出 "月份輸入錯誤。"
:::

**<span style="color: brown;">範例檔參考: demo/if_else_example.py</span>**
**<span style="color: darkblue;">練習檔參考: practice/if_exercise.py</span>**

### for 迴圈

迴圈就像程式碼世界的**自動化機器人**，用於讓程式碼區塊重複執行，讓你不用一直重複寫一樣的指令。

- **`for` 迴圈 (點名與數數)**：
  - 想像你手上有一個**確定的清單**（例如：一盒 10 顆雞蛋、一組 5 個學生的名單）。
  - `for` 迴圈就是一個個走訪這個清單，把清單裡所有東西都處理一遍。當清單跑完，迴圈就結束。
  - **適用情境：** 當你**知道**要重複做幾次，或者要處理完「某個集合」裡的所有東西時。
  -

![06_為何要使用迴圈_infographic](https://hackmd.io/_uploads/S19nMkFIZe.jpg)

### 使用 range() 函式：執行固定次數

range() 是生成一串數字序列的工具，常用於 for 迴圈依序執行多次：
**range(5): 產生 0, 1, 2, 3, 4(從 0 起跳到 4（不含 5）)**

```python=
for i in range(5):
    print(f"第 {i} 次迴圈")
```

**range(1, 6): 產生 1 到 5(不含 6)**

```python=
for i in range(1, 6):
    print(f"數字 {i}")
```

**range(開始, 結束, 間隔)：從 0 起，每次+2，到 11 前結束**

```python=
# range(0, 11, 2): 產生 0, 2, 4, 6, 8, 10
for i in range(0, 11, 2):
    print(f"偶數 {i}")
```

### 遍歷（Iterate）清單中的每個元素

for 迴圈也可以用來「逐一」取出清單內的項目：

```python=
# 範例：遍歷水果串列
fruits = ["apple", "banana", "kiwi"]
for fruit in fruits:
    print(f"清單中的水果：我要吃 {fruit}！")

# fruit 會依序輸出 "apple"、"banana"、"kiwi"
```

### 遍歷字串中的每個字元

for 迴圈也可用來處理字串內的每一個字：

```python=
message = "Python"
for char in message:
    print(f"字串中的字元：{char}")

# 依序輸出 'P', 'y', 't', 'h', 'o', 'n'
```

### 使用 enumerate() 同時取得索引和值

如果需要同時拿到資料位置（索引）和內容，用 enumerate()：

```python
scores = [95, 88, 76]
for index, score in enumerate(scores):
    print(f"  第 {index + 1} 位學生的分數是 {score}")

# enumerate(scores) 會依序輸出 (0, 95)、(1, 88)、(2, 76)
```

### while 迴圈

- **`while` 迴圈 (達成目標為止)**：
  - 想像你在執行一個任務，但你**不知道**要做幾次，只知道「什麼時候該停」。
  - `while` 迴圈會不斷檢查一個**條件**（例如：「肚子餓不餓？」、「密碼對不對？」）。只要條件是 `True`，它就會一直執行下去。
  - **適用情境：** 當你**不知道**確切次數，但需要不斷重複直到某個目標達成或條件變為 `False` 時。

#### 範例程式

```python
# for 迴圈範例：依序處理清單內所有項目
fruits = ["apple", "banana", "kiwi"]
for fruit in fruits:
    print(f"清單中的水果：我要吃 {fruit}！")

print("-" * 15)

# while 迴圈範例：直到條件滿足才停止
money_needed = 100
money_saved = 0
count = 1

while money_saved < money_needed:
    print(f"第 {count} 次存錢，目前金額：{money_saved}")
    money_saved += 30 # 每次存 30 元
    count += 1

print(f"恭喜！終於存到 {money_saved} 元，可以買玩具了。")

# 迴圈處理串列
for fruit in fruits:
    print(fruit)
# 會逐一印出 apple, cherry, grape

```

**<span style="color: brown;">範例檔參考: examples/03_for_loops.py</span>**

### 搭配 break 和 continue 流程控制

break 和 continue 是迴圈中的「**緊急按鈕**」，讓你可以精準控制迴圈的執行進度。

想像你是一家工廠的員工，正在一條產品檢驗流水線（迴圈）上工作，你的任務是檢查所有送過來的產品：
**break (強制停機**)會立即終止整個迴圈：
就像你突然發現一個嚴重的安全問題，比如輸送帶開始冒火花。
一旦發現這個問題，你會立刻按下紅色緊急按鈕，整條流水線（迴圈）會馬上停下來，後面的產品（數據）連檢查的機會都沒有。

**continue (跳過瑕疵品，跳過本次迴圈的剩餘程式碼)**：
就像你看到一個產品有輕微的外觀刮痕，不合格但無關安全。
你會把這個有刮痕的產品推到旁邊的廢料區，不用再對它進行後續的貼標籤或包裝等步驟，然後馬上開始檢查下一個送來的產品。

`break`：遇到某狀況就「終止整個迴圈」
![15_break和continue的流程控制_infographic](https://hackmd.io/_uploads/SyJ6iAqUbg.jpg)

#### 範例程式

```python
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num > 5:
        print(f"    找到了！數字是 {num}")
        break  # 跳出整個 for 迴圈
    print(f"    檢查數字 {num}...")
```

`continue`：遇到某狀況「跳過本次，繼續下一圈」

```python
# continue 範例：跳過不想要的，繼續往下走
for num in numbers:
    if num % 2 == 0:
        continue  # 跳過偶數，繼續
    print(f"    奇數是: {num}")
```

**<span style="color: brown;">範例檔參考: examples/03_while_loops.py</span>**

#### 應用情境

**break (快速收工)**：
線上考試： 允許使用者嘗試登入 3 次，一旦超過限制，就終止登入迴圈，鎖住帳號。
**continue (篩選跳過)**：
清潔資料： 在處理客戶名單時，如果某個客戶的電話號碼欄位是空的，就跳過此客戶的簡訊發送步驟，直接處理下一個客戶。
遊戲計分： 遍歷遊戲紀錄時，如果玩家的分數是零，就跳過計算該玩家的經驗值。

**<span style="color: darkblue;">課堂練習參考: practice/for_loop_exercise.py</span>**
**<span style="color: darkblue;">課堂練習參考: practice/while_loop_exercise.py</span>**

---

### 回家小作業 1

<span style="color: darkblue;">在 homework 資料夾中, 完成下列練習題</span>

#### 練習題 1：簡易運算

檔名: `exercise_1_basic_calculations.py`

#### 練習題 2：決定分數等級

檔名: `exercise_2_grade.py`

#### 練習題 3：判斷是否為偶數

檔名: `exercise_3_even_odd.py`

#### 練習題 4：求和計算

檔名: `exercise_4_sum.py`

#### 練習題 5：最大值判斷

檔名: `exercise_5_max_value.py`

#### 練習題 6：while 迴圈猜數字

檔名: `exercise_6_guess_number.py`

#### 練習題 7：印出九九乘法表

檔名: `exercise_7_nested_loops.py`

**<span style="color: darkblue;">作業檔參考: homework/</span>**

---

## 4. 視窗程式設計入門（Tkinter GUI）

我們已經會寫「文字介面」的 Python 程式（使用 `input()` / `print()` 在終端機互動）。
本章要帶大家認識如何用 **Tkinter** 做出簡單的「視窗介面（GUI, Graphical User Interface）」程式，例如按鈕、文字框、小視窗等。

---

### 為什麼要學 GUI？

在實務應用中，很多非工程師的使用者，不習慣打指令或看黑底白字的終端畫面。
這時候，如果我們希望程式「給一般人使用」，就會需要一個較友善的 **視覺化介面（GUI）**。
![13_PythonGUI使用_infographic](https://hackmd.io/_uploads/BJiVBntLbg.jpg)

#### 常見的 GUI 使用情境：

- 給同事或家人使用的小工具程式（例如：加總工具、檔名批次更名、小型查詢工具）。
- 學校或公司內部的簡易系統原型（Prototype）。
- 教學展示：把原本在終端機跑的程式「包成一個視窗」，讓學習者更有感。

### 如何在 Python 中使用 GUI(Tkinter)？

#### 範例：按鈕改變標籤文字

```python
import tkinter as tk  # 1. 匯入模組

# 2. 建立主視窗
root = tk.Tk()
root.title("Tkinter Demo")          # 設定視窗標題
root.geometry("300x150")            # 設定視窗大小（寬x高）

# 3. 建立元件
label = tk.Label(root, text="請按下面的按鈕")
label.pack(pady=10)                 # 使用 pack 佈局並加一點垂直間距

def on_click():
    # 6. 事件處理函式：按下按鈕時要做的事
    label.config(text="按鈕已被按下！")

button = tk.Button(root, text="點我", command=on_click)
button.pack(pady=5)

# 7. 啟動事件迴圈
root.mainloop()

```

#### 範例 2: 使用 grid 做小表單

```python
import tkinter as tk

root = tk.Tk()
root.title("登入範例")
root.geometry("300x150")

# Label 與 Entry
tk.Label(root, text="帳號：").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="密碼：").grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_user = tk.Entry(root)
entry_pass = tk.Entry(root, show="*")

entry_user.grid(row=0, column=1, padx=5, pady=5)
entry_pass.grid(row=1, column=1, padx=5, pady=5)

def login():
    user = entry_user.get()
    pwd = entry_pass.get()
    print("登入帳號：", user, " 密碼：", pwd)

tk.Button(root, text="登入", command=login).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

```

![14_使用tkinter標準流程_infographic](https://hackmd.io/_uploads/H1Zs20cLbx.jpg)

**<span style="color: brown;">範例檔參考: examples/04_Tkinter01.py</span>**
**<span style="color: brown;">範例檔參考: examples/04_Tkinter02_grid.py</span>**

---

## 5. 錯誤處理

### 什麼是錯誤（Error）與例外（Exception）

- **錯誤/例外（Exception）**：執行程式時出現的不正常狀況，導致程式無法正常繼續。例如：輸入格式錯誤、檔案未找到、資料型態不符等。
- Python 遇到錯誤時，會「拋出」例外，並顯示**錯誤訊息**，協助我們判斷錯誤位置與原因。

![07_錯誤處理為什麼很重要_infographic](https://hackmd.io/_uploads/ByOWX1KL-e.jpg)

---

### 常見錯誤訊息解析

| 錯誤訊息類型      | 說明與出現時機               | 範例                       |
| ----------------- | ---------------------------- | -------------------------- |
| SyntaxError       | 語法錯誤；打錯、漏括號等     | `print('Hi'` (漏括號)      |
| NameError         | 變數未定義或拼錯名稱         | `print(a)` (a 未宣告過)    |
| TypeError         | 型態錯誤，如將字串與數字相加 | `3 + 'Hello'`              |
| ValueError        | 資料型態正確，但值不合理     | `int('xyz')`               |
| IndexError        | 串列索引超出範圍             | `lst = [1]; print(lst[2])` |
| KeyError          | 字典(key-value)查無鍵        | `d = {}; print(d['key'])`  |
| ZeroDivisionError | 被除數為零                   | `10/0`                     |
| AttributeError    | 呼叫不存在的屬性或方法       | `'abc'.push()`             |
| IndentationError  | 縮排錯誤                     | if 語句後未縮排            |
| FileNotFoundError | 檔案不存在                   | `open('none.txt')`         |

---

### 使用 try-except 處理錯誤

#### 1. try-except 基本用法

```python
try:
    # 可能發生錯誤的程式碼
    num = int(input("請輸入整數："))
    print(10 / num)
except ValueError:
    print("輸入的不是有效整數！")
except ZeroDivisionError:
    print("不能除以零！")
except Exception as e:
    print("發生未知錯誤：", e)

```

**<span style="color: brown;">範例檔參考: examples/05_error_exception.py</span>**

`try`: 嘗試執行一段可能出錯的程式

`except`: 捕捉特定錯誤類型，給予對應處理

`Exception as e`: 捕捉其它沒列出的錯誤

#### 2. finally 和 else

```python
try:
# code
except SomeError:
# 處理
else:
# 沒有錯誤時執行
finally:
# 一定會執行
```

---

### 實務除錯流程

1. **讀懂錯誤訊息**：看紅字提示的錯誤類型（如 NameError、IndexError），注意「最後一行」的錯誤類型及 Traceback 位置。
   ![截圖 2025-10-19 上午8.21](https://hackmd.io/_uploads/ryKKJgQ1bg.png)
2. **找出出錯行號與相關程式碼**：看訊息裡的“line X”或程式碼片段。
3. **檢查常見問題**：變數拼寫正確嗎？縮排是否正確？型態/值是否合乎預期？外部檔案是否存在？
4. **使用 print()/偵錯工具追蹤**：在關鍵步驟前後加 print 看變數內容，或用 VS Code 等 IDE 的「中斷點」、「逐行執行」功能協助追查。
5. **嘗試簡化問題、局部測試**：將程式拆小部分驗證，便於鎖定錯誤位置。

---

### 實作建議

- 練習自己「**刻意**」打出錯誤，觀察 Python 錯誤訊息。
- 多讀多理解 Traceback 訊息，並寫下遇過的錯誤與原因。
- 練習用 try-except 包覆 input、檔案開啟等「易發生錯誤」的動作。
- 嘗試自行設計錯誤處理流程，增強 Debug 能力。

---

## 5.字串與串列操作

### 字串的索引與切片（Indexing & Slicing）

Python 的字串是不可變物件（immutable），但可以透過「索引」或「切片」讀取部分內容。
![08_什麼是字串切片_infographic](https://hackmd.io/_uploads/BJiSO9T8Wg.jpg)

```python=
s = "python"

# 取得第 1 個字元 (索引 0)
print(s[0])  # p

# 取得最後 1 個字元 (負索引)
print(s[-1])  # n

# 切片：從索引 1 取到 3 (含頭不含尾)
print(s[1:4])  # yth

# 切片：從開頭取到索引 1 (含頭不含尾)
print(s[:2])  # py

# 切片：間隔取值 (每 2 個取 1 個)
print(s[::2])  # pto

```

**<span style="color: brown;">範例檔參考: demo/string_example.py</span>**

:::warning
📘 技巧重點：
s[start:end]：取 start 到 end-1 的字元。
s[::-1]：反轉字串。
s[::2]：每隔一個取一次（步長 slicing）。
:::

### 字串拼接與重複

```python
name = "Mandy"
greeting = "Hello, " + name  # 字串相加
repeat = "Hi! " * 3          # 重複輸出
print(greeting)  # Hello, Mandy
print(repeat)    # Hi! Hi! Hi!

```

**<span style="color: brown;">範例檔參考: demo/string_example.py</span>**

:::warning
📘 技巧重點：
使用 + 做字串串接。
使用 \* 可快速生成重複的文字（常用於測試或格式化）。
:::

#### 隨堂練習

<span style="color: darkblue;">在 practice/string_slicing_practice.py, 完成下列練習題</span>

---

### 字串格式化（String Formatting）

#### 字串常用技巧

| 技巧       | 範例                                 |
| ---------- | ------------------------------------ |
| 字串合併   | `"Hello" + "World"` → `'HelloWorld'` |
| 重複       | `"Hi" * 3` → `'HiHiHi'`              |
| 取長度     | `len("Hello")` → `5`                 |
| 切片       | `"Python"[0:3]` → `'Pyt'`            |
| 大小寫轉換 | `"hello".upper()` → `'HELLO'`        |

---

**<span style="color: darkblue;">練習檔參考: practice/string_exercise.py</span>**

:::info

#### --- 練習題 1: 提取檔案副檔名 ---

宣告一個檔案名稱字串，請提取其副檔名 (不包含'.')。

#### --- 練習題 2: 格式化姓名 ---

宣告一個格式混亂的名字字串，請將其整理成標準格式：

#### 1. 移除前後多餘的空白。

#### 2. 將名字轉換為首字大寫的格式 (Title Case)。

messy_name = " alAn tURiNg "
formatted_name = ""

#### --- 練習題 3: 計算句子中的單字數量 ---

目前有一個句子，請計算裡面有多少個單字。
sentence = "Python is a versatile and powerful programming language."

#### --- 練習題 4: 互動式姓名產生器 ---

請撰寫一段程式，完成以下步驟：

1. 使用 input() 提示使用者輸入他們的「姓氏」(last name)。
2. 使用 input() 提示使用者輸入他們的「名字」(first name)。
3. 將姓氏和名字串接起來，並在中間加上一個空格。

#### 4. 使用 print() 印出完整的姓名，格式為 "Hello, [名字] [姓氏]!"。

**<span style="color: brown;">範例檔參考: demo/string_example.py</span>**
:::

---

### 字串常見方法

| 方法             | 功能說明                                 | 範例/用途                                                          | 範例輸出                                                   |
| ---------------- | ---------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------- |
| .lower()         | 將所有字元轉為小寫                       | "Hello WORLD".lower()                                              | hello world                                                |
| .capitalize()    | 首字母大寫，其它小寫                     | "hello world".capitalize()                                         | Hello world                                                |
| .title()         | 每個單字首字母大寫                       | "hello world from python".title()                                  | Hello World From Python                                    |
| .find(sub)       | 尋找子字串第一次出現之位（找不到回傳-1） | "Python Programming".find("Pro")/"Python Programming".find("Java") | 7/-1                                                       |
| .replace(a, b)   | 將 a 全部換成 b                          | "I love Java".replace("Java", "Python")                            | I love Python                                              |
| .split(sep)      | 依分隔符拆成串列（預設空白）             | "apple,banana,orange".split(",")/"Hello World Python".split()      | ['apple', 'banana', 'orange']/['Hello', 'World', 'Python'] |
| .join(list)      | 串列元素以指定字串連接                   | "-".join(["Python","is","awesome"])                                | Python-is-awesome                                          |
| .strip()         | 去除字串前後的空白或指定字元             | " hello world ".strip()                                            | hello world                                                |
| .startswith(pre) | 判斷字串是否以指定字首開頭               | "Python Programming".startswith("Python")                          | True                                                       |
| .endswith(suf)   | 判斷字串是否以指定字尾結尾               | "code.py".endswith(".py")                                          | True                                                       |

### 串列（List）

串列（List）是 Python 最常用的資料結構之一，就像一個可以放任意元素的「籃子」。它可以存放多個資料（整數、字串、甚至其他串列），並且可以隨意存取、修改、刪除裡面的元素。
![04_為何要使用串列List_infographic](https://hackmd.io/_uploads/HJ7i0xc8We.jpg)

**<span style="color: brown;">範例檔參考: examples/07_lists.py</span>**

**基本特性**

- 元素有順序。（位置從 0 開始，也稱為索引）
- 可以存放不同型別的資料。
- 支援「增刪查改」：append, remove, index, 修改元素值。

#### 基本串列宣告

```python=
# 建立一個串列
fruits = ["apple", "banana", "cherry"]
```

#### 取值與修改

```python
print(fruits[0])        # apple
fruits[1] = "orange"   # 把第二個元素改為 orange
print(fruits)           # ["apple", "orange", "cherry"]
```

#### 串列常見操作

```python=
# 新增元素
fruits.append("grape")      # ["apple", "orange", "cherry", "grape"]

# 刪除元素
fruits.remove("orange")     # ["apple", "cherry", "grape"]

# 計算長度
print(len(fruits))          # 3

# 串列合併
more_fruits = ["melon", "kiwi"]
all_fruits = fruits + more_fruits
print(all_fruits)           # ["apple", "cherry", "grape", "melon", "kiwi"]
```

### 串列的索引與切片 (Indexing & Slicing)

說明如何取指定範圍的元素，例如 `fruits[1:3]`。

**範例：**

```python
fruits = ["apple", "banana", "cherry", "melon"]
print(fruits[1:3])  # ['banana', 'cherry']
```

### 判斷元素是否存在

使用 in 運算子檢查元素是否存在。
**範例：**

```python
if "apple" in fruits:
    print("找到蘋果")
```

### 串列排序與反向

使用 .sort() 進行排序，使用 .reverse() 進行反向。
**範例：**

```python
fruits.sort()
fruits.reverse()
```

**<span style="color: brown;">範例檔參考: examples/05_lists.py</span>**

### 串列拷貝

.copy() 方法可建立串列的淺拷貝，但若串列中包含巢狀結構，內層元素仍共用記憶體位置。
**範例：**

```python
new_fruits = fruits.copy()
```

### 巢狀串列（List of Lists）

巢狀串列是指串列中還包含其他串列，例如二維陣列。
**範例：**

```python
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0][1])  # 2
```

### 其他常用的串列方法

- `.extend()`：將另一個串列的元素加入原串列。
- `.count()`：計算指定元素出現次數。
- `.index()`：返回指定元素第一次出現的索引位置。

**範例：**

```python
fruits.extend(["orange", "grape"])
print(fruits.count("apple"))
print(fruits.index("banana"))
```

:::info

### 回家小作業

#### 練習題 9：字串方法練習

**<span style="color: darkblue;">開啟以下檔案練習: homework/exercise_9_string_methods_exercise.py</span>**
:::

## 7. 元組、字典與集合

![12_為什麼需要容器，什麼是容器_infographic](https://hackmd.io/_uploads/Bk9eg2KLZl.jpg)

### 元組 (Tuple)

元組就像「戶籍上的家人名單」，一旦登記好，不能隨意變更順序或內容，只能整組搬運。
**範例**：

```python
family = ("爸爸", "媽媽", "小明")
# family[0] = "哥哥"  # 執行會出錯，因為元組不可修改元素
print(family)
```

**特性:**
元組不可修改（immutable），適合用在需要保證資料不被意外改動的場景。
例：固定的參數設定、星期幾，身份證資訊等不變的資料。

### 字典 (Dictionary)

字典像「聯絡人通訊錄」，電話簿裡姓名是「鍵」，電話號碼是「值」。
**範例**：

```python
contact = {"王大明": "0987654321", "陳小美": "0911223344"}
print(contact["王大明"])       # 取值
contact["陳小美"] = "0933445566" # 修改值
contact["李小強"] = "0955888999" # 新增
del contact["王大明"]           # 刪除
print(contact)
```

**特性：**

- 可依「鍵」快速查詢、增改、刪除資料。
- 常用在需要標示（像編號、姓名、產品編號）的情境，例如：學生名單、產品目錄。

### 集合（Set）

集合就像「同學聚餐打卡名單」，每人只會被記錄一次，不重複計算。
**範例:**

```python
canjia = set(["阿明", "小美", "阿明", "阿光"])
print(canjia)  # 只剩 {'阿明', '小美', '阿光'}，重複自動排除
# 集合運算
banA = set(["阿明", "小美", "阿光"])
banB = set(["小美", "阿光", "小強"])
print(banA | banB) # 聯集（有參加A或B的同學）
print(banA & banB) # 交集（兩個班都有的同學）
print(banA - banB) # 差集（只在A班沒有在B班的同學）
```

**特性:**

- 集合在需要去重、統計時很方便。
- 非常適合問卷資料、重複計算排除、成員比對。
-

### 資料結構選擇與轉換

在撰寫程式時，選擇合適的資料結構就像挑選適合的收納盒。你需要根據「要存放的資料型態」和「使用情境」來決定

資料結構之間可以互相轉換，像是元組可以轉成清單，清單再轉成集合或字典以便不同操作。

#### 如何選擇

- 先判斷資料是不是「不變」→ 選元組。
- 有「鍵值／標籤／對應」需求 → 選字典。
- 有「去重」或「集合運算」需求 → 選集合。
- 若需求改變，利用 Python 內建函式可快速做資料結構轉換，讓資料更好用、更彈性。

情境範例:
假設你原本有一份「不可變」的食譜（元組），但臨時想加一個新食材，還希望快速統計有哪些不重複的食材。

```python
# 原始食譜（元組）
recipe = ("蛋", "牛奶", "吐司", "蛋")

# 需求改變，想要加食材，須先轉清單
recipe_list = list(recipe)
recipe_list.append("起司")  # 新增食材

# 想快速統計有哪些不重複的食材
recipe_set = set(recipe_list)

print("加料後的食譜：", recipe_list)  # ['蛋', '牛奶', '吐司', '蛋', '起司']
print("不重複食材：", recipe_set)   # {'牛奶', '蛋', '吐司', '起司'}
```

:::warning
範例中我們使用了 list() 將元組轉成清單，才能加料或修改。
再用 set() 將清單轉成集合，馬上去掉重複食材。
:::

## 8. 函式設計

### 什麼是函式

![09_函式為什麼很重要_infographic](https://hackmd.io/_uploads/rJhjvcp8Zl.jpg)

函式就像是一個「工具盒」或「小機器」，可以把一些重複的工作自動化。你只要把需要的資料（叫做「參數」）丟進去，它就會幫你處理好，再把結果回傳給你。

### 函式可以做什麼？

- 讓程式碼更簡潔、更好管理：不用一直重複寫一樣的程式，可以直接呼叫函式。
- 自動計算與處理：像是「加法」、「資料檢查」、「格式轉換」等等，都可以寫成函式。
- 模組化設計：有了函式，可以把一個大問題分成很多小部分，各自解決。

#### 1.使用 def 關鍵字定義：

```python
def say_hello():
    print("Hello, Python!")

say_hello()  # 呼叫這個函數，就會印出 Hello, Python!
```

#### 2. 參數傳遞（位置、關鍵字、預設值）

位置參數：根據傳入順序對應

```python
def greet(name, age):
    print(f"{name} 今年 {age} 歲")
greet("小明", 18)
```

關鍵字參數：指定名稱傳值（順序可調整）

```python
greet(age=18, name="小明")
```

預設參數：未輸入時用預設值

```python
def greet(name, age=20):
    print(f"{name} 今年 {age} 歲")
greet("小美")  # age自動是20
```

#### 3. return 回傳值

使用 return 關鍵字把運算結果回傳到主程式

```python
def add(x, y):
    return x + y

result = add(3, 7)  # result 得到 10
```

**<span style="color: brown;">範例檔參考: examples/10_functions.py</span>**

#### 4. 什麼是變數作用域

「變數作用域」指的是一個變數在程式裡「哪裡可以用」、「存活在哪裡」。簡單來說，就是這個變數能不能在某個地方被找到和用到。
![18_為什麼要有作用域_infographic](https://hackmd.io/_uploads/rJhLqcT8-x.jpg)

常見的作用域有兩種：

- **全域變數**：在整個程式裡都能用。例如在程式最外層定義的變數，任何地方都能讀取或改它。

```python
value = 10  # 全域變數

def show():
    print(value)  # 這裡也能用 value
```

使用 `global` 可在函數內修改全域變數

```python
value = 10
def update():
    global value
    value = 99  # 直接改全域
update()
print(value)
```

- **區域變數**：只在「某個函數」或「程式區塊」裡有效，一離開這裡就不存在了。

```python
def func():
    x = 5  # 區域變數，只能在 func 裡用
    print(x)

func()
print(x)  # 這裡會出錯，因為 x 不存在
```

#### 為什麼要有作用域？

- 防止混亂：讓每段程式只用自己的變數，其他地方不會踫到或亂改。
- 管理記憶體：不需要的變數離開區域就自動消失，節省資源。
- 提升安全性：避免重要變數被隨意改動。

#### 什麼是 lambda 匿名函數？

lambda 匿名函數，就是一種「簡短的函數寫法」。
它不用 def 也不用取名字，只要在一行內寫好運算公式，就能馬上用。
![17_什麼是lambda匿名函式_infographic](https://hackmd.io/_uploads/rJteqq6L-e.jpg)

#### lambda 的語法架構

```python
lambda 參數: 運算式
```

**特點：**
匿名：不需要命名（像臨時工，做完就走，不留名字）
寫法短：適合只做一、兩行小事

範例:

```python
add = lambda x, y: x + y
print(add(3, 4))  # 輸出 7
```

搭配 map / filter / sorted 等函式，快速處理資料

```python
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, nums))  # [2, 4, 6, 8]
```

**<span style="color: brown;">範例檔參考: examples/10_functions.py</span>**

### 常用函式庫

#### 1. 數學運算函式庫：`math` 模組

`math` 模組是 Python 內建的數學運算工具箱，支援各種數值計算（如：四則運算、開根號、三角函式、常數...）。
![10_為何要使用模組_infographic](https://hackmd.io/_uploads/H1X3ACcUbl.jpg)

```python
import math

print(math.sqrt(16))      # 根號計算，結果為 4
print(math.pow(2, 8))     # 2 的 8 次方，256
print(math.ceil(3.2))     # 無條件進位，結果為 4
print(math.floor(3.8))    # 無條件捨去，結果為 3
print(math.pi)            # 圓周率常數 3.1415...
```

#### 2. 資料驗證函式範例

常用於檢查資料格式或內容是否合乎規定，常配合標準函式庫如 re（正規表示式模組）：

```python
import re

def 驗證電子郵件(字串):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', 字串) is not None

def 是否正整數(數值):
    return 數值 > 0

print(驗證電子郵件("abc@xyz.com"))  # True
print(驗證電子郵件("hello.world"))  # False
print(是否正整數(-5))               # False
```

#### 3. datetime 模組

用來處理日期、時間的取得、格式化、運算。
常見功能：

- 取得現在時間：datetime.datetime.now()
- 日期格式轉換：strftime 轉字串、strptime 轉回時間物件
- 計算時間差：可直接相減得到秒數、天數等

```python
import datetime

現在 = datetime.datetime.now()
print(現在)  # 顯示目前日期時間

文字格式 = 現在.strftime("%Y-%m-%d %H:%M")
print(文字格式)  # 格式化輸出

明天 = 現在 + datetime.timedelta(days=1)
print(明天)  # 計算一天之後
```

#### 4. random 模組

**用途**：隨機數、亂數抽樣、模擬隨機事件。
**常見功能**：

- 取得 0~1 之間的亂數：random.random()
- 亂數整數：random.randint(a, b)
- 從串列隨機選一個：random.choice(清單)
- 洗牌：random.shuffle(清單)

```python
import random

print("\n--- 2. random 模組 ---")
# 產生一個 1 到 10 之間的隨機整數
random_int = random.randint(1, 10)
print(f"1到10之間的隨機整數: {random_int}")

# 從列表中隨機選擇一個元素
fruits = ["蘋果", "香蕉", "櫻桃", "橘子"]
random_fruit = random.choice(fruits)
print(f"從列表中隨機選擇的水果: {random_fruit}")

# 將列表的元素隨機排序 (原地修改)
print(f"排序前的列表: {fruits}")
random.shuffle(fruits)
print(f"隨機排序後的列表: {fruits}")
print("-" * 20)
```

#### 5. os 模組

**用途**：檔案、資料夾操作，存取環境變數，執行系統指令。
**常見功能**：

- 檢查目前工作目錄：os.getcwd()
- 列出資料夾內容：os.listdir(路徑)
- 建立或移除資料夾：os.mkdir()、os.rmdir()
- 執行外部程式：os.system('指令')

```python
import os

print(os.getcwd())             # 目前目錄
print(os.listdir('.'))         # 現在資料夾的檔案列表
os.mkdir('test')               # 建新資料夾
os.system('echo Hello World')  # 執行系統指令（顯示 Hello World）

```

**<span style="color: brown;">範例檔參考: examples/11_common_libraries.py</span>**

#### 6. json 模組

**用途**：在 Python 與 JSON 之間轉換。
**常見功能**：

- Python 資料型態轉成 JSON 字串：json.dumps(物件)
- JSON 字串轉回 Python 物件：json.loads(字串)
- 讀寫 JSON 檔案：json.dump()、json.load()

```python
import json

person_dict = {"name": "小明", "age": 25, "isStudent": True}
json_string = json.dumps(person_dict, ensure_ascii=False, indent=4)
print("Python 字典轉換為 JSON 字串:")
print(json_string)
print("-" * 20)
```

**<span style="color: brown;">範例檔參考: examples/11_common_libraries.py</span>**
**<span style="color: darkblue;">練習檔參考: examples/practice_11_common_libraries.py</span>**

### 隨堂練習

#### 幸運數字日誌 (Lucky Number Logger)

**任務說明**
請設計一個「幸運數字日誌」程式，讓使用者每天可以記錄自己的幸運數字，並將結果顯示在畫面上。
**要求**：

- 使用 input() 讓使用者輸入「姓名」。
- 使用 random.randint(1, 99) 自動產生一個 1 到 99 之間的幸運數字。
- 設計至少一個自訂函式（例如 format_lucky_message(name, number)），負責組合並回傳要顯示的訊息字串。
- 在主程式中呼叫該函式，印出完整的幸運數字訊息，例如：
- `2025-12-30，今天 Alex 的幸運數字是 7！祝你有美好的一天！`

**程式撰寫建議**：

- 可以額外使用 datetime 模組，在訊息中加入今天的日期。
- 可將輸入處理、訊息格式化、畫面輸出拆成不同函式，練習用函式來組織程式碼。

**<span style="color: darkblue;">開啟以下檔案練習: homework/exercise_10_lucky_number_logger.py</span>**

---

### 實務演練

### 智慧生活小幫手 Smart Life Assistant

#### 目標

綜合應用 Python 基礎語法，建立一個能根據使用者輸入提供「智慧化建議」的小程式。
學生需能運用條件判斷、容器資料結構、迴圈、字典、函式與模組（如 `datetime`、`random`）完成互動式邏輯。

---

#### 任務架構

**基礎任務**
製作一個互動式應用程式，內容需包含：

1. **使用者輸入**：例如輸入姓名、氣溫、心情等資料。
2. **條件判斷**：使用 `if/elif/else` 根據輸入輸出不同結果。
3. **容器應用**：以 `list` 或 `dict` 儲存建議選項（如穿搭、飲食、顏色）。
4. **模組應用**：使用 `datetime` 顯示時間，或 `random` 隨機選擇建議。
5. **格式化輸出**：使用 f-string 或 emoji 讓結果更清晰美觀。

**範例輸出：**
🌤️ Smart Life Assistant 🌤️
請輸入姓名：小明
請輸入今天氣溫：28
請輸入心情（好/普通/差）：好

👉 小明的今日建議：
天氣炎熱，建議穿著輕薄衣物。
午餐推薦：涼麵。
幸運顏色：💙 藍色。

---

#### 進階挑戰（加分）

- 加入 `while` 迴圈讓使用者可多次查詢。
- 使用 `json` 模擬天氣與建議資料。
- 讓程式可輸出日誌檔（`log.txt`），記錄每次查詢結果。
- 延伸模組挑戰：
  - `turtle`：畫出代表今日天氣的圖案。
  - `matplotlib`：將使用者的查詢統計製成簡易圖表。

#### 專題反思

- 我在這個專題中，哪一部分花最多時間理解？
- AI 給我的哪一個提示最有幫助？
- 如果要讓這個程式更有趣，我會加上什麼？

#### 延伸挑戰

若完成度高，可嘗試開發其他版本：

- 「每日任務推薦器」：輸入時間與心情自動生成學習任務。
- 「理財習慣追蹤器」：輸入消費金額並分類記錄。
- 「健康檢查小幫手」：輸入體重與身高計算 BMI 並提供建議。
